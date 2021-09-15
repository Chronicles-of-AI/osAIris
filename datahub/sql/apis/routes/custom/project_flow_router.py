from fastapi import APIRouter, Depends, HTTPException, status
from sql.apis.schemas.requests.custom.project_flow_request import (
    CreateProjectFlow,
    GetProjectFlow,
)
from sql.apis.schemas.responses.custom.project_flow_response import (
    CreateProjectFlowResponse,
    ProjectFlowResponse,
    AllProjectFlowResponse,
)
from sql.controllers.custom.project_flow_controller import ProjectFlowController
from fastapi.security import OAuth2PasswordBearer
from commons.auth import decodeJWT
from sql import logger

logging = logger(__name__)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")
project_flow_router = APIRouter()


@project_flow_router.post(
    "/osairis/project_flow/create",
    response_model=CreateProjectFlowResponse,
)
async def create_project_flow(
    create_project_flow_request: CreateProjectFlow,
    token: str = Depends(oauth2_scheme),
):
    """[API Router to Create a Project Flow]

    Args:
        create_project_flow_request (CreateProjectFlow): [Based on the Input Schema]
        token (str, optional): [description]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Exception]
        error: [Error]

    Returns:
        [type]: [Basedon Output Response]
    """
    try:
        logging.info("Calling /osairis/project_flow/create endpoint")
        logging.debug(f"Request: {create_project_flow_request}")
        if decodeJWT(token=token):
            response = ProjectFlowController().create_project_flow_controller(
                request=create_project_flow_request
            )
            return CreateProjectFlowResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /osairis/project_flow/create endpoint: {error}")
        raise error


@project_flow_router.get(
    "/osairis/project_flow",
)
async def get_all_project_flow(
    token: str = Depends(oauth2_scheme),
):
    """[API Router to list all Project Flows]

    Args:
        token (str, optional): [description]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Exception]
        error: [Error]

    Returns:
        [type]: [Basedon Output Response]
    """
    try:
        logging.info("Calling /osairis/project_flow endpoint")
        if decodeJWT(token=token):
            response = ProjectFlowController().get_all_project_flow_controller()
            return response
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /osairis/project_flow endpoint: {error}")
        raise error


@project_flow_router.get(
    "/osairis/project_flow/by_id",
    response_model=ProjectFlowResponse,
)
async def get_project_flow(
    pipeline_id: str,
    token: str = Depends(oauth2_scheme),
):
    """[API Router to get a Project Flow based on pipeline ID]

    Args:
        pipeline_id (str): [Unique Identifier for every Project Flow]
        token (str, optional): [description]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Exception]
        error: [Error]

    Returns:
        [type]: [Basedon Output Response]
    """
    try:
        logging.info("Calling /osairis/project_flow/by_id endpoint")
        logging.debug(f"Request: {pipeline_id}")
        if decodeJWT(token=token):
            response = ProjectFlowController().get_project_flow_by_name_controller(
                pipeline_id=pipeline_id
            )
            return ProjectFlowResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /osairis/project_flow/by_id endpoint: {error}")
        raise error
