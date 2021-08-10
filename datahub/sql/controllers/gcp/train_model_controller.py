from commons.external_call import APIInterface
from sql import config
from sql.crud.model_crud import CRUDModel
from sql.crud.operation_crud import CRUDOperations
from sql.controllers.gcp.model_management_controller import ManageModelController
from datetime import datetime


class TrainModelController:
    def __init__(self):
        self.CRUDModel = CRUDModel()
        self.CRUDOperations = CRUDOperations()
        self.ManageModelController = ManageModelController()
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
                "functional_stage": "TRAIN_MODEL",
                "service_id": api_response.get("dataset_id"),
                "created": datetime.now(),
            }
            self.CRUDOperations.create(**operation_crud_request)
        except Exception as error:
            raise error

    def train_text_classification_model_controller(self, request):
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
            train_classification_model_url = (
                self.gcp_config.get("automl")
                .get("text")
                .get("train_classification_model")
            )
            train_classification_model_request = request.dict(exclude_none=True)
            response, status_code = APIInterface.post(
                route=train_classification_model_url,
                data=train_classification_model_request,
            )
            if status_code == 200:
                crud_request = {
                    "model_id": response.get("operation_id"),
                    "dataset_id": request.dataset_id,
                    "alias_name": request.model_display_name,
                    "UUID": uuid,
                    "status": "Training Started",
                    "created": datetime.now(),
                }
                self.CRUDModel.create(**crud_request)
                self.create_operation_record(api_response=response)
                return {
                    "operation_id": response.get("operation_id"),
                    "status": "Training Started",
                }
            else:
                # TODO: error
                pass
                return {"status": "Training failed"}
        except Exception as error:
            raise error

    def train_ner_model_controller(self, request):
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
            train_ner_model_url = (
                self.gcp_config.get("automl").get("text").get("train_ner_model")
            )
            train_ner_model_request = request.dict(exclude_none=True)
            response, status_code = APIInterface.post(
                route=train_ner_model_url,
                data=train_ner_model_request,
            )
            if status_code == 200:
                crud_request = {
                    "model_id": response.get("operation_id"),
                    "dataset_id": request.dataset_id,
                    "alias_name": request.model_display_name,
                    "UUID": uuid,
                    "status": "Training Started",
                    "created": datetime.now(),
                }
                self.CRUDModel.create(**crud_request)
                self.create_operation_record(api_response=response)
                return {
                    "operation_id": response.get("operation_id"),
                    "status": "Training Started",
                }
            else:
                # TODO: error
                pass
                return {"status": "Training failed"}
        except Exception as error:
            raise error

    def train_image_classification_model_controller(self, request):
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
            train_image_classification_model_url = (
                self.gcp_config.get("automl")
                .get("image")
                .get("train_image_classification_model")
            )
            train_image_classification_model_request = request.dict(exclude_none=True)
            response, status_code = APIInterface.post(
                route=train_image_classification_model_url,
                data=train_image_classification_model_request,
            )
            if status_code == 200:
                crud_request = {
                    "model_id": response.get("operation_id"),
                    "dataset_id": request.dataset_id,
                    "alias_name": request.model_display_name,
                    "UUID": uuid,
                    "status": "Training Started",
                    "created": datetime.now(),
                }
                self.CRUDModel.create(**crud_request)
                self.create_operation_record(api_response=response)
                return {
                    "operation_id": response.get("operation_id"),
                    "status": "Training Started",
                }
            else:
                # TODO: error
                pass
                return {"status": "Training failed"}
        except Exception as error:
            raise error

    def train_image_classification_edge_model_controller(self, request):
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
            train_edge_image_classification_model_url = (
                self.gcp_config.get("automl")
                .get("image")
                .get("train_image_classification_edge_model")
            )
            train_edge_image_classification_model_request = request.dict(
                exclude_none=True
            )
            response, status_code = APIInterface.post(
                route=train_edge_image_classification_model_url,
                data=train_edge_image_classification_model_request,
            )
            if status_code == 200:
                crud_request = {
                    "model_id": response.get("operation_id"),
                    "dataset_id": request.dataset_id,
                    "alias_name": request.model_display_name,
                    "UUID": uuid,
                    "status": "Training Started",
                    "created": datetime.now(),
                }
                self.CRUDModel.create(**crud_request)
                self.create_operation_record(api_response=response)
                return {
                    "operation_id": response.get("operation_id"),
                    "status": "Training Started",
                }
            else:
                # TODO: error
                pass
                return {"status": "Training failed"}
        except Exception as error:
            raise error

    def train_object_detection_model_controller(self, request):
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
            train_object_detection_model_url = (
                self.gcp_config.get("automl")
                .get("image")
                .get("train_object_detection_model")
            )
            train_object_detection_model_request = request.dict(exclude_none=True)
            response, status_code = APIInterface.post(
                route=train_object_detection_model_url,
                data=train_object_detection_model_request,
            )
            if status_code == 200:
                crud_request = {
                    "model_id": response.get("operation_id"),
                    "dataset_id": request.dataset_id,
                    "alias_name": request.model_display_name,
                    "UUID": uuid,
                    "status": "Training Started",
                    "created": datetime.now(),
                }
                self.CRUDModel.create(**crud_request)
                self.create_operation_record(api_response=response)
                return {
                    "operation_id": response.get("operation_id"),
                    "status": "Training Started",
                }
            else:
                # TODO: error
                pass
                return {"status": "Training failed"}
        except Exception as error:
            raise error

    def train_object_detection_edge_model_controller(self, request):
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
            train_object_detection_edge_model_url = (
                self.gcp_config.get("automl")
                .get("image")
                .get("train_object_detection_edge_model")
            )
            train_object_detection_edge_model_request = request.dict(exclude_none=True)
            response, status_code = APIInterface.post(
                route=train_object_detection_edge_model_url,
                data=train_object_detection_edge_model_request,
            )
            if status_code == 200:
                crud_request = {
                    "model_id": response.get("operation_id"),
                    "dataset_id": request.dataset_id,
                    "alias_name": request.model_display_name,
                    "UUID": uuid,
                    "status": "Training Started",
                    "created": datetime.now(),
                }
                self.CRUDModel.create(**crud_request)
                self.create_operation_record(api_response=response)
                return {
                    "operation_id": response.get("operation_id"),
                    "status": "Training Started",
                }
            else:
                # TODO: error
                pass
                return {"status": "Training failed"}
        except Exception as error:
            raise error
