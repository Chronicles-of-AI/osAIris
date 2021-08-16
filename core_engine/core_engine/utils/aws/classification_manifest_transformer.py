import datetime
from core_engine import logger

logging = logger(__name__)


def aws_image_classification_transformation(json_data: dict):
    """[Converting Label Studio Annotations to AWS Manifest file needs]

    Args:
        json_data (dict): [All annotations]

    Raises:
        e: [Error]

    Returns:
        [list]: [All Annotations]
    """
    try:
        logging.info(f"AWS Image Classification Transformation for JSON: {json_data}")
        all_annotations = []
        for obj in json_data:
            cloud_uri = obj.get("data").get("image")
            annotations = obj.get("annotations")[0]
            results = annotations.get("result")
            class_name = results[0].get("value").get("choices")[0]
            final_sample_annot = {
                "source-ref": cloud_uri,
                "image_classification": 1,
                "image_classification-metadata": {
                    "confidence": 1,
                    "class-name": class_name,
                    "type": "groundtruth/image-classification",
                    "human-annotated": "yes",
                    "creation-date": "T".join(
                        str(datetime.datetime.today()).split(" ")
                    ),
                    "job-name": "labeling-job/image_classification",
                },
            }
            all_annotations.append(final_sample_annot)
        return all_annotations
    except Exception as e:
        logging.error(e)
        raise e


def aws_text_classification_transformation(json_data: dict):
    """[Converting Label Studio Annotations to AWS Manifest file needs]

    Args:
        json_data (dict): [All annotations]

    Raises:
        error: [Error]

    Returns:
        [list]: [All annotations]
    """
    try:
        logging.info(f"AWS Text Classification Transformation for JSON: {json_data}")
        all_annotations = []
        for obj in json_data:
            text = obj.get("data").get("text")
            annotations = obj.get("annotations")[0]
            results = annotations.get("result")
            class_name = results[0].get("value").get("choices")[0]
            final_sample_annot = {
                "source": text,
                "text_classification": 1,
                "text_classification-metadata": {
                    "confidence": 1,
                    "class-name": class_name,
                    "type": "groundtruth/text-classification",
                    "human-annotated": "yes",
                    "creation-date": "T".join(
                        str(datetime.datetime.today()).split(" ")
                    ),
                    "job-name": "labeling-job/text_classification",
                },
            }
            all_annotations.append(final_sample_annot)
        return all_annotations
    except Exception as error:
        logging.error(f"{error=}")
        raise error
