from typing import List
from fastapi import File, UploadFile, APIRouter
from apis.schemas.requests.gcp.get_predictions_request import (
    GetPredictions,
    GetImagePredictions,
)
from controllers.gcp.get_predictions_controller import GetPredictionController

get_predictions_router = APIRouter()


@get_predictions_router.post("/gcp/automl/get_text_predictions")
def get_text_predictions(
    get_text_predictions_request: GetPredictions,
):
    return GetPredictionController().text_model_predictions_controller(
        request=get_text_predictions_request
    )


@get_predictions_router.post("/gcp/automl/get_image_predictions")
def get_image_predictions(get_image_predictions_request: GetImagePredictions):
    return GetPredictionController().image_model_predictions_controller(
        request=get_image_predictions_request
    )
