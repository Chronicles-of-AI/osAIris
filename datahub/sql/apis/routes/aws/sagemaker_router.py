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

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")
sagemaker_router = APIRouter()


@sagemaker_router.post(
    "/aws/sagemaker/start_training_job", response_model=TrainingJobResponse
)
def start_training_job(
    create_training_job_request: CreateTrainingJob, token: str = Depends(oauth2_scheme)
):
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


@sagemaker_router.post(
    "/aws/sagemaker/stop_training_job", response_model=TrainingStatus
)
def stop_training_job(
    stop_training_job_request: TrainingJob, token: str = Depends(oauth2_scheme)
):
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


@sagemaker_router.post("/aws/sagemaker/describe_training_job")
def describe_training_job(
    describe_training_job_request: TrainingJob, token: str = Depends(oauth2_scheme)
):
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


@sagemaker_router.get("/aws/sagemaker/list_training_job")
def list_training_job(token: str = Depends(oauth2_scheme)):
    if decodeJWT(token=token):
        response = SagemakerController().list_training_job_controller()
        return response
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid access token",
            headers={"WWW-Authenticate": "Bearer"},
        )
