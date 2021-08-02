from fastapi import APIRouter
from apis.schemas.requests.gcp.train_model_request import (
    TrainTextModel,
    TrainImageModel,
    TrainImageEdgeModel,
)
from controllers.gcp.train_model_controller import TrainModelController

train_model_router = APIRouter()


@train_model_router.post("/gcp/automl/train_text_classification_model")
def create_text_classification_training(
    train_text_classification_model_request: TrainTextModel,
):
    return TrainModelController().train_text_classification_model_controller(
        request=train_text_classification_model_request
    )


@train_model_router.post("/gcp/automl/train_ner_model")
def create_ner_training(
    train_ner_model_request: TrainTextModel,
):
    return TrainModelController().train_ner_model_controller(
        request=train_ner_model_request
    )


@train_model_router.post("/gcp/automl/train_image_classification_model")
def create_image_classification_training(
    train_image_classification_model_request: TrainImageModel,
):
    return TrainModelController().train_image_classification_model_controller(
        request=train_image_classification_model_request
    )


@train_model_router.post("/gcp/automl/train_image_classification_edge_model")
def create_image_classification_edge_training(
    train_image_classification_edge_model_request: TrainImageEdgeModel,
):
    return TrainModelController().train_image_classification_edge_model_controller(
        request=train_image_classification_edge_model_request
    )


@train_model_router.post("/gcp/automl/train_object_detection_model")
def create_object_detection_training(
    train_object_detection_model_request: TrainImageModel,
):
    return TrainModelController().train_object_detection_model_controller(
        request=train_object_detection_model_request
    )


@train_model_router.post("/gcp/automl/train_object_detection_edge_model")
def create_object_detection_edge_training(
    train_object_detection_edge_model_request: TrainImageEdgeModel,
):
    return TrainModelController().train_object_detection_edge_model_controller(
        request=train_object_detection_edge_model_request
    )
