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

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")

manage_model_router = APIRouter()


@manage_model_router.post(
    "/gcp/automl/deploy_model", response_model=ManageModelResponse
)
def deploy_model(
    deploy_model_request: ManageModel,
    token: str = Depends(oauth2_scheme),
):
    """[summary]

    Args:
        deploy_model_request (ManageModel): [description]
        token (str, optional): [description]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [description]
        error: [description]

    Returns:
        [type]: [description]
    """
    try:
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
        raise error


@manage_model_router.post(
    "/gcp/automl/undeploy_model", response_model=ManageModelResponse
)
def undeploy_model(
    undeploy_model_request: ManageModel,
    token: str = Depends(oauth2_scheme),
):
    """[summary]

    Args:
        undeploy_model_request (ManageModel): [description]
        token (str, optional): [description]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [description]
        error: [description]

    Returns:
        [type]: [description]
    """
    try:
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
        raise error


@manage_model_router.post("/gcp/automl/list_models")
def list_models(
    list_models_request: ListModels,
    token: str = Depends(oauth2_scheme),
):
    """[summary]

    Args:
        list_models_request (ListModels): [description]
        token (str, optional): [description]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [description]
        error: [description]

    Returns:
        [type]: [description]
    """
    try:
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
        raise error


@manage_model_router.post("/gcp/automl/get_model_description")
def get_model_description(
    get_model_description_request: DescriptionModels,
    token: str = Depends(oauth2_scheme),
):
    """[summary]

    Args:
        get_model_description_request (DescriptionModels): [description]
        token (str, optional): [description]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [description]
        error: [description]

    Returns:
        [type]: [description]
    """
    try:
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
        raise error


@manage_model_router.post(
    "/gcp/automl/delete_model", response_model=ManageModelResponse
)
def delete_model(
    delete_model_request: DeleteModels,
    token: str = Depends(oauth2_scheme),
):
    """[summary]

    Args:
        delete_model_request (DeleteModels): [description]
        token (str, optional): [description]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [description]
        error: [description]

    Returns:
        [type]: [description]
    """
    try:
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
        raise error
