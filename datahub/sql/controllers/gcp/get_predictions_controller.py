from google.cloud.storage import bucket
from commons.external_call import APIInterface
from sql import config
from sql.utils.gcs_helper import upload_blob_string


class GetPredictionController:
    def __init__(self):
        self.gcp_config = config.get("core_engine").get("gcp")

    def text_model_predictions_controller(self, request):
        """[summary]

        Args:
            request ([type]): [description]

        Raises:
            error: [description]

        Returns:
            [type]: [description]
        """
        try:
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
        """[summary]

        Args:
            project_id (str): [description]
            model_id (str): [description]
            region (str): [description]
            bucket_name (str): [description]
            gcs_file_name (str): [description]
            file_bytes ([type]): [description]

        Raises:
            error: [description]

        Returns:
            [type]: [description]
        """
        try:
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
            raise error
