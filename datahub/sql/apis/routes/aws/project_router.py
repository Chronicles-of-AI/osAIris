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

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")
project_router = APIRouter()


@project_router.post("/aws/rekog/create_project", response_model=CreateProjectResponse)
def create_project(
    create_project_request: CreateProject, token: str = Depends(oauth2_scheme)
):
    """[summary]

    Args:
        create_project_request (CreateProject): [description]
        token (str, optional): [description]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [description]
        error: [description]

    Returns:
        [type]: [description]
    """
    try:
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
        raise error


@project_router.post("/aws/rekog/delete_project", response_model=DeleteProjectResponse)
def delete_project(
    delete_project_request: DeleteProject, token: str = Depends(oauth2_scheme)
):
    """[summary]

    Args:
        delete_project_request (DeleteProject): [description]
        token (str, optional): [description]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [description]
        error: [description]

    Returns:
        [type]: [description]
    """
    try:
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
        raise error


@project_router.get("/aws/rekog/get_all_projects")
def get_all_projects(token: str = Depends(oauth2_scheme)):
    """[summary]

    Args:
        token (str, optional): [description]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [description]
        error: [description]

    Returns:
        [type]: [description]
    """
    try:
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
        raise error


@project_router.get("/aws/rekog/get_project_description")
def get_project_status(
    project_arn: str,
    version_names: Optional[str] = None,
    token: str = Depends(oauth2_scheme),
):
    """[summary]

    Args:
        project_arn (str): [description]
        version_names (Optional[str], optional): [description]. Defaults to None.
        token (str, optional): [description]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [description]
        error: [description]

    Returns:
        [type]: [description]
    """
    try:
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
        raise error
