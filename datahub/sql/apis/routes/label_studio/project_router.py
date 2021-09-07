from fastapi import APIRouter, Depends, HTTPException, status
from sql.apis.schemas.requests.label_studio.project_request import (
    CreateProject,
    Project,
    TransformAnnotation,
)
from sql.controllers.label_studio.label_studio_controller import ProjectController
from sql.apis.schemas.responses.label_studio.project_response import (
    CreateProjectResponse,
    ProjectResponse,
    ExportAnnotationResponse,
    TransformAnnotationResponse,
)
from fastapi.security import OAuth2PasswordBearer
from commons.auth import decodeJWT
from sql import logger

logging = logger(__name__)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")
project_router = APIRouter()


@project_router.post(
    "/label_studio/create_project", response_model=CreateProjectResponse
)
async def create_project(
    create_project_request: CreateProject, token: str = Depends(oauth2_scheme)
):
    """[API router to create label studio project]

    Args:
        create_project_request (CreateProject): [Create label studio project request]
        token (str, optional): [Bearer token for authentication]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized exception when invalid token is passed]
        error: [Exception in underlying controller]

    Returns:
        [CreateProjectResponse]: [Label studio created project details]
    """
    try:
        logging.info("Calling /label_studio/create_project endpoint")
        logging.debug(f"Request: {create_project_request}")
        if decodeJWT(token=token):
            response = ProjectController().create_project_controller(
                create_project_request
            )
            # return CreateProjectResponse(**response)
            return response
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /label_studio/create_project endpoint: {error}")
        raise error


@project_router.delete("/label_studio/delete_project", response_model=ProjectResponse)
async def delete_project(
    delete_project_request: Project, token: str = Depends(oauth2_scheme)
):
    """[API router to delte label studio project]

    Args:
        delete_project_request (Project): [Delete label studio project request]
        token (str, optional): [Bearer token for authentication]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized exception when invalid token is passed]
        error: [Exception in underlying controller]

    Returns:
        [ProjectResponse]: [Label studio deleted project details]
    """
    try:
        logging.info("Calling /label_studio/delete_project endpoint")
        logging.debug(f"Request: {delete_project_request}")
        if decodeJWT(token=token):
            response = ProjectController().delete_project_controller(
                delete_project_request
            )
            return ProjectResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /label_studio/delete_project endpoint: {error}")
        raise error


@project_router.get(
    "/label_studio/export_annotations", response_model=ExportAnnotationResponse
)
async def export_annotations(
    project_id: int,
    pipeline_id: int,
    service_provider: str,
    bucket_name: str,
    token: str = Depends(oauth2_scheme),
):
    """[API router to export annotated data from label studio project]

    Args:
        project_id (int): [Label studio project id]
        service_provider (str): [Cloud service provided (AWS or GCP)]
        bucket_name (str): [Cloud bucket name to store the annotation file]
        token (str, optional): [Bearer token for authentication]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized exception when invalid token is passed]
        error: [Exception in underlying controller]

    Returns:
        [ExportAnnotationResponse]: [Exported annotation cloud URI]
    """
    try:
        logging.info("Calling /label_studio/export_annotations endpoint")
        logging.debug(f"Request: {project_id=},{service_provider=},{bucket_name=}")
        if decodeJWT(token=token):
            response = ProjectController().export_annotations_controller(
                project_id=project_id,
                service_provider=service_provider,
                bucket_name=bucket_name,
                pipeline_id=pipeline_id,
            )
            return ExportAnnotationResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /label_studio/export_annotations endpoint: {error}")
        raise error


@project_router.post(
    "/label_studio/transform_annotations", response_model=TransformAnnotationResponse
)
async def transform_annotations(
    transform_annotation_request: TransformAnnotation,
    token: str = Depends(oauth2_scheme),
):
    """[API router to transform the exported annotation as per requirement]

    Args:
        transform_annotation_request (TransformAnnotation): [Transform annotation request]
        token (str, optional): [Bearer token for authentication]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized exception when invalid token is passed]
        error: [Exception in underlying controller]

    Returns:
        [TransformAnnotationResponse]: [Transformed annotation cloud URI]
    """
    try:
        logging.info("Calling /label_studio/transform_annotations endpoint")
        logging.debug(f"Request: {transform_annotation_request}")
        if decodeJWT(token=token):
            response = ProjectController().transform_annotations_controller(
                transform_annotation_request
            )
            return TransformAnnotationResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /label_studio/transform_annotations endpoint: {error}")
        raise error
