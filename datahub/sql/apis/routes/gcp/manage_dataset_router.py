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
from sql import logger

logging = logger(__name__)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")

manage_dataset_router = APIRouter()


@manage_dataset_router.post(
    "/gcp/automl/list_datasets", response_model=ListDatasetsResponse
)
async def list_datasets(
    list_datasets_request: ListDatasets,
    token: str = Depends(oauth2_scheme),
):
    """[API router to list all AutoML datasets]

    Args:
        list_datasets_request (ListDatasets): [AutoML list all datasets request]
        token (str, optional): [Bearer token for authentication]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized exception when invalid token is passed]
        error: [Exception in underlying controller]

    Returns:
        [ListDatasetsResponse]: [List of all the datasets imported in AutoML]
    """
    try:
        logging.info("Calling /gcp/automl/list_datasets endpoint")
        logging.debug(f"Request: {list_datasets_request}")
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
    except Exception as error:
        logging.error(f"Error in /gcp/automl/list_datasets endpoint: {error}")
        raise error


@manage_dataset_router.post(
    "/gcp/automl/get_dataset_description", response_model=DescriptionDatasetsResponse
)
async def get_dataset_description(
    get_dataset_description_request: DescriptionDataset,
    token: str = Depends(oauth2_scheme),
):
    """[API router to get description of AutoML dataset]

    Args:
        get_dataset_description_request (DescriptionDataset): [Get AutoML dataset description request]
        token (str, optional): [Bearer token for authentication]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized exception when invalid token is passed]
        error: [Exception in underlying controller]

    Returns:
        [DescriptionDatasetsResponse]: [Description of the AutoML dataset]
    """
    try:
        logging.info("Calling /gcp/automl/get_dataset_description endpoint")
        logging.debug(f"Request: {get_dataset_description_request}")
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
    except Exception as error:
        logging.error(f"Error in /gcp/automl/get_dataset_description endpoint: {error}")
        raise error


@manage_dataset_router.post(
    "/gcp/automl/delete_dataset", response_model=DeleteDatasetResponse
)
async def delete_dataset(
    delete_dataset_request: DeleteDataset,
    token: str = Depends(oauth2_scheme),
):
    """[API router to delete a AutoML dataset]

    Args:
        delete_dataset_request (DeleteDataset): [AutoML delete dataset request]
        token (str, optional): [Bearer token for authentication]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized exception when invalid token is passed]
        error: [Exception in underlying controller]

    Returns:
        [DeleteDatasetResponse]: [delete AutoML dataset response]
    """
    try:
        logging.info("Calling /gcp/automl/delete_dataset endpoint")
        logging.debug(f"Request: {delete_dataset_request}")
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
    except Exception as error:
        logging.error(f"Error in /gcp/automl/delete_dataset endpoint: {error}")
        raise error
