import json
from datetime import datetime
from utils.aws.s3_helper import read_annotations_from_s3, write_annotations_to_s3
from utils.label_studio.label_studio_helper import transform_annotations
from utils.gcp.gcs_helper import read_file_from_gcs, upload_blob_string
from core_engine import logger

logging = logger(__name__)


class ProjectController:
    def __init__(self) -> None:
        pass

    def transform_annotations_controller(self, request):
        """[Transform Annotations of Label Studio into GCP AutomL format]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [Transformed Annotations]
        """
        try:
            logging.info(f"Transfirm annotations Controller: {request}")
            if request.service_provider == "aws":
                annotations_data = read_annotations_from_s3(
                    input_data_s3_uri=request.input_data_uri
                )
                transformed_annotation_data = transform_annotations(
                    json_data=annotations_data,
                    service_provider=request.service_provider,
                )
                transformed_cloud_uri = write_annotations_to_s3(
                    bucket_name=request.output_data_bucket_name,
                    byte_data=transformed_annotation_data,
                    prefix=request.output_data_file_prefix,
                )
            elif request.service_provider == "gcp":
                bucket_name = request.input_data_uri.split("//")[-1].split("/")[0]
                file_path = "/".join(
                    request.input_data_uri.split("//")[-1].split("/")[1:]
                )
                annotations_data = read_file_from_gcs(
                    file_path=file_path, bucket_name=bucket_name
                )
                transformed_annotation_df = transform_annotations(
                    json_data=json.loads(annotations_data.decode("UTF-8")),
                    service_provider=request.service_provider,
                )
                transformed_cloud_uri = upload_blob_string(
                    bucket_name=request.output_data_bucket_name,
                    file=transformed_annotation_df.to_csv(header=False, index=False),
                    destination_file_name=f"{request.output_data_file_prefix}/annotations_{str(int(datetime.now().timestamp())*10000)}.csv",
                    content_type="text/csv",
                )
            else:
                transformed_cloud_uri = ""
            return {"cloud_uri": transformed_cloud_uri}
        except Exception as error:
            logging.error(f"{error=}")
            raise error
