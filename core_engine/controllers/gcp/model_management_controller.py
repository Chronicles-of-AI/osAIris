from utils.gcp.automl_manage_model import (
    model_deployment,
    model_undeployment,
    get_model_description,
    delete_model,
)
from utils.gcp.automl_list_models import list_models
from core_engine import logger

logging = logger(__name__)


class ManageModelController:
    def __init__(self):
        pass

    def deploy_model_controller(self, request):
        """[Deploy a Model In AutoML GCP]

        Args:
            request ([type]): [Based on the Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [description]
        """
        try:
            logging.info(f"Deploy Model Controller: {request}")
            return model_deployment(
                project_id=request.project_id,
                model_id=request.model_id,
                region=request.region,
            )
        except Exception as error:
            logging.error(f"{error=}")
            raise error

    def undeploy_model_controller(self, request):
        """[Un-Deploy a Model In AutoML GCP]

        Args:
            request ([type]): [Based on the Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [description]
        """
        try:
            logging.info(f"Un-Deploy Model Controller: {request}")
            return model_undeployment(
                project_id=request.project_id,
                model_id=request.model_id,
                region=request.region,
            )
        except Exception as error:
            logging.error(f"{error=}")
            raise error

    def list_model_controller(self, request):
        """[List Models In AutoML GCP]

        Args:
            request ([type]): [Based on the Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [description]
        """
        try:
            logging.info(f"List Model Controller: {request}")
            return list_models(
                project_id=request.project_id,
                region=request.region,
                dataset_id=request.dataset_id,
            )
        except Exception as error:
            logging.error(f"{error=}")
            raise error

    def get_model_description_controller(self, request):
        """[Describe a Model In AutoML GCP]

        Args:
            request ([type]): [Based on the Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [description]
        """
        try:
            logging.info(f"Get Model Description Controller: {request}")
            return get_model_description(
                project_id=request.project_id,
                region=request.region,
                model_id=request.model_id,
            )
        except Exception as error:
            logging.error(f"{error=}")
            raise error

    def delete_model_controller(self, request):
        """[Delete a Model In AutoML GCP]

        Args:
            request ([type]): [Based on the Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [description]
        """
        try:
            logging.info(f"Delete Model Controller: {request}")
            return delete_model(
                project_id=request.project_id,
                region=request.region,
                model_id=request.model_id,
            )
        except Exception as error:
            logging.error(f"{error=}")
            raise error
