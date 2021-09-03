import logging
from commons.external_call import APIInterface
from sql import config, logger
from sql.crud.model_crud import CRUDModel
from sql.crud.operation_crud import CRUDOperations
from sql.crud.project_flow_crud import CRUDProjectFlow
from sql.controllers.gcp.model_management_controller import ManageModelController
from datetime import datetime

logging = logger(__name__)


class TrainModelController:
    def __init__(self):
        self.CRUDModel = CRUDModel()
        self.CRUDOperations = CRUDOperations()
        self.CRUDProjectFlow = CRUDProjectFlow()
        self.ManageModelController = ManageModelController()
        self.gcp_config = config.get("core_engine").get("gcp")

    def create_operation_record(self, api_response: dict):
        """[Controller function to create operation record]

        Args:
            api_response (dict): [API response from operations]

        Raises:
            error: [Error raised from controller layer]
        """
        try:
            logging.info("executing create_operation_record function")
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
            logging.error(f"Error in create_operation_record function: {error}")
            raise error

    def train_text_classification_model_controller(self, request):
        """[Controller function to train text classification model]

        Args:
            request ([dict]): [text classification training request]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [dict]: [text classification training operation details]
        """
        try:
            logging.info(
                "executing train_text_classification_model_controller function"
            )
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
                project_flow_crud_request = {
                    "pipeline_id": train_classification_model_request.get(
                        "pipeline_id"
                    ),
                    "updated_at": datetime.now(),
                    "functional_stage_id": response.get("operation_id"),
                    "current_stage": "TRAINING",
                }
                self.CRUDProjectFlow.update(**project_flow_crud_request)
                return {
                    "operation_id": response.get("operation_id"),
                    "status": "Training Started",
                }
            else:
                raise Exception({"status": "Training failed"})
        except Exception as error:
            logging.error(
                f"Error in train_text_classification_model_controller function: {error}"
            )
            raise error

    def train_ner_model_controller(self, request):
        """[Controller function to train NER model]

        Args:
            request ([dict]): [NER training request]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [dict]: [NER training operation details]
        """
        try:
            logging.info("executing train_ner_model_controller function")
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
                project_flow_crud_request = {
                    "pipeline_id": train_ner_model_request.get("pipeline_id"),
                    "updated_at": datetime.now(),
                    "functional_stage_id": response.get("operation_id"),
                    "current_stage": "TRAINING",
                }
                self.CRUDProjectFlow.update(**project_flow_crud_request)
                return {
                    "operation_id": response.get("operation_id"),
                    "status": "Training Started",
                }
            else:
                raise Exception({"status": "Training failed"})
        except Exception as error:
            logging.error(f"Error in train_ner_model_controller function: {error}")
            raise error

    def train_image_classification_model_controller(self, request):
        """[Controller function to train image classification model]

        Args:
            request ([dict]): [image classification training request]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [dict]: [image classification training operation details]
        """
        try:
            logging.info(
                "executing train_image_classification_model_controller function"
            )
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
                project_flow_crud_request = {
                    "pipeline_id": train_image_classification_model_request.get(
                        "pipeline_id"
                    ),
                    "updated_at": datetime.now(),
                    "functional_stage_id": response.get("operation_id"),
                    "current_stage": "TRAINING",
                }
                self.CRUDProjectFlow.update(**project_flow_crud_request)
                return {
                    "operation_id": response.get("operation_id"),
                    "status": "Training Started",
                }
            else:
                raise Exception({"status": "Training failed"})
        except Exception as error:
            logging.error(
                f"Error in train_image_classification_model_controller function: {error}"
            )
            raise error

    def train_image_classification_edge_model_controller(self, request):
        """[Controller function to train image classification model for edge device]

        Args:
            request ([dict]): [image classification training request]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [dict]: [image classification training operation details for edge device]
        """
        try:
            logging.info(
                "executing train_image_classification_edge_model_controller function"
            )
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
                project_flow_crud_request = {
                    "pipeline_id": train_edge_image_classification_model_request.get(
                        "pipeline_id"
                    ),
                    "updated_at": datetime.now(),
                    "functional_stage_id": response.get("operation_id"),
                    "current_stage": "TRAINING",
                }
                self.CRUDProjectFlow.update(**project_flow_crud_request)
                return {
                    "operation_id": response.get("operation_id"),
                    "status": "Training Started",
                }
            else:
                raise Exception({"status": "Training failed"})
        except Exception as error:
            logging.error(
                f"Error in train_image_classification_edge_model_controller function: {error}"
            )
            raise error

    def train_object_detection_model_controller(self, request):
        """[Controller function to train object detection model]

        Args:
            request ([dict]): [object detection training request]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [dict]: [object detection training operation details]
        """
        try:
            logging.info("executing train_object_detection_model_controller function")
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
                project_flow_crud_request = {
                    "pipeline_id": train_object_detection_model_request.get(
                        "pipeline_id"
                    ),
                    "updated_at": datetime.now(),
                    "functional_stage_id": response.get("operation_id"),
                    "current_stage": "TRAINING",
                }
                self.CRUDProjectFlow.update(**project_flow_crud_request)
                return {
                    "operation_id": response.get("operation_id"),
                    "status": "Training Started",
                }
            else:
                raise Exception({"status": "Training failed"})
        except Exception as error:
            logging.error(
                f"Error in train_object_detection_model_controller function: {error}"
            )
            raise error

    def train_object_detection_edge_model_controller(self, request):
        """[Controller function to train object detection model for edge device]

        Args:
            request ([dict]): [object detection training request]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [dict]: [object detection training operation details for edge device]
        """
        try:
            logging.info(
                "executing train_object_detection_edge_model_controller function"
            )
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
                project_flow_crud_request = {
                    "pipeline_id": train_object_detection_edge_model_request.get(
                        "pipeline_id"
                    ),
                    "updated_at": datetime.now(),
                    "functional_stage_id": response.get("operation_id"),
                    "current_stage": "TRAINING",
                }
                self.CRUDProjectFlow.update(**project_flow_crud_request)
                return {
                    "operation_id": response.get("operation_id"),
                    "status": "Training Started",
                }
            else:
                raise Exception({"status": "Training failed"})
        except Exception as error:
            logging.error(
                f"Error in train_object_detection_edge_model_controller function: {error}"
            )
            raise error
