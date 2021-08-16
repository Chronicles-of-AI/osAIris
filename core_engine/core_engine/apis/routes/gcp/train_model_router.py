from fastapi import APIRouter
from core_engine.apis.schemas.requests.gcp.train_model_request import (
    TrainTextModel,
    TrainImageModel,
    TrainImageEdgeModel,
)
from core_engine.controllers.gcp.train_model_controller import TrainModelController
from core_engine import logger

logging = logger(__name__)

train_model_router = APIRouter()


@train_model_router.post("/gcp/automl/train_text_classification_model")
def create_text_classification_training(
    train_text_classification_model_request: TrainTextModel,
):
    """[Train a Text Classification Model in AutoML GCP]

    Args:
        train_text_classification_model_request (TrainTextModel): [Based on Input Schema]

    Raises:
        error: [Error]

    Returns:
        [type]: [description]
    """
    try:
        logging.info(
            f"Create Text Classification Model Router: {train_text_classification_model_request}"
        )
        return TrainModelController().train_text_classification_model_controller(
            request=train_text_classification_model_request
        )
    except Exception as error:
        logging.error(f"{error=}")
        raise error


@train_model_router.post("/gcp/automl/train_ner_model")
def create_ner_training(
    train_ner_model_request: TrainTextModel,
):
    """[Train a NER Model in AutoML GCP]

    Args:
        train_ner_model_request (TrainTextModel): [Based on Input Schema]

    Raises:
        error: [Error]

    Returns:
        [type]: [description]
    """
    try:
        logging.info(f"Create NER Model Router: {train_ner_model_request}")
        return TrainModelController().train_ner_model_controller(
            request=train_ner_model_request
        )
    except Exception as error:
        logging.error(f"{error=}")
        raise error


@train_model_router.post("/gcp/automl/train_image_classification_model")
def create_image_classification_training(
    train_image_classification_model_request: TrainImageModel,
):
    """[Train a Image Classification Model in AutoML GCP]

    Args:
        train_image_classification_model_request (TrainImageModel): [Based on Input Schema]

    Raises:
        error: [Error]

    Returns:
        [type]: [description]
    """
    try:
        logging.info(
            f"Create Image Classification Model Router: {train_image_classification_model_request}"
        )
        return TrainModelController().train_image_classification_model_controller(
            request=train_image_classification_model_request
        )
    except Exception as error:
        logging.error(f"{error=}")
        raise error


@train_model_router.post("/gcp/automl/train_image_classification_edge_model")
def create_image_classification_edge_training(
    train_image_classification_edge_model_request: TrainImageEdgeModel,
):
    """[Train a Image Classification Model for Edge in AutoML GCP]

    Args:
        train_image_classification_edge_model_request (TrainImageEdgeModel): [Based on Input Schema]

    Raises:
        error: [Error]

    Returns:
        [type]: [description]
    """
    try:
        logging.info(
            f"Create Text Classification Model for Edge Router: {train_image_classification_edge_model_request}"
        )
        return TrainModelController().train_image_classification_edge_model_controller(
            request=train_image_classification_edge_model_request
        )
    except Exception as error:
        logging.error(f"{error=}")
        raise error


@train_model_router.post("/gcp/automl/train_object_detection_model")
def create_object_detection_training(
    train_object_detection_model_request: TrainImageModel,
):
    """[Train a Object Detection Model in AutoML GCP]

    Args:
        train_object_detection_model_request (TrainImageModel): [Based on Input Schema]

    Raises:
        error: [Error]

    Returns:
        [type]: [description]
    """
    try:
        logging.info(
            f"Create Object Detection Model Router: {train_object_detection_model_request}"
        )
        return TrainModelController().train_object_detection_model_controller(
            request=train_object_detection_model_request
        )
    except Exception as error:
        logging.error(f"{error=}")
        raise error


@train_model_router.post("/gcp/automl/train_object_detection_edge_model")
def create_object_detection_edge_training(
    train_object_detection_edge_model_request: TrainImageEdgeModel,
):
    """[Train a Object Detection Model for Edge in AutoML GCP]

    Args:
        train_object_detection_edge_model_request (TrainImageEdgeModel): [Based on Input Schema]

    Raises:
        error: [Error]

    Returns:
        [type]: [description]
    """
    try:
        logging.info(
            f"Create Object Detection Model Router: {train_object_detection_edge_model_request}"
        )
        return TrainModelController().train_object_detection_edge_model_controller(
            request=train_object_detection_edge_model_request
        )
    except Exception as error:
        logging.error(f"{error=}")
        raise error
