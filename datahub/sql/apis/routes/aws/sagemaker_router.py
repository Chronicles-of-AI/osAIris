import logging
from fastapi import APIRouter, Depends, HTTPException, status
from yaml.tokens import ValueToken
from sql.apis.schemas.requests.aws.sagemaker_request import (
    CreateTrainingJob,
    TrainingJob,
)
from sql.apis.schemas.responses.aws.sagemaker_response import (
    TrainingJobResponse,
    TrainingStatus,
)
from sql.controllers.aws.sagemaker_controller import SagemakerController
from fastapi.security import OAuth2PasswordBearer
from commons.auth import decodeJWT
from sql import logger

logging = logger(__name__)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")
sagemaker_router = APIRouter()


@sagemaker_router.post(
    "/aws/sagemaker/start_training_job", response_model=TrainingJobResponse
)
def start_training_job(
    create_training_job_request: CreateTrainingJob, token: str = Depends(oauth2_scheme)
):
    """[API router to start training job on AWS Sagemaker]

    Args:
        create_training_job_request (CreateTrainingJob): [AWS Sagemaker start training job request]
        token (str, optional): [Bearer token for authentication]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized exception when invalid token is passed]
        error: [Exception in underlying controller]

    Returns:
        [dict]: [AWS Sagemaker start training response]
    """
    try:
        logging.info("Calling /aws/sagemaker/start_training_job endpoint")
        logging.debug(f"Request: {create_training_job_request}")
        if decodeJWT(token=token):
            response = SagemakerController().start_training_job_controller(
                create_training_job_request
            )
            return TrainingJobResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /aws/sagemaker/start_training_job endpoint: {error}")
        raise error


@sagemaker_router.post(
    "/aws/sagemaker/stop_training_job", response_model=TrainingStatus
)
def stop_training_job(
    stop_training_job_request: TrainingJob, token: str = Depends(oauth2_scheme)
):
    """[API router to stop training job on AWS Sagemaker]

    Args:
        stop_training_job_request (TrainingJob): [AWS Sagemaker stop training job request]
        token (str, optional): [Bearer token for authentication]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized exception when invalid token is passed]
        error: [Exception in underlying controller]

    Returns:
        [dict]: [AWS Sagemaker stop training response]
    """
    try:
        logging.info("Calling /aws/sagemaker/stop_training_job endpoint")
        logging.debug(f"Request: {stop_training_job_request}")
        if decodeJWT(token=token):
            response = SagemakerController().stop_training_job_controller(
                stop_training_job_request
            )
            return TrainingStatus(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /aws/sagemaker/stop_training_job endpoint: {error}")
        raise error


@sagemaker_router.post("/aws/sagemaker/describe_training_job")
def describe_training_job(
    describe_training_job_request: TrainingJob, token: str = Depends(oauth2_scheme)
):
    """[API router to describe a training job on AWS Sagemaker]

    Args:
        describe_training_job_request (TrainingJob): [AWS Sagemaker describe training job request]
        token (str, optional): [Bearer token for authentication]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized exception when invalid token is passed]
        error: [Exception in underlying controller]

    Returns:
        [dict]: [AWS Sagemaker describe training job response]
    """
    try:
        logging.info("Calling /aws/sagemaker/describe_training_job endpoint")
        logging.debug(f"Request: {describe_training_job_request}")
        if decodeJWT(token=token):
            response = SagemakerController().describe_training_job_controller(
                describe_training_job_request
            )
            return TrainingStatus(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(
            f"Error in /aws/sagemaker/describe_training_job endpoint: {error}"
        )
        raise error


@sagemaker_router.get("/aws/sagemaker/list_training_job")
def list_training_job(token: str = Depends(oauth2_scheme)):
    """[API router to list all the training jobs on AWS Sagemaker]

    Args:
        token (str, optional): [Bearer token for authentication]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized exception when invalid token is passed]
        error: [Exception in underlying controller]

    Returns:
        [dict]: [AWS Sagemaker list of all training jobs]
    """
    try:
        logging.info("Calling /aws/sagemaker/list_training_job endpoint")
        if decodeJWT(token=token):
            response = SagemakerController().list_training_job_controller()
            return response
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /aws/sagemaker/list_training_job endpoint: {error}")
        raise error
