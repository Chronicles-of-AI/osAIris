from fastapi import APIRouter, Depends, HTTPException, status
from typing import Optional
from sql.apis.schemas.requests.aws.model_request import (
    StartTraining,
    DeployModel,
    UndeployModel,
    DeleteModel,
)
from sql.apis.schemas.responses.aws.model_response import ModelStatus
from sql.controllers.aws.model_controller import ModelController
from fastapi.security import OAuth2PasswordBearer
from commons.auth import decodeJWT

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")
model_router = APIRouter()


@model_router.post("/aws/rekog/start_training", response_model=ModelStatus)
def start_training(
    start_training_request: StartTraining, token: str = Depends(oauth2_scheme)
):
    """[summary]

    Args:
        start_training_request (StartTraining): [description]
        token (str, optional): [description]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [description]
        error: [description]

    Returns:
        [type]: [description]
    """
    try:
        if decodeJWT(token=token):
            response = ModelController().train_model_controller(start_training_request)
            return ModelStatus(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        raise error


@model_router.post("/aws/rekog/deploy_model", response_model=ModelStatus)
def deploy_model(
    deploy_model_request: DeployModel, token: str = Depends(oauth2_scheme)
):
    """[summary]

    Args:
        deploy_model_request (DeployModel): [description]
        token (str, optional): [description]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [description]
        error: [description]

    Returns:
        [type]: [description]
    """
    try:
        if decodeJWT(token=token):
            response = ModelController().deploy_model_controller(deploy_model_request)
            return ModelStatus(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        raise error


@model_router.post("/aws/rekog/undeploy_model", response_model=ModelStatus)
def undeploy_model(
    undeploy_model_request: UndeployModel, token: str = Depends(oauth2_scheme)
):
    """[summary]

    Args:
        undeploy_model_request (UndeployModel): [description]
        token (str, optional): [description]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [description]
        error: [description]

    Returns:
        [type]: [description]
    """
    try:
        if decodeJWT(token=token):
            response = ModelController().undeploy_model_controller(
                undeploy_model_request
            )
            return ModelStatus(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        raise error


@model_router.post("/aws/rekog/delete_model", response_model=ModelStatus)
def delete_model(
    delete_model_request: DeleteModel, token: str = Depends(oauth2_scheme)
):
    """[summary]

    Args:
        delete_model_request (DeleteModel): [description]
        token (str, optional): [description]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [description]
        error: [description]

    Returns:
        [type]: [description]
    """
    try:
        if decodeJWT(token=token):
            response = ModelController().delete_model_controller(delete_model_request)
            return ModelStatus(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        raise error


@model_router.get("/aws/rekog/get_model_evaluation")
def get_model_evaluation(
    project_arn: str,
    version_name: Optional[str] = None,
    token: str = Depends(oauth2_scheme),
):
    """[summary]

    Args:
        project_arn (str): [description]
        version_name (Optional[str], optional): [description]. Defaults to None.
        token (str, optional): [description]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [description]
        error: [description]

    Returns:
        [type]: [description]
    """
    try:
        if decodeJWT(token=token):
            response = ModelController().get_evaluation_controller(
                project_arn=project_arn, version_name=version_name
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


@model_router.get("/aws/rekog/get_model_manifest")
def get_model_manifest(
    project_arn: str,
    version_name: Optional[str] = None,
    token: str = Depends(oauth2_scheme),
):
    """[summary]

    Args:
        project_arn (str): [description]
        version_name (Optional[str], optional): [description]. Defaults to None.
        token (str, optional): [description]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [description]
        error: [description]

    Returns:
        [type]: [description]
    """
    try:
        if decodeJWT(token=token):
            response = ModelController().get_manifest_controller(
                project_arn=project_arn, version_name=version_name
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


@model_router.get("/aws/rekog/get_predictions")
def get_predictions(
    project_version_arn: str,
    s3_uri: str,
    confidence_threshold: int = 50,
    token: str = Depends(oauth2_scheme),
):
    """[summary]

    Args:
        project_version_arn (str): [description]
        s3_uri (str): [description]
        confidence_threshold (int, optional): [description]. Defaults to 50.
        token (str, optional): [description]. Defaults to Depends(oauth2_scheme).

    Raises:
        error: [description]

    Returns:
        [type]: [description]
    """
    try:
        return ModelController().get_predictions_controller(
            project_version_arn=project_version_arn,
            s3_uri=s3_uri,
            confidence_threshold=confidence_threshold,
        )
    except Exception as error:
        raise error
