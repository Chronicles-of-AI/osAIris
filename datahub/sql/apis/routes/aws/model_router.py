import logging
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
from sql import logger

logging = logger(__name__)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")
model_router = APIRouter()


@model_router.post("/aws/rekog/start_training", response_model=ModelStatus)
async def start_training(
    start_training_request: StartTraining, token: str = Depends(oauth2_scheme)
):
    """[API router to start training on AWS Rekognition]

    Args:
        start_training_request (StartTraining): [start training on AWS rekognition]
        token (str, optional): [Bearer token for authentication]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized exception when invalid token is passed]
        error: [Exception in underlying controller]

    Returns:
        [ModelStatus]: [Start Training response from AWS Rekognition]
    """
    try:
        logging.info("Calling /aws/rekog/start_training endpoint")
        logging.debug(f"Request: {start_training_request}")
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
        logging.error(f"Error in /aws/rekog/start_training endpoint: {error}")
        raise error


@model_router.post("/aws/rekog/deploy_model", response_model=ModelStatus)
async def deploy_model(
    deploy_model_request: DeployModel, token: str = Depends(oauth2_scheme)
):
    """[API router to deploy trained AWS Rekognition model]

    Args:
        deploy_model_request (DeployModel): [deploy AWS rekognition trained model]
        token (str, optional): [Bearer token for authentication]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized exception when invalid token is passed]
        error: [Exception in underlying controller]

    Returns:
        [ModelStatus]: [Deploy model response from AWS Rekognition]
    """
    try:
        logging.info("Calling /aws/rekog/deploy_model endpoint")
        logging.debug(f"Request: {deploy_model_request}")
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
        logging.error(f"Error in /aws/rekog/deploy_model endpoint: {error}")
        raise error


@model_router.post("/aws/rekog/undeploy_model", response_model=ModelStatus)
async def undeploy_model(
    undeploy_model_request: UndeployModel, token: str = Depends(oauth2_scheme)
):
    """[API router to un-deploy trained AWS Rekognition model]

    Args:
        undeploy_model_request (UndeployModel): [un-deploy AWS rekognition trained model]
        token (str, optional): [Bearer token for authentication]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized exception when invalid token is passed]
        error: [Exception in underlying controller]

    Returns:
        [ModelStatus]: [Un-Deploy model response from AWS Rekognition]
    """
    try:
        logging.info("Calling /aws/rekog/undeploy_model endpoint")
        logging.debug(f"Request: {undeploy_model_request}")
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
        logging.error(f"Error in /aws/rekog/undeploy_model endpoint: {error}")
        raise error


@model_router.post("/aws/rekog/delete_model", response_model=ModelStatus)
async def delete_model(
    delete_model_request: DeleteModel, token: str = Depends(oauth2_scheme)
):
    """[API router to delete trained AWS Rekognition model]

    Args:
        delete_model_request (DeleteModel): [Delete AWS rekognition trained model]
        token (str, optional): [Bearer token for authentication]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized exception when invalid token is passed]
        error: [Exception in underlying controller]

    Returns:
        [ModelStatus]: [Delete model response from AWS Rekognition]
    """
    try:
        logging.info("Calling /aws/rekog/delete_model endpoint")
        logging.debug(f"Request: {delete_model_request}")
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
        logging.error(f"Error in /aws/rekog/delete_model endpoint: {error}")
        raise error


@model_router.get("/aws/rekog/get_model_status")
async def get_model_status(
    project_arn: str,
    version_name: Optional[str] = None,
    token: str = Depends(oauth2_scheme),
):
    """[API router to get status for AWS Rekognition model]

    Args:
        project_arn (str): [Unique identifier for AWS Rekognition project]
        version_name (str, optional): [Unique identifier for AWS Rekognition model version]
        token (str, optional): [Bearer token for authentication]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized exception when invalid token is passed]
        error: [Exception in underlying controller]

    Returns:
        [dict]: [Status of model]
    """
    try:
        logging.info("Calling /aws/rekog/get_model_status endpoint")
        logging.debug(f"Request: {project_arn=},{version_name=}")
        if decodeJWT(token=token):
            response = ModelController().get_model_status(
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
        logging.error(f"Error in /aws/rekog/get_model_status endpoint: {error}")
        raise error


@model_router.get("/aws/rekog/get_model_evaluation")
async def get_model_evaluation(
    project_arn: str,
    version_name: Optional[str] = None,
    token: str = Depends(oauth2_scheme),
):
    """[API router to get evaluation matrix for AWS Rekognition model]

    Args:
        project_arn (str): [Unique identifier for AWS Rekognition project]
        version_name (str, optional): [Unique identifier for AWS Rekognition model version]
        token (str, optional): [Bearer token for authentication]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized exception when invalid token is passed]
        error: [Exception in underlying controller]

    Returns:
        [dict]: [evaluation matrix for deployed model]
    """
    try:
        logging.info("Calling /aws/rekog/get_model_evaluation endpoint")
        logging.debug(f"Request: {project_arn=},{version_name=}")
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
        logging.error(f"Error in /aws/rekog/get_model_evaluation endpoint: {error}")
        raise error


@model_router.get("/aws/rekog/get_model_manifest")
async def get_model_manifest(
    project_arn: str,
    version_name: Optional[str] = None,
    token: str = Depends(oauth2_scheme),
):
    """[API router to get model manifest details for AWS Rekognition model]

    Args:
        project_arn (str): [Unique identifier for AWS Rekognition project]
        version_name (str, optional): [Unique identifier for AWS Rekognition model version]
        token (str, optional): [Bearer token for authentication]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized exception when invalid token is passed]
        error: [Exception in underlying controller]

    Returns:
        [dict]: [model manifest details for deployed model]
    """
    try:
        logging.info("Calling /aws/rekog/get_model_manifest endpoint")
        logging.debug(f"Request: {project_arn=},{version_name=}")
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
        logging.error(f"Error in /aws/rekog/get_model_manifest endpoint: {error}")
        raise error


@model_router.get("/aws/rekog/get_predictions")
async def get_predictions(
    project_version_arn: str,
    s3_uri: str,
    confidence_threshold: int = 50,
    token: str = Depends(oauth2_scheme),
):
    """[API router to run inference on AWS Rekognition model]

    Args:
        project_version_arn (str): [Unique identifier for AWS Rekognition model]
        s3_uri (str): [S3 URI for the test image]
        confidence_threshold (int): [confidence threshold]
        token (str, optional): [Bearer token for authentication]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized exception when invalid token is passed]
        error: [Exception in underlying controller]

    Returns:
        [dict]: [inference results from deployed AWS Rekognition model]
    """
    try:
        logging.info("Calling /aws/rekog/get_predictions endpoint")
        logging.debug(
            f"Request: {project_version_arn=},{s3_uri=},{confidence_threshold=}"
        )
        return ModelController().get_predictions_controller(
            project_version_arn=project_version_arn,
            s3_uri=s3_uri,
            confidence_threshold=confidence_threshold,
        )
    except Exception as error:
        logging.error(f"Error in /aws/rekog/get_predictions endpoint: {error}")
        raise error
