from fastapi import APIRouter
from apis.schemas.requests.gcp.model_management_request import (
    ManageModel,
    ListModels,
    DescriptionModels,
    DeleteModels,
)
from controllers.gcp.model_management_controller import ManageModelController

manage_model_router = APIRouter()


@manage_model_router.post("/gcp/automl/deploy_model")
def deploy_model(
    deploy_model_request: ManageModel,
):
    return ManageModelController().deploy_model_controller(request=deploy_model_request)


@manage_model_router.post("/gcp/automl/undeploy_model")
def undeploy_model(
    undeploy_model_request: ManageModel,
):
    return ManageModelController().undeploy_model_controller(
        request=undeploy_model_request
    )


@manage_model_router.post("/gcp/automl/list_models")
def list_models(
    list_models_request: ListModels,
):
    return ManageModelController().list_model_controller(request=list_models_request)


@manage_model_router.post("/gcp/automl/get_model_description")
def get_model_description(
    get_model_description_request: DescriptionModels,
):
    return ManageModelController().get_model_description_controller(
        request=get_model_description_request
    )


@manage_model_router.post("/gcp/automl/delete_model")
def delete_model(
    delete_model_request: DeleteModels,
):
    return ManageModelController().delete_model_controller(request=delete_model_request)
