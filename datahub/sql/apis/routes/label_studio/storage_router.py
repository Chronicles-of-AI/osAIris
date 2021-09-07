from osAIris.datahub.sql.controllers.label_studio.label_studio_controller import (
    ProjectController,
)
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
    ListStoragesResponse,
)
from sql.controllers.label_studio.label_studio_controller import StorageController
from fastapi.security import OAuth2PasswordBearer
from commons.auth import decodeJWT
from sql import logger

logging = logger(__name__)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")
storage_router = APIRouter()


@storage_router.post(
    "/label_studio/create_s3_storage", response_model=CreateStorageResponse
)
async def create_s3_storage(
    create_storage_request: CreateStorage, token: str = Depends(oauth2_scheme)
):
    """[API router to add S3 storage to Label studio project]

    Args:
        create_storage_request (CreateStorage): [Create storage request]
        token (str, optional): [Bearer token for authentication]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized exception when invalid token is passed]
        error: [Exception in underlying controller]

    Returns:
        [CreateStorageResponse]: [Create storage response]
    """
    try:
        logging.info("Calling /label_studio/create_s3_storage endpoint")
        logging.debug(f"Request: {create_storage_request}")
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
        logging.error(f"Error in /label_studio/create_s3_storage endpoint: {error}")
        raise error


@storage_router.post("/label_studio/sync_s3_storage", response_model=StorageResponse)
async def sync_s3_storage(
    sync_storage_request: Storage, token: str = Depends(oauth2_scheme)
):
    """[API router to sync data into label studio project]

    Args:
        sync_storage_request (Storage): [Sync storage request]
        token (str, optional): [Bearer token for authentication]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized exception when invalid token is passed]
        error: [Exception in underlying controller]

    Returns:
        [StorageResponse]: [Sync storage response]
    """
    try:
        logging.info("Calling /label_studio/sync_s3_storage endpoint")
        logging.debug(f"Request: {sync_storage_request}")
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
        logging.error(f"Error in /label_studio/sync_s3_storage endpoint: {error}")
        raise error


@storage_router.delete(
    "/label_studio/delete_s3_storage", response_model=StorageDeleteResponse
)
async def delete_s3_storage(
    delete_storage_request: Storage, token: str = Depends(oauth2_scheme)
):
    """[API router to remove S3 storage from label studio project]

    Args:
        delete_storage_request (Storage): [Delete S3 storage request]
        token (str, optional): [Bearer token for authentication]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized exception when invalid token is passed]
        error: [Exception in underlying controller]

    Returns:
        [StorageDeleteResponse]: [Delete S3 storage from label studio project response]
    """
    try:
        logging.info("Calling /label_studio/delete_s3_storage endpoint")
        logging.debug(f"Request: {delete_storage_request}")
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
        logging.error(f"Error in /label_studio/delete_s3_storage endpoint: {error}")
        raise error


@storage_router.get("/label_studio/list_projects")
async def list_projects(token: str = Depends(oauth2_scheme)):
    """[API Router to list Projects attached in your Annotation Project]

    Args:
        token (str, optional): [description]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized exception when invalid token is passed]
        error: [Error]

    Returns:
        [type]: [List of Projects]
    """
    try:
        logging.info("Calling /label_studio/list_projects endpoint")
        if decodeJWT(token=token):
            response = ProjectController().list_projects_controller()
            return response
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /label_studio/list_projects endpoint: {error}")
        raise error


@storage_router.get("/label_studio/list_storages", response_model=ListStoragesResponse)
async def list_storages(project_id: int, token: str = Depends(oauth2_scheme)):
    """[API Router to list Storages attached in your Annotation Project]

    Args:
        project_id (int): [Unique Identifier for the Annotation Project]
        token (str, optional): [description]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized exception when invalid token is passed]
        error: [Error]

    Returns:
        [type]: [List of Storages]
    """
    try:
        logging.info("Calling /label_studio/list_storages endpoint")
        logging.debug(f"Request: {project_id}")
        if decodeJWT(token=token):
            response = StorageController().list_storages_controller(
                project_id=project_id
            )
            return ListStoragesResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /label_studio/list_storages endpoint: {error}")
        raise error


@storage_router.post(
    "/label_studio/create_gcs_storage", response_model=CreateGCSStorageResponse
)
async def create_gcs_storage(
    create_storage_request: CreateGCSStorage, token: str = Depends(oauth2_scheme)
):
    """[API router to add GCS storage to label studio project]

    Args:
        create_storage_request (CreateGCSStorage): [Add GCS storage to label studio project request]
        token (str, optional): [Bearer token for authentication]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized exception when invalid token is passed]
        error: [Exception in underlying controller]

    Returns:
        [CreateGCSStorageResponse]: [Add GCS storage to label studio project response]
    """
    try:
        logging.info("Calling /label_studio/create_gcs_storage endpoint")
        logging.debug(f"Request: {create_storage_request}")
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
        logging.error(f"Error in /label_studio/create_gcs_storage endpoint: {error}")
        raise error


@storage_router.post(
    "/label_studio/sync_gcs_storage", response_model=CreateGCSStorageResponse
)
async def sync_gcs_storage(
    sync_storage_request: Storage, token: str = Depends(oauth2_scheme)
):
    """[API router to sync data into label studio project]

    Args:
        sync_storage_request (Storage): [Sync storage request]
        token (str, optional): [Bearer token for authentication]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized exception when invalid token is passed]
        error: [Exception in underlying controller]

    Returns:
        [CreateGCSStorageResponse]: [Sync storage response]
    """
    try:
        logging.info("Calling /label_studio/sync_gcs_storage endpoint")
        logging.debug(f"Request: {sync_storage_request}")
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
        logging.error(f"Error in /label_studio/sync_gcs_storage endpoint: {error}")
        raise error


@storage_router.delete(
    "/label_studio/delete_gcs_storage", response_model=StorageDeleteResponse
)
async def delete_gcs_storage(
    delete_storage_request: Storage, token: str = Depends(oauth2_scheme)
):
    """[API router to remove GCS storage from label studio project]

    Args:
        delete_storage_request (Storage): [Delete GCS storage request]
        token (str, optional): [Bearer token for authentication]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized exception when invalid token is passed]
        error: [Exception in underlying controller]

    Returns:
        [StorageDeleteResponse]: [Delete GCS storage from label studio project response]
    """
    try:
        logging.info("Calling /label_studio/delete_gcs_storage endpoint")
        logging.debug(f"Request: {delete_storage_request}")
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
        logging.error(f"Error in /label_studio/delete_gcs_storage endpoint: {error}")
        raise error
