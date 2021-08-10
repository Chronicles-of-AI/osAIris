from commons.external_call import APIInterface
from sql import config
from sql.crud.import_data_crud import CRUDDataImport
from sql.crud.operation_crud import CRUDOperations
from datetime import datetime


class ImportDatasetController:
    def __init__(self):
        self.CRUDDataImport = CRUDDataImport()
        self.CRUDOperations = CRUDOperations()
        self.gcp_config = config.get("core_engine").get("gcp")

    def create_operation_record(self, api_response: dict):
        """[summary]

        Args:
            api_response (dict): [description]

        Raises:
            error: [description]
        """
        try:
            operation_crud_request = {
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
            raise error

    def create_import_dataset_controller(self, request):
        """[summary]

        Args:
            request ([type]): [description]

        Raises:
            error: [description]

        Returns:
            [type]: [description]
        """
        try:
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
                    "dataset_id": data_import_request.get("dataset_id"),
                    "UUID": uuid,
                    "uri": data_import_request.get("gcs_path"),
                    "status": "Import In-progress",
                }
                self.CRUDDataImport.create(**crud_request)
                self.create_operation_record(api_response=response)
                return response
            else:
                # TODO: error
                pass
                return {"status": "import dataset failed"}
        except Exception as error:
            raise error
