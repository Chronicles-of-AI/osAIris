from fastapi import APIRouter
from sql.apis.schemas.requests.gcp.dataset_management_request import (
    ListDatasets,
    DescriptionDataset,
    DeleteDataset,
)
from sql.controllers.gcp.dataset_management_controller import ManageDatasetController

manage_dataset_router = APIRouter()


@manage_dataset_router.post("/gcp/automl/list_datasets")
def list_datasets(
    list_datasets_request: ListDatasets,
):
    return ManageDatasetController().list_datasets_controller(
        request=list_datasets_request
    )


@manage_dataset_router.post("/gcp/automl/get_dataset_description")
def get_dataset_description(
    get_dataset_description_request: DescriptionDataset,
):
    return ManageDatasetController().get_dataset_description_controller(
        request=get_dataset_description_request
    )


@manage_dataset_router.post("/gcp/automl/delete_dataset")
def delete_dataset(
    delete_dataset_request: DeleteDataset,
):
    return ManageDatasetController().delete_dataset_controller(
        request=delete_dataset_request
    )
