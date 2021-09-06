from commons.external_call import APIInterface
from sql import config, logger
from sql.crud.import_data_crud import CRUDDataImport
from sql.crud.operation_crud import CRUDOperations
from sql.crud.project_flow_crud import CRUDProjectFlow
from datetime import datetime

logging = logger(__name__)


class ImportDatasetController:
    def __init__(self):
        self.CRUDDataImport = CRUDDataImport()
        self.CRUDOperations = CRUDOperations()
        self.CRUDProjectFlow = CRUDProjectFlow()
        self.gcp_config = config.get("core_engine").get("gcp")

    def create_operation_record(self, api_response: dict):
        """[Controller function to create operations record]

        Args:
            api_response (dict): [create operation record response]

        Raises:
            error: [Error raised from controller layer]
        """
        try:
            logging.info("executing create_operation_record function")
            operation_crud_request = {
                "pipeline_id": api_response.get("pipeline_id"),
                "operation_id": api_response.get("operation_id"),
                "status": api_response.get("status"),
                "project_id": api_response.get("project_id"),
                "region": api_response.get("region"),
                "functional_stage": "IMPORT_DATASET",
                "service_id": api_response.get("dataset_id"),
                "created": datetime.now(),
            }
            self.CRUDOperations.create(**operation_crud_request)
        except Exception as error:
            logging.error(f"Error in create_operation_record function: {error}")
            raise error

    def create_import_dataset_controller(self, request):
        """[Controller function to import dataset]

        Args:
            request ([dict]): [import dataset request]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [type]: [import dataset response]
        """
        try:
            logging.info("executing create_import_dataset_controller function")
            uuid = str(int(datetime.now().timestamp()) * 10000)
            data_import_url = (
                self.gcp_config.get("automl").get("common").get("import_dataset")
            )
            data_import_request = request.dict(exclude_none=True)
            response, status_code = APIInterface.post(
                route=data_import_url, data=data_import_request
            )
            if status_code == 200:
                crud_request = {
                    "pipeline_id": data_import_request.get("pipeline_id"),
                    "dataset_id": data_import_request.get("dataset_id"),
                    "UUID": uuid,
                    "uri": data_import_request.get("gcs_path"),
                    "status": "Import In-progress",
                }
                self.CRUDDataImport.create(**crud_request)
                response.update(
                    {
                        "pipeline_id": data_import_request.get("pipeline_id"),
                    }
                )
                self.create_operation_record(api_response=response)
                project_flow_crud_request = {
                    "pipeline_id": data_import_request.get("pipeline_id"),
                    "updated_at": datetime.now(),
                    "functional_stage_id": response.get("operation_id"),
                    "current_stage": "IMPORTING_DATASET",
                }
                self.CRUDProjectFlow.update(**project_flow_crud_request)
                return response
            else:
                raise Exception({"status": "import dataset failed"})
        except Exception as error:
            logging.error(
                f"Error in create_import_dataset_controller function: {error}"
            )
            raise error
