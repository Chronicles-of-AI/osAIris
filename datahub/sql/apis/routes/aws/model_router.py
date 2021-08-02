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
    if decodeJWT(token=token):
        response = ModelController().train_model_controller(start_training_request)
        return ModelStatus(**response)
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid access token",
            headers={"WWW-Authenticate": "Bearer"},
        )


@model_router.post("/aws/rekog/deploy_model", response_model=ModelStatus)
def deploy_model(
    deploy_model_request: DeployModel, token: str = Depends(oauth2_scheme)
):
    if decodeJWT(token=token):
        response = ModelController().deploy_model_controller(deploy_model_request)
        return ModelStatus(**response)
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid access token",
            headers={"WWW-Authenticate": "Bearer"},
        )


@model_router.post("/aws/rekog/undeploy_model", response_model=ModelStatus)
def undeploy_model(
    undeploy_model_request: UndeployModel, token: str = Depends(oauth2_scheme)
):
    if decodeJWT(token=token):
        response = ModelController().undeploy_model_controller(undeploy_model_request)
        return ModelStatus(**response)
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid access token",
            headers={"WWW-Authenticate": "Bearer"},
        )


@model_router.post("/aws/rekog/delete_model", response_model=ModelStatus)
def delete_model(
    delete_model_request: DeleteModel, token: str = Depends(oauth2_scheme)
):
    if decodeJWT(token=token):
        response = ModelController().delete_model_controller(delete_model_request)
        return ModelStatus(**response)
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid access token",
            headers={"WWW-Authenticate": "Bearer"},
        )


@model_router.get("/aws/rekog/get_model_evaluation")
def get_model_evaluation(
    project_arn: str,
    version_name: Optional[str] = None,
    token: str = Depends(oauth2_scheme),
):
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


@model_router.get("/aws/rekog/get_model_manifest")
def get_model_manifest(
    project_arn: str,
    version_name: Optional[str] = None,
    token: str = Depends(oauth2_scheme),
):
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


@model_router.get("/aws/rekog/get_predictions")
def get_predictions(
    project_version_arn: str,
    s3_uri: str,
    confidence_threshold: int = 50,
    token: str = Depends(oauth2_scheme),
):
    return ModelController().get_predictions_controller(
        project_version_arn=project_version_arn,
        s3_uri=s3_uri,
        confidence_threshold=confidence_threshold,
    )
