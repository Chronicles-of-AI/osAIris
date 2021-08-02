from fastapi import APIRouter
from apis.schemas.requests.aws.sagemaker_request import (
    CreateTrainingJob,
    TrainingJob,
)
from apis.schemas.response.aws.sagemaker_response import TrainingJobResponse
from controllers.aws.sagemaker_controller import SagemakerController

sagemaker_router = APIRouter()


@sagemaker_router.post(
    "/aws/sagemaker/start_training_job", response_model=TrainingJobResponse
)
def start_training_job(create_training_job_request: CreateTrainingJob):
    response = SagemakerController().start_training_job_controller(
        create_training_job_request
    )
    return TrainingJobResponse(**response)


@sagemaker_router.post("/aws/sagemaker/stop_training_job")
def stop_training_job(stop_training_job_request: TrainingJob):
    return SagemakerController().stop_training_job_controller(stop_training_job_request)


# TODO: Add response schema
@sagemaker_router.post("/aws/sagemaker/describe_training_job")
def describe_training_job(describe_training_job_request: TrainingJob):
    return SagemakerController().describe_training_job_controller(
        describe_training_job_request
    )


@sagemaker_router.get("/aws/sagemaker/list_training_job")
def list_training_job():
    response = SagemakerController().list_training_job_controller()
    return response
