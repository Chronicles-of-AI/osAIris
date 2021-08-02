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

model_router = APIRouter()


@model_router.post("/aws/rekog/start_training", response_model=StartTrainingResponse)
def start_training(start_training_request: StartTraining):
    response = ModelController().train_model_controller(start_training_request)
    return StartTrainingResponse(**response)


@model_router.post("/aws/rekog/deploy_model", response_model=ModelStatus)
def deploy_model(deploy_model_request: DeployModel):
    response = ModelController().deploy_model_controller(deploy_model_request)
    return ModelStatus(**response)


@model_router.post("/aws/rekog/undeploy_model", response_model=ModelStatus)
def undeploy_model(undeploy_model_request: UndeployModel):
    response = ModelController().undeploy_model_controller(undeploy_model_request)
    return ModelStatus(**response)


@model_router.post("/aws/rekog/delete_model", response_model=ModelStatus)
def delete_model(delete_model_request: DeleteModel):
    response = ModelController().delete_model_controller(delete_model_request)
    return ModelStatus(**response)


@model_router.get("/aws/rekog/get_model_evaluation")
def get_model_evaluation(project_arn: str, version_name: Optional[str] = None):
    response = ModelController().get_evaluation_controller(
        project_arn=project_arn, version_name=version_name
    )
    return response


@model_router.get("/aws/rekog/get_model_manifest")
def get_model_manifest(project_arn: str, version_name: Optional[str] = None):
    response = ModelController().get_manifest_controller(
        project_arn=project_arn, version_name=version_name
    )
    return response


@model_router.get("/aws/rekog/get_predictions")
def get_predictions(
    project_version_arn: str, s3_uri: str, confidence_threshold: int = 50
):
    return ModelController().get_predictions_controller(
        project_version_arn=project_version_arn,
        s3_uri=s3_uri,
        confidence_threshold=confidence_threshold,
    )
