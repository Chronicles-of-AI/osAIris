from fastapi import APIRouter, UploadFile, File
from sql.apis.schemas.requests.gcp.get_predictions_request import GetPredictions
from sql.controllers.gcp.get_predictions_controller import GetPredictionController
from sql import logger

logging = logger(__name__)
get_predictions_router = APIRouter()


@get_predictions_router.post("/gcp/automl/get_text_predictions")
def get_text_predictions(
    get_text_predictions_request: GetPredictions,
):
    """[API router to get text classification predictions]

    Args:
        get_text_predictions_request (GetPredictions): [Get text classification predictions from AutoML model]

    Raises:
        error: [Exception in underlying controller]

    Returns:
        [dict]: [text classification inference results]
    """
    try:
        logging.info("Calling /gcp/automl/get_text_predictions endpoint")
        logging.debug(f"Request: {get_text_predictions_request}")
        return GetPredictionController().text_model_predictions_controller(
            request=get_text_predictions_request
        )
    except Exception as error:
        logging.error(f"Error in /gcp/automl/get_text_predictions endpoint: {error}")
        raise error


@get_predictions_router.post("/gcp/automl/get_image_predictions")
async def get_image_predictions(
    project_id: str,
    model_id: str,
    region: str,
    bucket_name: str,
    gcs_file_name: str,
    file: UploadFile = File(...),
):
    """[API router to perform image classification inference on AutoML deployed model]

    Args:
        project_id (str): [AutoML project id]
        model_id (str): [AutoML image classification model id]
        region (str): [Region of deployment for AutoML model]
        bucket_name (str): [GCS bucket where inference image is stored]
        gcs_file_name (str): [GCS file name to be inferenced]
        file (UploadFile, optional): [file to be inferenced]. Defaults to File(...).

    Raises:
        error: [Exception in underlying controller]

    Returns:
        [dict]: [image classification infence results]
    """
    try:
        logging.info("Calling /gcp/automl/get_image_predictions endpoint")
        logging.debug(
            f"Request: {project_id=},{model_id=},{region=},{bucket_name=},{gcs_file_name=},{file=}"
        )
        return GetPredictionController().image_model_predictions_controller(
            project_id=project_id,
            model_id=model_id,
            region=region,
            bucket_name=bucket_name,
            gcs_file_name=gcs_file_name,
            file_bytes=await file.read(),
        )
    except Exception as error:
        logging.error(f"Error in /gcp/automl/get_image_predictions endpoint: {error}")
        raise error
