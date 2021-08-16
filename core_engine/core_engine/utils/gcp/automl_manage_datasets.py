from google.cloud import automl
from core_engine import logger

# TODO(developer): Uncomment and set the following variables
# project_id = "YOUR_PROJECT_ID"

client = automl.AutoMlClient()
logging = logger(__name__)


def get_dataset_description(project_id: str, region: str, dataset_id: str):
    """[Get Dataset Description]

    Args:
        project_id (str): [Unique Identifier for your Project]
        region (str): [Region]
        dataset_id (str): [Unique Identifier for your Dataset]

    Raises:
        error: [Error]

    Returns:
        [dict]: [description]
    """
    try:
        logging.info(f"Get Dataset Description for Project ID: {project_id}")
        logging.info(f"{dataset_id=}")
        dataset_full_id = client.dataset_path(project_id, region, dataset_id)
        dataset = client.get_dataset(name=dataset_full_id)

        dataset_dict = {
            "dataset_name": dataset.name,
            "dataset_id": dataset.name.split("/")[-1],
            "display_name": dataset.display_name,
        }
        return {"dataset_description": dataset_dict}
    except Exception as error:
        logging.error(f"{error=}")
        raise error


def list_datasets(project_id: str, region: str):
    """[List Datasets in AutoML]

    Args:
        project_id (str): [Unique Identifier for your Project]
        region (str): [Region]

    Raises:
        error: [Error]

    Returns:
        [type]: [description]
    """
    try:
        logging.info(f"Get Dataset Description for Project ID: {project_id}")
        project_location = f"projects/{project_id}/locations/{region}"
        request = automl.ListDatasetsRequest(parent=project_location, filter="")
        response = client.list_datasets(request=request)

        all_datasets = []
        for dataset in response:
            dataset_dict = {
                "dataset_name": dataset.name,
                "dataset_id": dataset.name.split("/")[-1],
                "display_name": dataset.display_name,
            }
            all_datasets.append(dataset_dict)
        return {"all_datasets": all_datasets}
    except Exception as error:
        logging.error(f"{error=}")
        raise error


def delete_datasets(project_id: str, region: str, dataset_id: str):
    """[Deletes a Dataset in AutoML]

    Args:
        project_id (str): [Unique Identifier for your Project]
        region (str): [Region]
        dataset_id (str): [Unique Identifier for your Dataset]

    Raises:
        error: [Error]

    Returns:
        [type]: [Status]
    """
    try:
        logging.info(f"Delete Dataset Description for Project ID: {project_id}")
        logging.info(f"{dataset_id=}")
        dataset_full_id = client.dataset_path(project_id, region, dataset_id)
        response = client.delete_dataset(name=dataset_full_id)
        return {
            "status": "Deleting",
            "operation_id": response.operation.name,
            "project_id": project_id,
            "region": region,
            "dataset_id": dataset_id,
        }
    except Exception as error:
        logging.error(f"{error=}")
        raise error
