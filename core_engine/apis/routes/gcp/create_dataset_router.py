from fastapi import APIRouter, Query
from typing import List, Optional
from apis.schemas.requests.gcp.create_dataset_request import (
    CreateTextClassificationDataset,
    CreateNERDataset,
    CreateImageClassificationDataset,
    CreateObjectDetectionDataset,
)
from controllers.gcp.create_dataset_controller import CreateDatasetController
from core_engine import logger

logging = logger(__name__)

create_dataset_router = APIRouter()


@create_dataset_router.post("/gcp/automl/create_text_classification_dataset")
def create_text_classification_dataset(
    create_text_classification_dataset_request: CreateTextClassificationDataset,
):
    """[Create a Text Classification Dataset Router]

    Args:
        create_text_classification_dataset_request (CreateTextClassificationDataset): [[Based on Input Schema]]

    Raises:
        error: [Error]

    Returns:
        [type]: [description]
    """
    try:
        logging.info(
            f"Create Text Classification Dataset Router: {create_text_classification_dataset_request}"
        )
        return CreateDatasetController().create_text_classification_dataset_controller(
            create_text_classification_dataset_request
        )
    except Exception as error:
        logging.error(f"{error=}")
        raise error


@create_dataset_router.post("/gcp/automl/create_ner_dataset")
def create_ner_dataset(
    create_ner_request: CreateNERDataset,
):
    """[Create a NER Dataset Router]

    Args:
        create_ner_request (CreateNERDataset): [[Based on Input Schema]]

    Raises:
        error: [Error]

    Returns:
        [type]: [description]
    """
    try:
        logging.info(f"Create NER Dataset Router: {create_ner_request}")
        return CreateDatasetController().create_ner_dataset_controller(
            create_ner_request
        )
    except Exception as error:
        logging.error(f"{error=}")
        raise error


@create_dataset_router.post("/gcp/automl/create_image_classification_dataset")
def create_image_classification_dataset(
    create_image_classification_dataset_request: CreateImageClassificationDataset,
):
    """[Create a Image Classification Dataset Router]

    Args:
        create_image_classification_dataset_request (CreateImageClassificationDataset): [[Based on Input Schema]]

    Raises:
        error: [Error]

    Returns:
        [type]: [description]
    """
    try:
        logging.info(
            f"Create Image Classification Dataset Router: {create_image_classification_dataset_request}"
        )
        return CreateDatasetController().create_image_classification_dataset_controller(
            create_image_classification_dataset_request
        )
    except Exception as error:
        logging.error(f"{error=}")
        raise error


@create_dataset_router.post("/gcp/automl/create_object_detection_dataset")
def create_object_detection_dataset(
    create_object_detection_dataset_request: CreateObjectDetectionDataset,
):
    """[Create a Object Dataset Router]

    Args:
        create_object_detection_dataset_request (CreateObjectDetectionDataset): [[Based on Input Schema]]

    Raises:
        error: [Error]

    Returns:
        [type]: [description]
    """
    try:
        logging.info(
            f"Create Object Detection Dataset Router: {create_object_detection_dataset_request}"
        )
        return CreateDatasetController().create_object_detection_dataset_controller(
            create_object_detection_dataset_request
        )
    except Exception as error:
        logging.error(f"{error=}")
        raise error
