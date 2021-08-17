import json

from core_engine.utils.aws.object_detection_transformer import (
    aws_object_detection_transformation,
)
from core_engine.utils.aws.classification_manifest_transformer import (
    aws_image_classification_transformation,
    aws_text_classification_transformation,
)
from core_engine.utils.gcp.classification_transformer import (
    gcp_image_classification_transformation,
    gcp_text_classification_transformation,
)
from core_engine.utils.gcp.object_detection_transformer import (
    gcp_object_detection_transformation,
)
from core_engine import logger

logging = logger(__name__)


def transform_annotations(json_data: dict, service_provider: str):
    """[Transform Annotations from Label Studio into Expected format]

    Args:
        json_data (dict): [Annotations]
        service_provider (str): [Cloud Service Provider - aws/gcp/azure]

    Raises:
        error: [Error]

    Returns:
        [type]: [description]
    """
    try:
        logging.info(f"Transform Annotations: {json_data}")
        logging.info(f"{service_provider=}")
        use_case = json_data[0].get("annotations")[0].get("result")[0].get("type")
        type_of_data = (
            json_data[0].get("annotations")[0].get("result")[0].get("to_name")
        )
        if service_provider.lower() == "aws":
            if use_case == "rectanglelabels" and type_of_data == "image":
                transformed_annotation_response = aws_object_detection_transformation(
                    json_data=json_data
                )
            elif use_case == "choices" and type_of_data == "image":
                transformed_annotation_response = (
                    aws_image_classification_transformation(json_data=json_data)
                )
            elif use_case == "choices" and type_of_data == "text":
                transformed_annotation_response = (
                    aws_text_classification_transformation(json_data=json_data)
                )
            return json.dumps(transformed_annotation_response).encode("UTF-8")
        elif service_provider.lower() == "gcp":
            if use_case == "rectanglelabels" and type_of_data == "image":
                transformed_annotation_response = gcp_object_detection_transformation(
                    json_data=json_data
                )
            elif use_case == "choices" and type_of_data == "image":
                transformed_annotation_response = (
                    gcp_image_classification_transformation(json_data=json_data)
                )
            elif use_case == "choices" and type_of_data == "text":
                transformed_annotation_response = (
                    gcp_text_classification_transformation(json_data=json_data)
                )
            # TODO: Add support for NER in GCP
            return transformed_annotation_response
    except Exception as error:
        logging.error(f"{error=}")
        raise error
