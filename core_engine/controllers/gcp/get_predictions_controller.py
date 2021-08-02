from utils.gcp.automl_predict import text_model_prediction, image_model_prediction


class GetPredictionController:
    def __init__(self):
        pass

    def text_model_predictions_controller(self, request):
        return text_model_prediction(
            project_id=request.project_id,
            model_id=request.model_id,
            content=request.content,
            region=request.region,
        )

    def image_model_predictions_controller(
        self,
        request,
    ):
        return image_model_prediction(
            project_id=request.project_id,
            model_id=request.model_id,
            gcs_uri=request.gcs_uri,
            region=request.region,
        )
