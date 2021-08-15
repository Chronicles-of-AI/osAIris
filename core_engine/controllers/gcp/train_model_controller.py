from utils.gcp.automl_train import (
    train_text_classification_model,
    train_ner_model,
    train_image_classification_model,
    train_image_classification_edge_model,
    train_object_detection_model,
    train_object_detection_edge_model,
)
from core_engine import logger

logging = logger(__name__)


class TrainModelController:
    def __init__(self):
        pass

    def train_text_classification_model_controller(self, request):
        """[Create a Text Classification Model in AutoML on GCP]

        Args:
            request ([type]): [Based on the Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [description]
        """
        try:
            logging.info(f"Train Text Classification Model Controller: {request}")
            return train_text_classification_model(
                project_id=request.project_id,
                dataset_id=request.dataset_id,
                model_display_name=request.model_display_name,
                region=request.region,
            )
        except Exception as error:
            logging.error(f"{error=}")
            raise error

    def train_ner_model_controller(self, request):
        """[Create a NER Model in AutoML on GCP]

        Args:
            request ([type]): [Based on the Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [description]
        """
        try:
            logging.info(f"Train NER Model Controller: {request}")
            return train_ner_model(
                project_id=request.project_id,
                dataset_id=request.dataset_id,
                model_display_name=request.model_display_name,
                region=request.region,
            )
        except Exception as error:
            logging.error(f"{error=}")
            raise error

    def train_image_classification_model_controller(self, request):
        """[Create a Image Classification Model in AutoML on GCP]

        Args:
            request ([type]): [Based on the Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [description]
        """
        try:
            logging.info(f"Train Image Classification Model Controller: {request}")
            return train_image_classification_model(
                project_id=request.project_id,
                dataset_id=request.dataset_id,
                model_display_name=request.model_display_name,
                region=request.region,
            )
        except Exception as error:
            logging.error(f"{error=}")
            raise error

    def train_image_classification_edge_model_controller(self, request):
        """[Create a Image Classification Model for Edge in AutoML on GCP]

        Args:
            request ([type]): [Based on the Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [description]
        """
        try:
            logging.info(
                f"Train Image Classification Model for Edge Controller: {request}"
            )
            return train_image_classification_edge_model(
                project_id=request.project_id,
                dataset_id=request.dataset_id,
                model_display_name=request.model_display_name,
                region=request.region,
                model_type=request.model_type,
            )
        except Exception as error:
            logging.error(f"{error=}")
            raise error

    def train_object_detection_model_controller(self, request):
        """[Create a Object Detection Model in AutoML on GCP]

        Args:
            request ([type]): [Based on the Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [description]
        """
        try:
            logging.info(f"Train Object Detection Model Controller: {request}")
            return train_object_detection_model(
                project_id=request.project_id,
                dataset_id=request.dataset_id,
                model_display_name=request.model_display_name,
                region=request.region,
            )
        except Exception as error:
            logging.error(f"{error=}")
            raise error

    def train_object_detection_edge_model_controller(self, request):
        """[Create a Object Detection Model for Edge in AutoML on GCP]

        Args:
            request ([type]): [Based on the Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [description]
        """
        try:
            logging.info(f"Train Object Detection Model for Edge Controller: {request}")
            return train_object_detection_edge_model(
                project_id=request.project_id,
                dataset_id=request.dataset_id,
                model_display_name=request.model_display_name,
                region=request.region,
                model_type=request.model_type,
            )
        except Exception as error:
            logging.error(f"{error=}")
            raise error
