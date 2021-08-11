from fastapi import APIRouter, UploadFile, File
from sql.apis.schemas.requests.gcp.get_predictions_request import GetPredictions
from sql.controllers.gcp.get_predictions_controller import GetPredictionController

get_predictions_router = APIRouter()


@get_predictions_router.post("/gcp/automl/get_text_predictions")
def get_text_predictions(
    get_text_predictions_request: GetPredictions,
):
    """[summary]

    Args:
        get_text_predictions_request (GetPredictions): [description]

    Raises:
        error: [description]

    Returns:
        [type]: [description]
    """
    try:
        return GetPredictionController().text_model_predictions_controller(
            request=get_text_predictions_request
        )
    except Exception as error:
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
    """[summary]

    Args:
        project_id (str): [description]
        model_id (str): [description]
        region (str): [description]
        bucket_name (str): [description]
        gcs_file_name (str): [description]
        file (UploadFile, optional): [description]. Defaults to File(...).

    Raises:
        error: [description]

    Returns:
        [type]: [description]
    """
    try:
        return GetPredictionController().image_model_predictions_controller(
            project_id=project_id,
            model_id=model_id,
            region=region,
            bucket_name=bucket_name,
            gcs_file_name=gcs_file_name,
            file_bytes=await file.read(),
        )
    except Exception as error:
        raise error
