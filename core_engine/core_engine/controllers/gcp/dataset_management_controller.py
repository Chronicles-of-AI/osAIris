from core_engine.utils.gcp.automl_manage_datasets import (
    list_datasets,
    delete_datasets,
    get_dataset_description,
)
from core_engine import logger

logging = logger(__name__)


class ManageDatasetController:
    def __init__(self):
        pass

    def list_datasets_controller(self, request):
        """[List Datasets in AutoML GCP]

        Args:
            request ([type]): [Based on the Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [description]
        """
        try:
            logging.info(f"List Dataset Controller: {request}")
            return list_datasets(
                project_id=request.project_id,
                region=request.region,
            )
        except Exception as error:
            logging.error(f"{error=}")
            raise error

    def get_dataset_description_controller(self, request):
        """[Describe a Dataset in AutoML GCP]

        Args:
            request ([type]): [Based on the Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [description]
        """
        try:
            logging.info(f"List Dataset Controller: {request}")
            return get_dataset_description(
                project_id=request.project_id,
                region=request.region,
                dataset_id=request.dataset_id,
            )
        except Exception as error:
            logging.error(f"{error=}")
            raise error

    def delete_dataset_controller(self, request):
        """[Delete a Dataset in AutoML GCP]

        Args:
            request ([type]): [Based on the Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [description]
        """
        try:
            logging.info(f"List Dataset Controller: {request}")
            return delete_datasets(
                project_id=request.project_id,
                region=request.region,
                dataset_id=request.dataset_id,
            )
        except Exception as error:
            logging.error(f"{error=}")
            raise error
