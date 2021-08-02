from fastapi import APIRouter, UploadFile, File
from sql.apis.schemas.requests.gcp.get_predictions_request import GetPredictions
from sql.controllers.gcp.get_predictions_controller import GetPredictionController

get_predictions_router = APIRouter()


@get_predictions_router.post("/gcp/automl/get_text_predictions")
def get_text_predictions(
    get_text_predictions_request: GetPredictions,
):
    return GetPredictionController().text_model_predictions_controller(
        request=get_text_predictions_request
    )


@get_predictions_router.post("/gcp/automl/get_image_predictions")
async def get_image_predictions(
    project_id: str,
    model_id: str,
    region: str,
    bucket_name: str,
    gcs_file_name: str,
    file: UploadFile = File(...),
):
    return GetPredictionController().image_model_predictions_controller(
        project_id=project_id,
        model_id=model_id,
        region=region,
        bucket_name=bucket_name,
        gcs_file_name=gcs_file_name,
        file_bytes=await file.read(),
    )
