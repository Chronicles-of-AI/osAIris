import logging
from google.cloud.storage import bucket
from commons.external_call import APIInterface
from sql import config, logger
from sql.utils.gcs_helper import upload_blob_string

logging = logger(__name__)


class GetPredictionController:
    def __init__(self):
        self.gcp_config = config.get("core_engine").get("gcp")

    def text_model_predictions_controller(self, request):
        """[Controller function to get text classification prediction]

        Args:
            request ([dict]): [text classification prediction request]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [dict]: [Predicted response]
        """
        try:
            logging.info("executing text_model_predictions_controller function")
            get_predictions_url = (
                self.gcp_config.get("automl").get("text").get("get_predictions")
            )
            get_predictions_request = request.dict(exclude_none=True)
            response, status_code = APIInterface.post(
                route=get_predictions_url,
                data=get_predictions_request,
            )
            return response
        except Exception as error:
            logging.error(
                f"Error in text_model_prediction_controller function: {error}"
            )
            raise error

    def image_model_predictions_controller(
        self,
        project_id: str,
        model_id: str,
        region: str,
        bucket_name: str,
        gcs_file_name: str,
        file_bytes,
    ):
        """[Controller function to get image classification prediction]

        Args:
            project_id (str): [project id for image classification model]
            model_id (str): [model id for image classification model]
            region (str): [region the model is deployed in]
            bucket_name (str): [bucket where prediction image is saved]
            gcs_file_name (str): [file name saved on GCS bucket]
            file_bytes ([bytes]): [file data in byte format]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [dict]: [predicted response]
        """
        try:
            logging.info("executing image_model_predictions_controller function")
            gcs_uri = upload_blob_string(
                bucket_name=bucket_name,
                file=file_bytes,
                destination_file_name=gcs_file_name,
                content_type="image/jpeg",
            )
            get_predictions_url = (
                self.gcp_config.get("automl").get("image").get("get_image_predictions")
            )
            get_predictions_request = {
                "project_id": project_id,
                "model_id": model_id,
                "region": region,
                "gcs_uri": gcs_uri,
            }
            response, status_code = APIInterface.post(
                route=get_predictions_url,
                data=get_predictions_request,
            )
            return response
        except Exception as error:
            logging.error(
                f"Error in image_model_predictions_controller function: {error}"
            )
            raise error
