from fastapi import APIRouter, Depends, HTTPException, status
from sql.apis.schemas.requests.gcp.dataset_management_request import (
    ListDatasets,
    DescriptionDataset,
    DeleteDataset,
)
from sql.apis.schemas.responses.gcp.dataset_management_response import (
    DeleteDatasetResponse,
    ListDatasetsResponse,
    DescriptionDatasetsResponse,
)
from sql.controllers.gcp.dataset_management_controller import ManageDatasetController
from fastapi.security import OAuth2PasswordBearer
from commons.auth import decodeJWT

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")

manage_dataset_router = APIRouter()


@manage_dataset_router.post(
    "/gcp/automl/list_datasets", response_model=ListDatasetsResponse
)
def list_datasets(
    list_datasets_request: ListDatasets,
    token: str = Depends(oauth2_scheme),
):
    if decodeJWT(token=token):
        response = ManageDatasetController().list_datasets_controller(
            request=list_datasets_request
        )
        return ListDatasetsResponse(**response)
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid access token",
            headers={"WWW-Authenticate": "Bearer"},
        )


@manage_dataset_router.post(
    "/gcp/automl/get_dataset_description", response_model=DescriptionDatasetsResponse
)
def get_dataset_description(
    get_dataset_description_request: DescriptionDataset,
    token: str = Depends(oauth2_scheme),
):
    if decodeJWT(token=token):
        response = ManageDatasetController().get_dataset_description_controller(
            request=get_dataset_description_request
        )
        return DescriptionDatasetsResponse(**response)
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid access token",
            headers={"WWW-Authenticate": "Bearer"},
        )


@manage_dataset_router.post(
    "/gcp/automl/delete_dataset", response_model=DeleteDatasetResponse
)
def delete_dataset(
    delete_dataset_request: DeleteDataset,
    token: str = Depends(oauth2_scheme),
):
    if decodeJWT(token=token):
        response = ManageDatasetController().delete_dataset_controller(
            request=delete_dataset_request
        )
        return DeleteDatasetResponse(**response)
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid access token",
            headers={"WWW-Authenticate": "Bearer"},
        )
