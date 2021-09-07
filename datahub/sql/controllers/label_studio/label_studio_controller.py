import os
import json
from datetime import datetime
from commons.external_call import APIInterface
from sql import config, logger
from sql.utils.s3_helper import write_annotations_to_s3
from sql.utils.gcs_helper import upload_blob_string
from sql.crud.project_flow_crud import CRUDProjectFlow

logging = logger(__name__)


class ProjectController:
    def __init__(self):
        self.CRUDProjectFlow = CRUDProjectFlow()
        self.label_studio_config = config.get("label_studio").get("endpoint")
        self.label_studio_token = config.get("label_studio").get("token")
        self.core_label_studio_config = config.get("core_engine").get(
            "label_studio_router"
        )
        self.header = {"Authorization": f"Token {self.label_studio_token}"}

    def create_project_controller(self, request):
        """[Controller function to create label studio project]

        Args:
            request ([dict]): [create label studio project request]

        Raises:
            error: [Error from label studio controller]

        Returns:
            [dict]: [label studio project details]
        """
        try:
            logging.info(f"Creating a annotation project on Label Studio")
            create_project_request = request.dict(exclude_none=True)
            create_project_url = self.label_studio_config.get("label_studio_project")
            logging.info(f"{create_project_url=}")
            response, status_code = APIInterface.post(
                route=create_project_url,
                data=create_project_request,
                headers=self.header,
            )
            return response
        except Exception as error:
            logging.error(f"Error in create_project_controller: {error}")
            raise error

    def list_projects_controller(self):
        """[Controller function to list label studio projects]

        Raises:
            error: [Error from label studio controller]

        Returns:
            [dict]: [label studio projects details]
        """
        try:
            logging.info(f"list all annotation project on Label Studio")
            list_project_url = self.label_studio_config.get("list_projects")
            logging.info(f"{list_project_url=}")
            response, status_code = APIInterface.post(
                route=list_project_url,
                params={"ordering": "id"},
                headers=self.header,
            )
            return response
        except Exception as error:
            logging.error(f"Error in list_projects_controller: {error}")
            raise error

    def delete_project_controller(self, request):
        """[Controller function to delete label studio project]

        Args:
            request ([dict]): [delete label studio project request]

        Raises:
            error: [Error from label studio controller]

        Returns:
            [dict]: [label studio project status]
        """
        try:
            logging.info(f"Deleting a annotation project from Label Studio")
            delete_project_url = f"{self.label_studio_config.get('label_studio_project')}/{request.project_id}"
            status_code = APIInterface.delete(
                route=delete_project_url, headers=self.header
            )
            if status_code == 204:
                return {"status": "Project Deleted Successfully"}
            else:
                raise Exception({"status": "Cannot Delete The Project"})
        except Exception as error:
            logging.error(f"Error in delete_project_controller: {error}")
            raise error

    def export_annotations_controller(
        self, project_id: int, service_provider: str, bucket_name: str, pipeline_id: int
    ):
        """[Controller function to export annotations from label studio project]

        Args:
            project_id (int): [Unique identifier for project]
            service_provider (str): [cloud service provider name]
            bucket_name (str): [bucket to save the annotation file on]

        Raises:
            error: [Error from label studio controller]

        Returns:
            [str]: [cloud uri for the exported annotation file]
        """
        try:
            logging.info(f"Exporting annotations from Label Studio project")
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

            project_flow_crud_request = {
                "raw_annotation_uri": cloud_uri,
                "current_stage": "EXPORT_ANNOTATIONS",
                "updated_at": datetime.now(),
                "pipeline_id": pipeline_id,
            }
            self.CRUDProjectFlow.update(**project_flow_crud_request)
            return {"cloud_uri": cloud_uri}
        except Exception as error:
            logging.error(f"Error in export_annotations_controller: {error}")
            raise error

    def transform_annotations_controller(self, request):
        """[Controller function to transform annotation]

        Args:
            request ([dict]): [transform annotation request]

        Raises:
            error: [Error from label studio controller]

        Returns:
            [dict]: [transformed annotation file details]
        """
        try:
            logging.info(f"Transform annotations from Label Studio project")
            transform_annotation_request = request.dict(exclude_none=True)
            transform_annotation_url = self.core_label_studio_config.get(
                "transform_annotations"
            )
            response, status_code = APIInterface.post(
                route=transform_annotation_url,
                data=transform_annotation_request,
                headers=self.header,
            )
            project_flow_crud_request = {
                "transform_annotation_uri": response.get("cloud_uri"),
                "current_stage": "TRANSFORM_ANNOTATIONS",
                "updated_at": datetime.now(),
                "pipeline_id": request.pipeline_id,
            }
            self.CRUDProjectFlow.update(**project_flow_crud_request)
            return response
        except Exception as error:
            logging.error(f"Error in transform_annotations_controller: {error}")
            raise error


class StorageController:
    def __init__(self):
        self.label_studio_config = config.get("label_studio").get("endpoint")
        self.label_studio_token = config.get("label_studio").get("token")
        self.header = {"Authorization": f"Token {self.label_studio_token}"}
        self.aws_access_key_id = os.environ.get("AWS_ACCESS_KEY_ID")
        self.aws_secret_access_key = os.environ.get("AWS_SECRET_ACCESS_KEY")

    def create_s3_storage_controller(self, request):
        """[Controller function to add S3 storage to project]

        Args:
            request ([dict]): [add S3 storage to project request]

        Raises:
            error: [Error from label studio controller]

        Returns:
            [dict]: [storage details]
        """
        try:
            logging.info(f"Create S3 storage Label Studio project")
            create_storage_request = request.dict(exclude_none=True)
            create_storage_request.update(
                {
                    "aws_access_key_id": self.aws_access_key_id,
                    "aws_secret_access_key": self.aws_secret_access_key,
                }
            )
            create_storage_url = self.label_studio_config.get("s3_storage")
            response, status_code = APIInterface.post(
                route=create_storage_url,
                data=create_storage_request,
                headers=self.header,
            )
            return response
        except Exception as error:
            logging.error(f"Error in create_s3_storage_controller: {error}")
            raise error

    def sync_s3_storage_controller(self, request):
        """[Controller function to sync S3 storage to project]

        Args:
            request ([dict]): [sync S3 storage to project request]

        Raises:
            error: [Error from label studio controller]

        Returns:
            [dict]: [storage details]
        """
        try:
            logging.info(f"Sync S3 storage with Label Studio project")
            sync_storage_url = f"{self.label_studio_config.get('s3_storage')}/{request.storage_id}/sync"
            response, status_code = APIInterface.post(
                route=sync_storage_url, headers=self.header
            )
            return response
        except Exception as error:
            logging.error(f"Error in sync_s3_storage_controller: {error}")
            raise error

    def delete_s3_storage_controller(self, request):
        """[Controller function to delete S3 storage to project]

        Args:
            request ([dict]): [delete S3 storage to project request]

        Raises:
            error: [Error from label studio controller]

        Returns:
            [dict]: [storage details]
        """
        try:
            logging.info(f"Delete S3 storage from Label Studio project")
            delete_storage_url = (
                f"{self.label_studio_config.get('s3_storage')}/{request.storage_id}"
            )
            status_code = APIInterface.delete(
                route=delete_storage_url, headers=self.header
            )
            if status_code == 204:
                return {"status": "Storage Deleted Successfully"}
            else:
                raise Exception({"status": "Cannot Delete The Storage"})
        except Exception as error:
            logging.error(f"Error in delete_s3_storage_controller: {error}")
            raise error

    def list_storages_controller(self, project_id: int):
        """[Controller function to list S3 storages]

        Args:
            request ([dict]): [list S3 storages]

        Raises:
            error: [Error from label studio controller]

        Returns:
            [dict]: [storage details]
        """
        try:
            logging.info(f"list S3 storages from Label Studio project")
            list_storage_url = f"{self.label_studio_config.get('storage')}"
            response, status_code = APIInterface.get(
                route=list_storage_url,
                params={"project": project_id},
                headers=self.header,
            )
            if status_code == 200:
                return {"storages": response}
            else:
                raise Exception({"status": "Cannot list Storages"})
        except Exception as error:
            logging.error(f"Error in delete_s3_storage_controller: {error}")
            raise error

    def create_gcs_storage_controller(self, request):
        """[Controller function to add GCS storage to project]

        Args:
            request ([dict]): [add GCS storage to project request]

        Raises:
            error: [Error from label studio controller]

        Returns:
            [dict]: [storage details]
        """
        try:
            logging.info("Create GCS storage on Label Studio project")
            create_storage_request = request.dict(exclude_none=True)
            create_storage_url = self.label_studio_config.get("gcs_storage")
            response, status_code = APIInterface.post(
                route=create_storage_url,
                data=create_storage_request,
                headers=self.header,
            )
            return response
        except Exception as error:
            logging.error(f"Error in create_gcs_storage_controller: {error}")
            raise error

    def sync_gcs_storage_controller(self, request):
        """[Controller function to sync GCS storage to project]

        Args:
            request ([dict]): [sync GCS storage to project request]

        Raises:
            error: [Error from label studio controller]

        Returns:
            [dict]: [storage details]
        """
        try:
            logging.info("Sync GCS storage on Label Studio project")
            sync_storage_url = f"{self.label_studio_config.get('gcs_storage')}/{request.storage_id}/sync"
            response, status_code = APIInterface.post(
                route=sync_storage_url, headers=self.header
            )
            return response
        except Exception as error:
            logging.error(f"Error in sync_gcs_storage_controller: {error}")
            raise error

    def delete_gcs_storage_controller(self, request):
        """[Controller function to delete GCS storage to project]

        Args:
            request ([dict]): [delete GCS storage to project request]

        Raises:
            error: [Error from label studio controller]

        Returns:
            [dict]: [storage details]
        """
        try:
            logging.info("Delete GCS storage on Label Studio project")
            delete_storage_url = (
                f"{self.label_studio_config.get('gcs_storage')}/{request.storage_id}"
            )
            status_code = APIInterface.delete(
                route=delete_storage_url, headers=self.header
            )
            if status_code == 204:
                return {"status": "Storage Deleted Successfully"}
            else:
                raise Exception({"status": "Cannot Delete The Storage"})
        except Exception as error:
            logging.error(f"Error in delete_gcs_storage_controller: {error}")
            raise error
