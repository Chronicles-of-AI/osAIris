from utils.gcp.automl_create_dataset import (
    create_text_classification_dataset,
    create_ner_dataset,
    create_image_classification_dataset,
    create_object_detection_dataset,
)
from core_engine import logger

logging = logger(__name__)


class CreateDatasetController:
    def __init__(self):
        pass

    def create_text_classification_dataset_controller(self, request):
        """[Create a Text Classification Dataset in AutoML on GCP]

        Args:
            request ([type]): [Based on the Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [description]
        """
        try:
            logging.info(f"Create Text Classification Dataset Controller: {request}")
            return create_text_classification_dataset(
                project_id=request.project_id,
                display_name=request.display_name,
                region=request.region,
                multi_label=request.multi_label,
            )
        except Exception as error:
            logging.error(f"{error=}")
            raise error

    def create_ner_dataset_controller(self, request):
        """[Create a NER Dataset in AutoML on GCP]

        Args:
            request ([type]): [Based on the Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [description]
        """
        try:
            logging.info(f"Create NER Dataset Controller: {request}")
            return create_ner_dataset(
                project_id=request.project_id,
                display_name=request.display_name,
            )
        except Exception as error:
            logging.error(f"{error=}")
            raise error

    def create_image_classification_dataset_controller(self, request):
        """[Create a Image Classification Dataset in AutoML on GCP]

        Args:
            request ([type]): [Based on the Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [description]
        """
        try:
            logging.info(f"Create Image Classification Dataset Controller: {request}")
            return create_image_classification_dataset(
                project_id=request.project_id,
                display_name=request.display_name,
                region=request.region,
                multi_label=request.multi_label,
            )
        except Exception as error:
            logging.error(f"{error=}")
            raise error

    def create_object_detection_dataset_controller(self, request):
        """[Create a Object Detection Dataset in AutoML on GCP]

        Args:
            request ([type]): [Based on the Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [description]
        """
        try:
            logging.info(f"Create Object Detection Dataset Controller: {request}")
            return create_object_detection_dataset(
                project_id=request.project_id,
                display_name=request.display_name,
                region=request.region,
            )
        except Exception as error:
            logging.error(f"{error=}")
            raise error
