import os
import json
from datetime import datetime
from commons.external_call import APIInterface
from sql import config
from sql.utils.s3_helper import write_annotations_to_s3
from sql.utils.gcs_helper import upload_blob_string
from sql import logger

logging = logger(__name__)


class ProjectController:
    def __init__(self):
        self.label_studio_config = config.get("label_studio").get("endpoint")
        self.label_studio_token = config.get("label_studio").get("token")
        self.core_label_studio_config = config.get("core_engine").get(
            "label_studio_router"
        )
        self.header = {"Authorization": f"Token {self.label_studio_token}"}

    def create_project_controller(self, request):
        try:
            logging.info(
                f"Creating a annotation project on Label Studio with request: {request}"
            )
            create_project_request = request.dict(exclude_none=True)
            create_project_url = self.label_studio_config.get("label_studio_project")
            logging.info(f"{create_project_url=}")
            response, status_code = APIInterface.post(
                route=create_project_url,
                data=create_project_request,
                headers=self.header,
            )
            logging.debug(f"createw project response : {response}")
            return response
        except Exception as error:
            logging.error(f"Error in create project controller: {error}")
            raise error

    def delete_project_controller(self, request):
        delete_project_url = f"{self.label_studio_config.get('label_studio_project')}/{request.project_id}"
        status_code = APIInterface.delete(route=delete_project_url, headers=self.header)
        if status_code == 204:
            return {"status": "Project Deleted Successfully"}
        else:
            return {"status": "Cannot Delete The Project"}
            # TODO: raise exceptions

    def export_annotations_controller(
        self, project_id: int, service_provider: str, bucket_name: str
    ):
        export_annotations_params = {"exportType": "JSON"}
        export_annotations_url = f"{self.label_studio_config.get('label_studio_project')}/{project_id}/export"
        response, status_code = APIInterface.get(
            route=export_annotations_url,
            params=export_annotations_params,
            headers=self.header,
        )
        if service_provider.lower() == "aws":
            cloud_uri = write_annotations_to_s3(
                bucket_name=bucket_name,
                json_data=response,
                prefix=f"label-studio/{project_id}",
            )
        elif service_provider.lower() == "gcp":
            cloud_uri = upload_blob_string(
                bucket_name=bucket_name,
                file=bytes(json.dumps(response).encode("UTF-8")),
                destination_file_name=f"label-studio/{project_id}/annotations_{str(datetime.now().timestamp())}.json",
                content_type="application/json",
            )
        else:
            cloud_uri = ""

        return {"cloud_uri": cloud_uri}

    def transform_annotations_controller(self, request):
        transform_annotation_request = request.dict(exclude_none=True)
        transform_annotation_url = self.core_label_studio_config.get(
            "transform_annotations"
        )
        response, status_code = APIInterface.post(
            route=transform_annotation_url,
            data=transform_annotation_request,
            headers=self.header,
        )
        return response


class StorageController:
    def __init__(self):
        self.label_studio_config = config.get("label_studio").get("endpoint")
        self.label_studio_token = config.get("label_studio").get("token")
        self.header = {"Authorization": f"Token {self.label_studio_token}"}
        self.aws_access_key_id = os.environ.get("AWS_ACCESS_KEY_ID")
        self.aws_secret_access_key = os.environ.get("AWS_SECRET_ACCESS_KEY")

    def create_s3_storage_controller(self, request):
        create_storage_request = request.dict(exclude_none=True)
        create_storage_request.update(
            {
                "aws_access_key_id": self.aws_access_key_id,
                "aws_secret_access_key": self.aws_secret_access_key,
            }
        )
        create_storage_url = self.label_studio_config.get("s3_storage")
        response, status_code = APIInterface.post(
            route=create_storage_url, data=create_storage_request, headers=self.header
        )
        return response

    def sync_s3_storage_controller(self, request):
        sync_storage_url = (
            f"{self.label_studio_config.get('s3_storage')}/{request.storage_id}/sync"
        )
        response, status_code = APIInterface.post(
            route=sync_storage_url, headers=self.header
        )
        return response

    def delete_s3_storage_controller(self, request):
        delete_storage_url = (
            f"{self.label_studio_config.get('s3_storage')}/{request.storage_id}"
        )
        status_code = APIInterface.delete(route=delete_storage_url, headers=self.header)
        if status_code == 204:
            return {"status": "Storage Deleted Successfully"}
        else:
            return {"status": "Cannot Delete The Storage"}
            # TODO: raise exceptions

    def create_gcs_storage_controller(self, request):
        create_storage_request = request.dict(exclude_none=True)
        create_storage_url = self.label_studio_config.get("gcs_storage")
        response, status_code = APIInterface.post(
            route=create_storage_url, data=create_storage_request, headers=self.header
        )
        return response

    def sync_gcs_storage_controller(self, request):
        sync_storage_url = (
            f"{self.label_studio_config.get('gcs_storage')}/{request.storage_id}/sync"
        )
        response, status_code = APIInterface.post(
            route=sync_storage_url, headers=self.header
        )
        return response

    def delete_gcs_storage_controller(self, request):
        delete_storage_url = (
            f"{self.label_studio_config.get('gcs_storage')}/{request.storage_id}"
        )
        status_code = APIInterface.delete(route=delete_storage_url, headers=self.header)
        if status_code == 204:
            return {"status": "Storage Deleted Successfully"}
        else:
            return {"status": "Cannot Delete The Storage"}
            # TODO: raise exceptions
