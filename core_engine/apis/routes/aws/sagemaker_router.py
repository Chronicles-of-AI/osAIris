from fastapi import APIRouter
from apis.schemas.requests.aws.sagemaker_request import (
    CreateTrainingJob,
    TrainingJob,
)
from apis.schemas.response.aws.sagemaker_response import TrainingJobResponse
from controllers.aws.sagemaker_controller import SagemakerController
from core_engine import logger

logging = logger(__name__)

sagemaker_router = APIRouter()


@sagemaker_router.post(
    "/aws/sagemaker/start_training_job", response_model=TrainingJobResponse
)
def start_training_job(create_training_job_request: CreateTrainingJob):
    """[Start a Training Job in AWs SageMaker]

    Args:
        create_training_job_request (CreateTrainingJob): [Based on Input Schema]

    Raises:
        error: [Error]

    Returns:
        [type]: [Based on Response Model]
    """
    try:
        logging.info(f"Start Training Job Router: {create_training_job_request}")
        response = SagemakerController().start_training_job_controller(
            create_training_job_request
        )
        return TrainingJobResponse(**response)
    except Exception as error:
        logging.error(f"{error=}")
        raise error


@sagemaker_router.post("/aws/sagemaker/stop_training_job")
def stop_training_job(stop_training_job_request: TrainingJob):
    """[Stop a Training Job in AWs SageMaker]

    Args:
        stop_training_job_request (TrainingJob): [Based on Input Schema]

    Raises:
        error: [Error]

    Returns:
        [type]: [Based on Response Model]
    """
    try:
        logging.info(f"Stop Training Job Router: {stop_training_job_request}")
        return SagemakerController().stop_training_job_controller(
            stop_training_job_request
        )
    except Exception as error:
        logging.error(f"{error=}")
        raise error


# TODO: Add response schema
@sagemaker_router.post("/aws/sagemaker/describe_training_job")
def describe_training_job(describe_training_job_request: TrainingJob):
    """[Describe a Training Job in AWs SageMaker]

    Args:
        describe_training_job_request (TrainingJob): [Based on Input Schema]

    Raises:
        error: [Error]

    Returns:
        [type]: [Based on Response Model]
    """
    try:
        logging.info(f"Describe Training Job Router: {describe_training_job_request}")
        return SagemakerController().describe_training_job_controller(
            describe_training_job_request
        )
    except Exception as error:
        logging.error(f"{error=}")
        raise error


@sagemaker_router.get("/aws/sagemaker/list_training_job")
def list_training_job():
    """[List Training Jobs in AWs SageMaker]

    Raises:
        error: [Error]

    Returns:
        [type]: [Based on Response Model]
    """
    try:
        logging.info(f"List Training Job Router")
        response = SagemakerController().list_training_job_controller()
        return response
    except Exception as error:
        logging.error(f"{error=}")
        raise error
