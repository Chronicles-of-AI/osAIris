from google.cloud import automl
from core_engine import logger

client = automl.AutoMlClient()
logging = logger(__name__)


def create_dataset(dataset, project_location: str):
    """[Created a Dataset in AutoML GCP]

    Args:
        dataset ([type]): [Dataset Name]
        project_location (str): [Region]

    Raises:
        error: [Error]

    Returns:
        [type]: [description]
    """
    try:
        logging.info(f"Create Dataset: {dataset}")
        response = client.create_dataset(parent=project_location, dataset=dataset)

        created_dataset = response.result()

        # Display the dataset information
        logging.info("Dataset name: {}".format(created_dataset.name))
        logging.info("Dataset id: {}".format(created_dataset.name.split("/")[-1]))

        dataset_info = {
            "dataset_name": created_dataset.name,
            "dataset_id": created_dataset.name.split("/")[-1],
        }
        return dataset_info
    except Exception as error:
        logging.error(f"{error=}")
        raise error


def create_text_classification_dataset(
    project_id: str, display_name: str, region: str, multi_label: bool = False
):
    """[Created a Text Classification Dataset in AutoML GCP]

    Args:
        project_id (str): [Unique Identifier for your Project]
        display_name (str): [Display NAme for GCP Console]
        region (str): [Region]
        multi_label (bool, optional): [MULTILABEL / MULTICLASS]. Defaults to False.

    Raises:
        error: [Error]

    Returns:
        [type]: [description]
    """
    try:
        logging.info(f"Create Text Classification Dataset: {project_id}")
        logging.info(f"{display_name=}")
        logging.info(f"{region=}")
        project_location = f"projects/{project_id}/locations/{region}"
        # us-central1
        if not multi_label:
            metadata = automl.TextClassificationDatasetMetadata(
                classification_type=automl.ClassificationType.MULTICLASS
            )
        else:
            metadata = automl.TextClassificationDatasetMetadata(
                classification_type=automl.ClassificationType.MULTILABEL
            )
        dataset = automl.Dataset(
            display_name=display_name,
            text_classification_dataset_metadata=metadata,
        )
        dataset_response = create_dataset(
            dataset=dataset, project_location=project_location
        )
        return dataset_response
    except Exception as error:
        logging.error(f"{error=}")
        raise error


def create_ner_dataset(project_id: str, display_name: str, region: str):
    """[Created a NER Dataset in AutoML GCP]

    Args:
        project_id (str): [Unique Identifier for your Project]
        display_name (str): [Display NAme for GCP Console]
        region (str): [Region]

    Raises:
        error: [Error]

    Returns:
        [type]: [description]
    """
    try:
        logging.info(f"Create NER Dataset: {project_id}")
        logging.info(f"{display_name=}")
        logging.info(f"{region=}")
        project_location = f"projects/{project_id}/locations/{region}"
        metadata = automl.TextExtractionDatasetMetadata()
        dataset = automl.Dataset(
            display_name=display_name, text_extraction_dataset_metadata=metadata
        )
        dataset_response = create_dataset(
            dataset=dataset, project_location=project_location
        )
        return dataset_response
    except Exception as error:
        logging.error(f"{error=}")
        raise error


def create_image_classification_dataset(
    project_id: str, display_name: str, region: str, multi_label: bool = False
):
    """[Created a Image Classification Dataset in AutoML GCP]

    Args:
        project_id (str): [Unique Identifier for your Project]
        display_name (str): [Display NAme for GCP Console]
        region (str): [Region]
        multi_label (bool, optional): [description]. Defaults to False.

    Raises:
        error: [Error]

    Returns:
        [type]: [description]
    """
    try:
        logging.info(f"Create Image Classification Dataset: {project_id}")
        logging.info(f"{display_name=}")
        logging.info(f"{region=}")
        project_location = f"projects/{project_id}/locations/{region}"
        if not multi_label:
            metadata = automl.ImageClassificationDatasetMetadata(
                classification_type=automl.ClassificationType.MULTICLASS
            )
        else:
            metadata = automl.ImageClassificationDatasetMetadata(
                classification_type=automl.ClassificationType.MULTILABEL
            )
        dataset = automl.Dataset(
            display_name=display_name,
            image_classification_dataset_metadata=metadata,
        )
        dataset_response = create_dataset(
            dataset=dataset, project_location=project_location
        )
        return dataset_response
    except Exception as error:
        logging.error(f"{error=}")
        raise error


def create_object_detection_dataset(project_id: str, display_name: str, region: str):
    """[Created a Object Detection Dataset in AutoML GCP]

    Args:
        project_id (str): [Unique Identifier for your Project]
        display_name (str): [Display NAme for GCP Console]
        region (str): [Region]

    Raises:
        error: [Error]

    Returns:
        [type]: [description]
    """
    try:
        logging.info(f"Create Object Detection Dataset: {project_id}")
        logging.info(f"{display_name=}")
        logging.info(f"{region=}")
        project_location = f"projects/{project_id}/locations/{region}"
        metadata = automl.ImageObjectDetectionDatasetMetadata()
        dataset = automl.Dataset(
            display_name=display_name, image_object_detection_dataset_metadata=metadata
        )
        dataset_response = create_dataset(
            dataset=dataset, project_location=project_location
        )
        return dataset_response
    except Exception as error:
        logging.error(f"{error=}")
        raise error
