from fastapi import APIRouter
from core_engine.apis.schemas.requests.gcp.dataset_management_request import (
    ListDatasets,
    DescriptionDataset,
    DeleteDataset,
)
from core_engine.controllers.gcp.dataset_management_controller import (
    ManageDatasetController,
)
from core_engine import logger

logging = logger(__name__)

manage_dataset_router = APIRouter()


@manage_dataset_router.post("/gcp/automl/list_datasets")
def list_datasets(
    list_datasets_request: ListDatasets,
):
    """[List Datasets in AutoML Router]

    Args:
        list_datasets_request (ListDatasets): [Based on Input Schema]

    Raises:
        error: [Error]

    Returns:
        [type]: [description]
    """
    try:
        logging.info(f"List Dataset Router: {list_datasets_request}")
        return ManageDatasetController().list_datasets_controller(
            request=list_datasets_request
        )
    except Exception as error:
        logging.error(f"{error=}")
        raise error


@manage_dataset_router.post("/gcp/automl/get_dataset_description")
def get_dataset_description(
    get_dataset_description_request: DescriptionDataset,
):
    """[Describe a Dataset in AutoML Router]

    Args:
        get_dataset_description_request (DescriptionDataset): [Based on Input Schema]

    Raises:
        error: [Error]

    Returns:
        [type]: [description]
    """
    try:
        logging.info(
            f"Get Dataset Descriptio Router: {get_dataset_description_request}"
        )
        return ManageDatasetController().get_dataset_description_controller(
            request=get_dataset_description_request
        )
    except Exception as error:
        logging.error(f"{error=}")
        raise error


@manage_dataset_router.post("/gcp/automl/delete_dataset")
def delete_dataset(
    delete_dataset_request: DeleteDataset,
):
    """[Delete a Dataset in AutoML Router]

    Args:
        delete_dataset_request (DeleteDataset): [Based on Input Schema]

    Raises:
        error: [Error]

    Returns:
        [type]: [description]
    """
    try:
        logging.info(f"Delete Dataset Router: {delete_dataset_request}")
        return ManageDatasetController().delete_dataset_controller(
            request=delete_dataset_request
        )
    except Exception as error:
        logging.error(f"{error=}")
        raise error
