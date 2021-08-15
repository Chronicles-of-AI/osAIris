from utils.gcp.automl_predict import text_model_prediction, image_model_prediction
from core_engine import logger

logging = logger(__name__)


class GetPredictionController:
    def __init__(self):
        pass

    def text_model_predictions_controller(self, request):
        """[Get Predictions from an AutoML Model]

        Args:
            request ([type]): [Based on the Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [description]
        """
        try:
            logging.info(f"Text Model Prediction Controller: {request}")
            return text_model_prediction(
                project_id=request.project_id,
                model_id=request.model_id,
                content=request.content,
                region=request.region,
            )
        except Exception as error:
            logging.error(f"{error=}")
            raise error

    def image_model_predictions_controller(
        self,
        request,
    ):
        """[Get Predictions from an AutoML Model]

        Args:
            request ([type]): [Based on the Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [description]
        """
        try:
            logging.info(f"Text Model Prediction Controller: {request}")
            return image_model_prediction(
                project_id=request.project_id,
                model_id=request.model_id,
                gcs_uri=request.gcs_uri,
                region=request.region,
            )
        except Exception as error:
            logging.error(f"{error=}")
            raise error
