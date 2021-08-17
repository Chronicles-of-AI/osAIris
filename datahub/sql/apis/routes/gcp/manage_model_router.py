from fastapi import APIRouter, Depends, HTTPException, status
from sql.apis.schemas.requests.gcp.model_management_request import (
    ManageModel,
    ListModels,
    DescriptionModels,
    DeleteModels,
)
from sql.apis.schemas.responses.gcp.model_management_response import ManageModelResponse
from sql.controllers.gcp.model_management_controller import ManageModelController
from fastapi.security import OAuth2PasswordBearer
from commons.auth import decodeJWT
from sql import logger

logging = logger(__name__)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")

manage_model_router = APIRouter()


@manage_model_router.post(
    "/gcp/automl/deploy_model", response_model=ManageModelResponse
)
async def deploy_model(
    deploy_model_request: ManageModel,
    token: str = Depends(oauth2_scheme),
):
    """[API router to deploy an AutoML model]

    Args:
        deploy_model_request (ManageModel): [AutoML model details to be deployed]
        token (str, optional): [Bearer token for authentication]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized exception when invalid token is passed]
        error: [Exception in underlying controller]

    Returns:
        [ManageModelResponse]: [AutoML model deployment response]
    """
    try:
        logging.info("Calling /gcp/automl/deploy_model endpoint")
        logging.debug(f"Request: {deploy_model_request}")
        if decodeJWT(token=token):
            response = ManageModelController().deploy_model_controller(
                request=deploy_model_request
            )
            return ManageModelResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /gcp/automl/deploy_model endpoint: {error}")
        raise error


@manage_model_router.post(
    "/gcp/automl/undeploy_model", response_model=ManageModelResponse
)
async def undeploy_model(
    undeploy_model_request: ManageModel,
    token: str = Depends(oauth2_scheme),
):
    """[API router to undeploy a AutoML model]

    Args:
        undeploy_model_request (ManageModel): [AutoML model details to be un-deployed]
        token (str, optional): [Bearer token for authentication]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized exception when invalid token is passed]
        error: [Exception in underlying controller]

    Returns:
        [ManageModelResponse]: [AutoML undeploy model response]
    """
    try:
        logging.info("Calling /gcp/automl/undeploy_model endpoint")
        logging.debug(f"Request: {undeploy_model_request}")
        if decodeJWT(token=token):
            response = ManageModelController().undeploy_model_controller(
                request=undeploy_model_request
            )
            return ManageModelResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /gcp/automl/undeploy_model endpoint: {error}")
        raise error


@manage_model_router.post("/gcp/automl/list_models")
async def list_models(
    list_models_request: ListModels,
    token: str = Depends(oauth2_scheme),
):
    """[API router to list all autoML models]

    Args:
        list_models_request (ListModels): [List all autoML model request]
        token (str, optional): [Bearer token for authentication]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized exception when invalid token is passed]
        error: [Exception in underlying controller]

    Returns:
        [dict]: [List of all the trained models]
    """
    try:
        logging.info("Calling /gcp/automl/list_models endpoint")
        logging.debug(f"Request: {list_models_request}")
        if decodeJWT(token=token):
            response = ManageModelController().list_model_controller(
                request=list_models_request
            )
            return response
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /gcp/automl/list_models endpoint: {error}")
        raise error


@manage_model_router.post("/gcp/automl/get_model_description")
async def get_model_description(
    get_model_description_request: DescriptionModels,
    token: str = Depends(oauth2_scheme),
):
    """[API router to get model description]

    Args:
        get_model_description_request (DescriptionModels): [Get AutoML model description request]
        token (str, optional): [Bearer token for authentication]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized exception when invalid token is passed]
        error: [Exception in underlying controller]

    Returns:
        [dict]: [AutoML model description]
    """
    try:
        logging.info("Calling /gcp/automl/get_model_description endpoint")
        logging.debug(f"Request: {get_model_description_request}")
        if decodeJWT(token=token):
            response = ManageModelController().get_model_description_controller(
                request=get_model_description_request
            )
            return response
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /gcp/automl/get_model_description endpoint: {error}")
        raise error


@manage_model_router.post(
    "/gcp/automl/delete_model", response_model=ManageModelResponse
)
async def delete_model(
    delete_model_request: DeleteModels,
    token: str = Depends(oauth2_scheme),
):
    """[API router to delete AutoML model]

    Args:
        delete_model_request (DeleteModels): [AutoML model delete request]
        token (str, optional): [Bearer token for authentication]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized exception when invalid token is passed]
        error: [Exception in underlying controller]

    Returns:
        [dict]: [AutoML model delete response]
    """
    try:
        logging.info("Calling /gcp/automl/delete_model endpoint")
        logging.debug(f"Request: {delete_model_request}")
        if decodeJWT(token=token):
            response = ManageModelController().delete_model_controller(
                request=delete_model_request
            )
            return ManageModelResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /gcp/automl/delete_model endpoint: {error}")
        raise error
