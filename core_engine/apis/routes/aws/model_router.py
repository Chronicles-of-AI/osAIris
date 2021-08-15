from fastapi import APIRouter
from typing import Optional

from starlette import responses
from apis.schemas.requests.aws.model_request import (
    DeployModel,
    UndeployModel,
    DeleteModel,
    StartTraining,
)
from apis.schemas.response.aws.model_response import StartTrainingResponse, ModelStatus
from controllers.aws.model_controller import ModelController
from core_engine import logger

logging = logger(__name__)

model_router = APIRouter()


@model_router.post("/aws/rekog/start_training", response_model=StartTrainingResponse)
def start_training(start_training_request: StartTraining):
    """[Train a Model in AWS]

    Args:
        start_training_request (StartTraining): [Based on Input Schema]

    Raises:
        error: [Error]

    Returns:
        [type]: [Based on Response Model]
    """
    try:
        logging.info(f"Start Training Router: {start_training_request}")
        response = ModelController().train_model_controller(start_training_request)
        return StartTrainingResponse(**response)
    except Exception as error:
        logging.error(f"{error=}")
        raise error


@model_router.post("/aws/rekog/deploy_model", response_model=ModelStatus)
def deploy_model(deploy_model_request: DeployModel):
    """[Deploy a Model in AWS]

    Args:
        deploy_model_request (DeployModel): [Based on Input Schema]

    Raises:
        error: [Error]

    Returns:
        [type]: [Based on Response Model]
    """
    try:
        logging.info(f"Deploy Model Router: {deploy_model_request}")
        response = ModelController().deploy_model_controller(deploy_model_request)
        return ModelStatus(**response)
    except Exception as error:
        logging.error(f"{error=}")
        raise error


@model_router.post("/aws/rekog/undeploy_model", response_model=ModelStatus)
def undeploy_model(undeploy_model_request: UndeployModel):
    """[Un-Deploy a Model in AWS]

    Args:
        undeploy_model_request (UndeployModel): [Based on Input Schema]

    Raises:
        error: [Error]

    Returns:
        [type]: [Based on Response Model]
    """
    try:
        logging.info(f"Un-Deploy Model Router: {undeploy_model_request}")
        response = ModelController().undeploy_model_controller(undeploy_model_request)
        return ModelStatus(**response)
    except Exception as error:
        logging.error(f"{error=}")
        raise error


@model_router.post("/aws/rekog/delete_model", response_model=ModelStatus)
def delete_model(delete_model_request: DeleteModel):
    """[Delete a Model in AWS]

    Args:
        delete_model_request (DeleteModel): [Based on Input Schema]

    Raises:
        error: [Error]

    Returns:
        [type]: [Based on Response Model]
    """
    try:
        logging.info(f"Delete Model Router: {delete_model_request}")
        response = ModelController().delete_model_controller(delete_model_request)
        return ModelStatus(**response)
    except Exception as error:
        logging.error(f"{error=}")
        raise error


@model_router.get("/aws/rekog/get_model_evaluation")
def get_model_evaluation(project_arn: str, version_name: Optional[str] = None):
    """[Get Evaluations of a Model in AWS]

    Args:
        project_arn (str): [Unique Identifier for your Project]
        version_name (Optional[str], optional): [Version Name in AWS]. Defaults to None.

    Raises:
        error: [Error]

    Returns:
        [type]: [Based on Response Model]
    """
    try:
        logging.info(f"Get Model Evaluation Router: {project_arn}")
        response = ModelController().get_evaluation_controller(
            project_arn=project_arn, version_name=version_name
        )
        return response
    except Exception as error:
        logging.error(f"{error=}")
        raise error


@model_router.get("/aws/rekog/get_model_manifest")
def get_model_manifest(project_arn: str, version_name: Optional[str] = None):
    """[Get Manifest of a Model in AWS]

    Args:
        project_arn (str): [Unique Identifier for your Project]
        version_name (Optional[str], optional): [Version Name in AWS]. Defaults to None.

    Raises:
        error: [Error]

    Returns:
        [type]: [Based on Response Model]
    """
    try:
        logging.info(f"Get Model Manifest Router: {project_arn}")
        response = ModelController().get_manifest_controller(
            project_arn=project_arn, version_name=version_name
        )
        return response
    except Exception as error:
        logging.error(f"{error=}")
        raise error


@model_router.get("/aws/rekog/get_predictions")
def get_predictions(
    project_version_arn: str, s3_uri: str, confidence_threshold: int = 50
):
    """[Get Predictions from a Model in AWS]

    Args:
        project_version_arn (str): [Unique Identifier for your Project Version]
        s3_uri (str): [Input Data Path]
        confidence_threshold (int, optional): [Confidence Threshold]. Defaults to 50.

    Raises:
        error: [Error]

    Returns:
        [type]: [Based on Response Model]
    """
    try:
        logging.info(f"Get Predictions Router: {project_version_arn}")
        return ModelController().get_predictions_controller(
            project_version_arn=project_version_arn,
            s3_uri=s3_uri,
            confidence_threshold=confidence_threshold,
        )
    except Exception as error:
        logging.error(f"{error=}")
        raise error
