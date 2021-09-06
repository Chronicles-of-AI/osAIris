from fastapi import APIRouter
from core_engine.apis.schemas.requests.gcp.model_management_request import (
    ManageModel,
    ListModels,
    DescriptionModels,
    DeleteModels,
)
from core_engine.controllers.gcp.model_management_controller import (
    ManageModelController,
)
from core_engine import logger

logging = logger(__name__)

manage_model_router = APIRouter()


@manage_model_router.post("/gcp/automl/deploy_model")
def deploy_model(
    deploy_model_request: ManageModel,
):
    """[Describe a Model in AutoML GCP]

    Args:
        deploy_model_request (ManageModel): [Based on Input Schema]

    Raises:
        error: [Error]

    Returns:
        [type]: [description]
    """
    try:
        logging.info(f"Deploy Model Router: {deploy_model_request}")
        return ManageModelController().deploy_model_controller(
            request=deploy_model_request
        )
    except Exception as error:
        logging.error(f"{error=}")
        raise error


@manage_model_router.post("/gcp/automl/undeploy_model")
def undeploy_model(
    undeploy_model_request: ManageModel,
):
    """[Describe a Model in AutoML GCP]

    Args:
        undeploy_model_request (ManageModel): [Based on Input Schema]

    Raises:
        error: [Error]

    Returns:
        [type]: [description]
    """
    try:
        logging.info(f"Un-Deploy Model Router: {undeploy_model_request}")
        return ManageModelController().undeploy_model_controller(
            request=undeploy_model_request
        )
    except Exception as error:
        logging.error(f"{error=}")
        raise error


@manage_model_router.post("/gcp/automl/list_models")
def list_models(
    list_models_request: ListModels,
):
    """[List Models in AutoML GCP]

    Args:
        list_models_request (ListModels): [Based on Input Schema]

    Raises:
        error: [Error]

    Returns:
        [type]: [description]
    """
    try:
        logging.info(f"List Model Router: {list_models_request}")
        return ManageModelController().list_model_controller(
            request=list_models_request
        )
    except Exception as error:
        logging.error(f"{error=}")
        raise error


@manage_model_router.post("/gcp/automl/get_model_description")
def get_model_description(
    get_model_description_request: DescriptionModels,
):
    """[Describe a Model in AutoML GCP]

    Args:
        get_model_description_request (DescriptionModels): [Based on Input Schema]

    Raises:
        error: [Error]

    Returns:
        [type]: [description]
    """
    try:
        logging.info(f"Get Model Description Router: {get_model_description_request}")
        return ManageModelController().get_model_description_controller(
            request=get_model_description_request
        )
    except Exception as error:
        logging.error(f"{error=}")
        raise error


@manage_model_router.post("/gcp/automl/get_model_evaluation")
def get_model_evaluation(
    get_model_evaluation_request: DescriptionModels,
):
    """[Describe a Model in AutoML GCP]

    Args:
        get_model_evaluation_request (DescriptionModels): [Based on Input Schema]

    Raises:
        error: [Error]

    Returns:
        [type]: [description]
    """
    try:
        logging.info(f"Get Model Description Router: {get_model_evaluation_request}")
        return ManageModelController().get_model_evaluation_controller(
            request=get_model_evaluation_request
        )
    except Exception as error:
        logging.error(f"{error=}")
        raise error


@manage_model_router.post("/gcp/automl/delete_model")
def delete_model(
    delete_model_request: DeleteModels,
):
    """[Delete a Model in AutoML GCP]

    Args:
        delete_model_request (DeleteModels): [Based on Input Schema]

    Raises:
        error: [Error]

    Returns:
        [type]: [description]
    """
    try:
        logging.info(f"Delete Model Router: {delete_model_request}")
        return ManageModelController().delete_model_controller(
            request=delete_model_request
        )
    except Exception as error:
        logging.error(f"{error=}")
        raise error
