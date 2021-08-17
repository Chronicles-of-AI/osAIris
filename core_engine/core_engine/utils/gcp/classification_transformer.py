import pandas as pd
from core_engine import logger

logging = logger(__name__)


def gcp_image_classification_transformation(json_data: dict):
    """[Image Classification Transformation from Label Studio to AutoML format]

    Args:
        json_data (dict): [Annotations]

    Raises:
        error: [Error]

    Returns:
        [list]: [List of Annotations]
    """
    try:
        logging.info(f"Image Classification Transformer: {json_data}")
        all_annotations = []
        for obj in json_data:
            cloud_uri = obj.get("data").get("image")
            annotations = obj.get("annotations")[0]
            results = annotations.get("result")
            class_name = results[0].get("value").get("choices")[0]
            all_annotations.append([cloud_uri, class_name])
        annotations_df = pd.DataFrame(all_annotations)
        return annotations_df
    except Exception as error:
        logging.error(f"{error=}")
        raise error


def gcp_text_classification_transformation(json_data: dict):
    """[Text Classification Transformation from Label Studio to AutoML format]

    Args:
        json_data (dict): [Annotations]

    Raises:
        error: [Error]

    Returns:
        [list]: [List of Annotations]
    """
    try:
        logging.info(f"Text Classification Transformer: {json_data}")
        all_annotations = []
        for obj in json_data:
            text = obj.get("data").get("text")
            annotations = obj.get("annotations")[0]
            results = annotations.get("result")
            class_name = results[0].get("value").get("choices")[0]
            all_annotations.append([text, class_name])
        annotations_df = pd.DataFrame(all_annotations)
        return annotations_df
    except Exception as error:
        logging.error(f"{error=}")
        raise error
