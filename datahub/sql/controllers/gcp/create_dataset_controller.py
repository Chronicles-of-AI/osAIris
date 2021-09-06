from commons.external_call import APIInterface
from sql import config, logger
from sql.crud.dataset_crud import CRUDDataset
from sql.crud.project_flow_crud import CRUDProjectFlow
from datetime import datetime

logging = logger(__name__)


class CreateDatasetController:
    def __init__(self):
        self.gcp_config = config.get("core_engine").get("gcp")
        self.CRUDDataset = CRUDDataset()
        self.CRUDProjectFlow = CRUDProjectFlow()

    def create_text_classification_dataset_controller(self, request):
        """[Controller function to create GCP text classification dataset]

        Args:
            request ([type]): [create text classification request]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [str]: [dataset_name]
            [str]: [dataset_id]
        """
        try:
            logging.info(
                "executing create_text_classification_dataset_controller function"
            )
            uuid = str(int(datetime.now().timestamp()) * 10000)
            create_dataset_url = (
                self.gcp_config.get("automl")
                .get("text")
                .get("create_classification_dataset")
            )
            create_dataset_request = request.dict(exclude_none=True)
            response, status_code = APIInterface.post(
                route=create_dataset_url, data=create_dataset_request
            )
            if status_code == 200:
                crud_request = {
                    "dataset_id": response.get("dataset_id"),
                    "alias_name": create_dataset_request.get("display_name"),
                    "UUID": uuid,
                    "status": "Created",
                    "problem_type": "text_classification",
                }
                self.CRUDDataset.create(**crud_request)
                project_flow_crud_request = {
                    "pipeline_id": create_dataset_request.get("pipeline_id"),
                    "updated_at": datetime.now(),
                    "functional_stage_id": response.get("dataset_id"),
                    "current_stage": "DATASET_CREATED",
                }
                self.CRUDProjectFlow.update(**project_flow_crud_request)
                return {
                    "dataset_name": create_dataset_request.get("display_name"),
                    "dataset_id": response.get("dataset_id"),
                }
            else:
                raise Exception({"status": "create dataset failed"})
        except Exception as error:
            logging.error(
                f"Error in create_text_classification_dataset_controller function: {error}"
            )
            raise error

    def create_ner_dataset_controller(self, request):
        """[Controller function to create GCP NER dataset]

        Args:
            request ([type]): [create ner extraction dataset request]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [str]: [dataset_name]
            [str]: [dataset_id]
        """
        try:
            logging.info("executing create_ner_dataset_controller function")
            uuid = str(int(datetime.now().timestamp()) * 10000)
            create_dataset_url = (
                self.gcp_config.get("automl").get("text").get("create_ner_dataset")
            )
            create_dataset_request = request.dict(exclude_none=True)
            response, status_code = APIInterface.post(
                route=create_dataset_url, data=create_dataset_request
            )
            if status_code == 200:
                crud_request = {
                    "dataset_id": response.get("dataset_id"),
                    "alias_name": create_dataset_request.get("display_name"),
                    "UUID": uuid,
                    "status": "Created",
                    "problem_type": "text_ner",
                }
                self.CRUDDataset.create(**crud_request)
                project_flow_crud_request = {
                    "pipeline_id": create_dataset_request.get("pipeline_id"),
                    "updated_at": datetime.now(),
                    "functional_stage_id": response.get("dataset_id"),
                    "current_stage": "DATASET_CREATED",
                }
                self.CRUDProjectFlow.update(**project_flow_crud_request)
                return {
                    "dataset_name": create_dataset_request.get("display_name"),
                    "dataset_id": response.get("dataset_id"),
                }
            else:
                raise Exception({"status": "create dataset failed"})
        except Exception as error:
            logging.error(f"Error in create_ner_dataset_controller function: {error}")
            raise error

    def create_image_classification_dataset_controller(self, request):
        """[Controller function to create image classification dataset]

        Args:
            request ([type]): [create image classification dataset request]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [str]: [dataset_name]
            [str]: [dataset_id]
        """
        try:
            logging.info(
                "executing create_image_classification_dataset_controller function"
            )
            uuid = str(int(datetime.now().timestamp()) * 10000)
            create_dataset_url = (
                self.gcp_config.get("automl")
                .get("image")
                .get("create_image_classification_dataset")
            )
            create_dataset_request = request.dict(exclude_none=True)
            response, status_code = APIInterface.post(
                route=create_dataset_url, data=create_dataset_request
            )
            if status_code == 200:
                crud_request = {
                    "dataset_id": response.get("dataset_id"),
                    "alias_name": create_dataset_request.get("display_name"),
                    "UUID": uuid,
                    "status": "Created",
                    "problem_type": "image_classification",
                }
                self.CRUDDataset.create(**crud_request)
                project_flow_crud_request = {
                    "pipeline_id": create_dataset_request.get("pipeline_id"),
                    "updated_at": datetime.now(),
                    "functional_stage_id": response.get("dataset_id"),
                    "current_stage": "DATASET_CREATED",
                }
                self.CRUDProjectFlow.update(**project_flow_crud_request)
                return {
                    "dataset_name": create_dataset_request.get("display_name"),
                    "dataset_id": response.get("dataset_id"),
                }
            else:
                raise Exception({"status": "create dataset failed"})
        except Exception as error:
            logging.error(
                f"Error in create_image_classification_dataset_controller function: {error}"
            )
            raise error

    def create_object_detection_dataset_controller(self, request):
        """[Controller function to create object detection dataset]

        Args:
            request ([type]): [create object detection dataset request]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [str]: [dataset_name]
            [str]: [dataset_id]
        """
        try:
            logging.info(
                "executing create_object_detection_dataset_controller function"
            )
            uuid = str(int(datetime.now().timestamp()) * 10000)
            create_dataset_url = (
                self.gcp_config.get("automl")
                .get("image")
                .get("create_object_detection_dataset")
            )
            create_dataset_request = request.dict(exclude_none=True)
            response, status_code = APIInterface.post(
                route=create_dataset_url, data=create_dataset_request
            )
            if status_code == 200:
                crud_request = {
                    "dataset_id": response.get("dataset_id"),
                    "alias_name": create_dataset_request.get("display_name"),
                    "UUID": uuid,
                    "status": "Created",
                    "problem_type": "object_detection",
                }
                self.CRUDDataset.create(**crud_request)
                project_flow_crud_request = {
                    "pipeline_id": create_dataset_request.get("pipeline_id"),
                    "updated_at": datetime.now(),
                    "functional_stage_id": response.get("dataset_id"),
                    "current_stage": "DATASET_CREATED",
                }
                self.CRUDProjectFlow.update(**project_flow_crud_request)
                return {
                    "dataset_name": create_dataset_request.get("display_name"),
                    "dataset_id": response.get("dataset_id"),
                }
            else:
                raise Exception({"status": "create dataset failed"})
        except Exception as error:
            logging.error(
                f"Error in create_object_detection_dataset_controller function: {error}"
            )
            raise error
