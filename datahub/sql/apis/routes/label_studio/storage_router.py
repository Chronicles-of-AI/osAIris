from fastapi import APIRouter, Depends, HTTPException, status
from sql.apis.schemas.requests.label_studio.storage_request import (
    CreateStorage,
    Storage,
    CreateGCSStorage,
)
from sql.apis.schemas.responses.label_studio.storage_response import (
    CreateGCSStorageResponse,
    CreateStorageResponse,
    StorageDeleteResponse,
    StorageResponse,
)
from sql.controllers.label_studio.label_studio_controller import StorageController
from fastapi.security import OAuth2PasswordBearer
from commons.auth import decodeJWT

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")
storage_router = APIRouter()


@storage_router.post(
    "/label_studio/create_s3_storage", response_model=CreateStorageResponse
)
def create_s3_storage(
    create_storage_request: CreateStorage, token: str = Depends(oauth2_scheme)
):
    """[summary]

    Args:
        create_storage_request (CreateStorage): [description]
        token (str, optional): [description]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [description]
        error: [description]

    Returns:
        [type]: [description]
    """
    try:
        if decodeJWT(token=token):
            response = StorageController().create_s3_storage_controller(
                create_storage_request
            )
            return CreateStorageResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        raise error


@storage_router.post("/label_studio/sync_s3_storage", response_model=StorageResponse)
async def sync_s3_storage(
    sync_storage_request: Storage, token: str = Depends(oauth2_scheme)
):
    """[summary]

    Args:
        sync_storage_request (Storage): [description]
        token (str, optional): [description]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [description]
        error: [description]

    Returns:
        [type]: [description]
    """
    try:
        if decodeJWT(token=token):
            response = StorageController().sync_s3_storage_controller(
                sync_storage_request
            )
            return StorageResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        raise error


@storage_router.delete(
    "/label_studio/delete_s3_storage", response_model=StorageDeleteResponse
)
def delete_s3_storage(
    delete_storage_request: Storage, token: str = Depends(oauth2_scheme)
):
    """[summary]

    Args:
        delete_storage_request (Storage): [description]
        token (str, optional): [description]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [description]
        error: [description]

    Returns:
        [type]: [description]
    """
    try:
        if decodeJWT(token=token):
            response = StorageController().delete_s3_storage_controller(
                delete_storage_request
            )
            return StorageDeleteResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        raise error


@storage_router.post(
    "/label_studio/create_gcs_storage", response_model=CreateGCSStorageResponse
)
def create_gcs_storage(
    create_storage_request: CreateGCSStorage, token: str = Depends(oauth2_scheme)
):
    """[summary]

    Args:
        create_storage_request (CreateGCSStorage): [description]
        token (str, optional): [description]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [description]
        error: [description]

    Returns:
        [type]: [description]
    """
    try:
        if decodeJWT(token=token):
            response = StorageController().create_gcs_storage_controller(
                create_storage_request
            )
            return CreateGCSStorageResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        raise error


@storage_router.post(
    "/label_studio/sync_gcs_storage", response_model=CreateGCSStorageResponse
)
async def sync_gcs_storage(
    sync_storage_request: Storage, token: str = Depends(oauth2_scheme)
):
    """[summary]

    Args:
        sync_storage_request (Storage): [description]
        token (str, optional): [description]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [description]
        error: [description]

    Returns:
        [type]: [description]
    """
    try:
        if decodeJWT(token=token):
            response = StorageController().sync_gcs_storage_controller(
                sync_storage_request
            )
            return CreateGCSStorageResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        raise error


@storage_router.delete(
    "/label_studio/delete_gcs_storage", response_model=StorageDeleteResponse
)
def delete_gcs_storage(
    delete_storage_request: Storage, token: str = Depends(oauth2_scheme)
):
    """[summary]

    Args:
        delete_storage_request (Storage): [description]
        token (str, optional): [description]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [description]
        error: [description]

    Returns:
        [type]: [description]
    """
    try:
        if decodeJWT(token=token):
            response = StorageController().delete_gcs_storage_controller(
                delete_storage_request
            )
            return StorageDeleteResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        raise error
