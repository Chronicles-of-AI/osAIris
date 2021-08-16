import logging
from fastapi import APIRouter, Depends, HTTPException, status
from typing import List, Optional
from sql.apis.schemas.requests.aws.project_request import (
    CreateProject,
    DeleteProject,
)
from sql.apis.schemas.responses.aws.project_response import (
    CreateProjectResponse,
    DeleteProjectResponse,
)
from sql.controllers.aws.project_controller import ProjectController
from fastapi.security import OAuth2PasswordBearer
from commons.auth import decodeJWT
from sql import logger

logging = logger(__name__)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")
project_router = APIRouter()


@project_router.post("/aws/rekog/create_project", response_model=CreateProjectResponse)
async def create_project(
    create_project_request: CreateProject, token: str = Depends(oauth2_scheme)
):
    """[API router to create project on AWS Rekognition]

    Args:
        create_project_request (CreateProject): [AWS Rekognition create project request]
        token (str, optional): [Bearer token for authentication]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized exception when invalid token is passed]
        error: [Exception in underlying controller]

    Returns:
        [CreateProjectResponse]: [AWS Rekognition create project response]
    """
    try:
        logging.info("Calling /aws/rekog/create_project endpoint")
        logging.debug(f"Request: {create_project_request}")
        if decodeJWT(token=token):
            response = ProjectController().create_project(
                request=create_project_request
            )
            return CreateProjectResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /aws/rekog/create_project endpoint: {error}")
        raise error


@project_router.post("/aws/rekog/delete_project", response_model=DeleteProjectResponse)
async def delete_project(
    delete_project_request: DeleteProject, token: str = Depends(oauth2_scheme)
):
    """[API router to delete project on AWS Rekognition]

    Args:
        delete_project_request (DeleteProject): [AWS Rekognition create project request]
        token (str, optional): [Bearer token for authentication]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized exception when invalid token is passed]
        error: [Exception in underlying controller]

    Returns:
        [DeleteProjectResponse]: [AWS Rekognition delete project response]
    """
    try:
        logging.info("Calling /aws/rekog/delete_project endpoint")
        logging.debug(f"Request: {delete_project_request}")
        if decodeJWT(token=token):
            response = ProjectController().delete_project(
                request=delete_project_request
            )
            return DeleteProjectResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /aws/rekog/delete_project endpoint: {error}")
        raise error


@project_router.get("/aws/rekog/get_all_projects")
async def get_all_projects(token: str = Depends(oauth2_scheme)):
    """[API router to get all AWS Rekognition projects]

    Args:
        token (str, optional): [Bearer token for authentication]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized exception when invalid token is passed]
        error: [Exception in underlying controller]

    Returns:
        [dict]: [List of all AWS Rekognition projects]
    """
    try:
        logging.info("Calling /aws/rekog/get_all_projects endpoint")
        if decodeJWT(token=token):
            response = ProjectController().get_all_projects()
            return response
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /aws/rekog/get_all_projects endpoint: {error}")
        raise error


@project_router.get("/aws/rekog/get_project_description")
async def get_project_status(
    project_arn: str,
    version_names: Optional[str] = None,
    token: str = Depends(oauth2_scheme),
):
    """[API router to get AWS Rekognition project description]

    Args:
        project_arn (str): [Unique identifier for AWS Rekognition project]
        version_names (Optional[str], optional): [Unique identifier for AWS Rekognition project version]. Defaults to None.
        token (str, optional): [Bearer token for authentication]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized exception when invalid token is passed]
        error: [Exception in underlying controller]

    Returns:
        [dict]: [AWS Rekognition project description]
    """
    try:
        logging.info("Calling /aws/rekog/get_project_description endpoint")
        logging.debug(f"Request: {project_arn=},{version_names=}")
        if decodeJWT(token=token):
            response = ProjectController().get_project_description(
                project_arn=project_arn, version_names=version_names
            )
            return response
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /aws/rekog/get_project_description endpoint: {error}")
        raise error
