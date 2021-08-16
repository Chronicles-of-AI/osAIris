from google.cloud import automl
from core_engine import logger

# Sample variable values
# project_id = "us-gcp-ame-con-be2-npd-1"
# dataset_id = "TCN8344915572575698944"
# display_name = "decision_caller_api_model_v1"

client = automl.AutoMlClient()
logging = logger(__name__)


def train_text_classification_model(
    project_id: str, dataset_id: str, model_display_name: str, region: str
):
    """[Train Text Classification Model in AutoML GCP]

    Args:
        project_id (str): [Unique Identifier for your Project]
        dataset_id (str): [Unique Identifier for your Dataset]
        model_display_name (str): [Display name for GCP console]
        region (str): [Region]

    Raises:
        error: [Error]

    Returns:
        [dict]: [Stauts]
    """
    try:
        logging.info(f"Train Text Classification Model for Project ID: {project_id}")
        logging.info(f"{dataset_id=}")
        logging.info(f"{model_display_name=}")
        project_location = f"projects/{project_id}/locations/{region}"
        metadata = automl.TextClassificationModelMetadata()
        model = automl.Model(
            display_name=model_display_name,
            dataset_id=dataset_id,
            text_classification_model_metadata=metadata,
        )
        response = client.create_model(parent=project_location, model=model)

        return {
            "operation_id": response.operation.name,
            "dataset_id": dataset_id,
            "status": "Training Started",
            "project_id": project_id,
            "region": region,
        }
    except Exception as error:
        logging.error(f"{error=}")
        raise error


def train_ner_model(
    project_id: str, dataset_id: str, model_display_name: str, region: str
):
    """[Train NER Model in AutoML GCP]

    Args:
        project_id (str): [Unique Identifier for your Project]
        dataset_id (str): [Unique Identifier for your Dataset]
        model_display_name (str): [Display name for GCP console]
        region (str): [Region]

    Raises:
        error: [Error]

    Returns:
        [dict]: [Stauts]
    """
    try:
        logging.info(f"Train NER Model for Project ID: {project_id}")
        logging.info(f"{dataset_id=}")
        logging.info(f"{model_display_name=}")
        # A resource that represents Google Cloud Platform location.
        project_location = f"projects/{project_id}/locations/{region}"
        # Leave model unset to use the default base model provided by Google
        metadata = automl.TextExtractionModelMetadata()
        model = automl.Model(
            display_name=model_display_name,
            dataset_id=dataset_id,
            text_extraction_model_metadata=metadata,
        )

        # Create a model with the model metadata in the region.
        response = client.create_model(parent=project_location, model=model)
        return {
            "operation_id": response.operation.name,
            "dataset_id": dataset_id,
            "status": "Training Started",
            "project_id": project_id,
            "region": region,
        }
    except Exception as error:
        logging.error(f"{error=}")
        raise error


def train_image_classification_model(
    project_id: str, dataset_id: str, model_display_name: str, region: str
):
    """[Train Image Classification Model in AutoML GCP]

    Args:
        project_id (str): [Unique Identifier for your Project]
        dataset_id (str): [Unique Identifier for your Dataset]
        model_display_name (str): [Display name for GCP console]
        region (str): [Region]

    Raises:
        error: [Error]

    Returns:
        [dict]: [Stauts]
    """
    try:
        logging.info(f"Train Image Classification Model for Project ID: {project_id}")
        logging.info(f"{dataset_id=}")
        logging.info(f"{model_display_name=}")
        project_location = f"projects/{project_id}/locations/{region}"
        metadata = automl.ImageClassificationModelMetadata(
            train_budget_milli_node_hours=24000
        )
        model = automl.Model(
            display_name=model_display_name,
            dataset_id=dataset_id,
            image_classification_model_metadata=metadata,
        )

        # Create a model with the model metadata in the region.
        response = client.create_model(parent=project_location, model=model)
        return {
            "operation_id": response.operation.name,
            "dataset_id": dataset_id,
            "status": "Training Started",
            "project_id": project_id,
            "region": region,
        }
    except Exception as error:
        logging.error(f"{error=}")
        raise error


def train_image_classification_edge_model(
    project_id: str,
    dataset_id: str,
    model_display_name: str,
    region: str,
    model_type: str = "mobile-versatile-1",
):
    """[Train Image Classification Model for Edge in AutoML GCP]

    Args:
        project_id (str): [Unique Identifier for your Project]
        dataset_id (str): [Unique Identifier for your Dataset]
        model_display_name (str): [Display name for GCP console]
        region (str): [Region]
        model_type (str, optional): [description]. Defaults to "mobile-versatile-1".

    Raises:
        error: [Error]

    Returns:
        [dict]: [Stauts]
    """
    try:
        logging.info(
            f"Train Image Classification Model for Edge for Project ID: {project_id}"
        )
        logging.info(f"{dataset_id=}")
        logging.info(f"{model_display_name=}")
        project_location = f"projects/{project_id}/locations/{region}"
        metadata = automl.ImageClassificationModelMetadata(
            train_budget_milli_node_hours=24000, model_type=model_type
        )
        model = automl.Model(
            display_name=model_display_name,
            dataset_id=dataset_id,
            image_classification_model_metadata=metadata,
        )

        # Create a model with the model metadata in the region.
        response = client.create_model(parent=project_location, model=model)
        return {
            "operation_id": response.operation.name,
            "dataset_id": dataset_id,
            "status": "Training Started",
            "project_id": project_id,
            "region": region,
        }
    except Exception as error:
        logging.error(f"{error=}")
        raise error


def train_object_detection_model(
    project_id: str, dataset_id: str, model_display_name: str, region: str
):
    """[Train Object Deteciton Model in AutoML GCP]

    Args:
        project_id (str): [Unique Identifier for your Project]
        dataset_id (str): [Unique Identifier for your Dataset]
        model_display_name (str): [Display name for GCP console]
        region (str): [Region]

    Raises:
        error: [Error]

    Returns:
        [dict]: [Stauts]
    """
    try:
        logging.info(f"Train Object Detection Model for Project ID: {project_id}")
        logging.info(f"{dataset_id=}")
        logging.info(f"{model_display_name=}")
        project_location = f"projects/{project_id}/locations/{region}"
        metadata = automl.ImageClassificationModelMetadata(
            train_budget_milli_node_hours=24000
        )
        model = automl.Model(
            display_name=model_display_name,
            dataset_id=dataset_id,
            image_classification_model_metadata=metadata,
        )

        # Create a model with the model metadata in the region.
        response = client.create_model(parent=project_location, model=model)
        return {
            "operation_id": response.operation.name,
            "dataset_id": dataset_id,
            "status": "Training Started",
            "project_id": project_id,
            "region": region,
        }
    except Exception as error:
        logging.error(f"{error=}")
        raise error


def train_object_detection_edge_model(
    project_id: str,
    dataset_id: str,
    model_display_name: str,
    region: str,
    model_type: str = "mobile-versatile-1",
):
    """[Train Object Deteciton Model for Edge in AutoML GCP]

    Args:
        project_id (str): [Unique Identifier for your Project]
        dataset_id (str): [Unique Identifier for your Dataset]
        model_display_name (str): [Display name for GCP console]
        region (str): [Region]
        model_type (str, optional): [description]. Defaults to "mobile-versatile-1".

    Raises:
        error: [Error]

    Returns:
        [dict]: [Stauts]
    """
    try:
        logging.info(
            f"Train Object Detection Model for Edge for Project ID: {project_id}"
        )
        logging.info(f"{dataset_id=}")
        logging.info(f"{model_display_name=}")
        project_location = f"projects/{project_id}/locations/{region}"
        metadata = automl.ImageClassificationModelMetadata(
            train_budget_milli_node_hours=24000, model_type=model_type
        )
        model = automl.Model(
            display_name=model_display_name,
            dataset_id=dataset_id,
            image_classification_model_metadata=metadata,
        )

        # Create a model with the model metadata in the region.
        response = client.create_model(parent=project_location, model=model)
        return {
            "operation_id": response.operation.name,
            "dataset_id": dataset_id,
            "status": "Training Started",
            "project_id": project_id,
            "region": region,
        }
    except Exception as error:
        logging.error(f"{error=}")
        raise error
