from typing import List
from fastapi import File, UploadFile, APIRouter
from core_engine.apis.schemas.requests.gcp.get_predictions_request import (
    GetPredictions,
    GetImagePredictions,
)
from core_engine.controllers.gcp.get_predictions_controller import (
    GetPredictionController,
)
from core_engine import logger

logging = logger(__name__)

get_predictions_router = APIRouter()


@get_predictions_router.post("/gcp/automl/get_text_predictions")
def get_text_predictions(
    get_text_predictions_request: GetPredictions,
):
    """[Get Text Predictions from AutoML Model]

    Args:
        get_text_predictions_request (GetPredictions): [Based on Input Schema]

    Raises:
        error: [Error]

    Returns:
        [type]: [description]
    """
    try:
        logging.info(f"Get Text Predictions Router: {get_text_predictions_request}")
        return GetPredictionController().text_model_predictions_controller(
            request=get_text_predictions_request
        )
    except Exception as error:
        logging.error(f"{error=}")
        raise error


@get_predictions_router.post("/gcp/automl/get_image_predictions")
def get_image_predictions(get_image_predictions_request: GetImagePredictions):
    """[Get Image Predictions from AutoML Model]

    Args:
        get_image_predictions_request (GetImagePredictions): [Based on Input Schema]

    Raises:
        error: [Error]

    Returns:
        [type]: [description]
    """
    try:
        logging.info(f"Get Image Predictions Router: {get_image_predictions_request}")
        return GetPredictionController().image_model_predictions_controller(
            request=get_image_predictions_request
        )
    except Exception as error:
        logging.error(f"{error=}")
        raise error
