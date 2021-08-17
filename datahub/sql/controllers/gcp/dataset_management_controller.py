from datetime import datetime
import logging
from commons.external_call import APIInterface
from sql.crud.dataset_crud import CRUDDataset
from sql.crud.operation_crud import CRUDOperations
from sql import config, logger

logging = logger(__name__)


class ManageDatasetController:
    def __init__(self):
        self.CRUDDataset = CRUDDataset()
        self.CRUDOperations = CRUDOperations()
        self.gcp_config = config.get("core_engine").get("gcp")

    def create_operation_record(self, api_response: dict):
        """[Controller function to create GCP operation record]

        Args:
            api_response (dict): [API response from create operation]

        Raises:
            error: [Error raised from controller layer]
        """
        try:
            logging.info("executing create_operation_record function")
            operation_crud_request = {
                "operation_id": api_response.get("operation_id"),
                "status": api_response.get("status"),
                "project_id": api_response.get("project_id"),
                "region": api_response.get("region"),
                "functional_stage": "DELETE_DATASET",
                "service_id": api_response.get("dataset_id"),
                "created": datetime.now(),
            }
            self.CRUDOperations.create(**operation_crud_request)
        except Exception as error:
            logging.error(f"Error in create_operation_record function: {error}")
            raise error

    def list_datasets_controller(self, request):
        """[Controller function to list all GCP datasets]

        Args:
            request ([dict]): [list datasets request]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [list]: [list of all the datasets created on GCP]
        """
        try:
            logging.info("executing list_datasets_controller function")
            list_dataset_url = (
                self.gcp_config.get("automl").get("common").get("list_datasets")
            )
            list_dataset_request = request.dict(exclude_none=True)
            response, status_code = APIInterface.post(
                route=list_dataset_url,
                data=list_dataset_request,
            )
            return response
        except Exception as error:
            logging.error(f"Error in list_datasets_controller function: {error}")
            raise error

    def get_dataset_description_controller(self, request):
        """[Controller function to get dataset description]

        Args:
            request ([dict]): [get dataset description request]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [dict]: [dataset description details]
        """
        try:
            logging.info("executing get_dataset_description_controller function")
            get_dataset_description_url = (
                self.gcp_config.get("automl")
                .get("common")
                .get("get_dataset_description")
            )
            get_dataset_description_request = request.dict(exclude_none=True)
            response, status_code = APIInterface.post(
                route=get_dataset_description_url,
                data=get_dataset_description_request,
            )
            return response
        except Exception as error:
            logging.error(
                f"Error in get_dataset_description_controller function: {error}"
            )
            raise error

    def delete_dataset_controller(self, request):
        """[Controller function to delete dataset]

        Args:
            request ([dict]): [delete dataset request]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [dict]: [deleted dataset response]
        """
        try:
            logging.info("executing delete_dataset_controller function")
            delete_dataset_url = (
                self.gcp_config.get("automl").get("common").get("delete_dataset")
            )
            delete_dataset_request = request.dict(exclude_none=True)
            response, status_code = APIInterface.post(
                route=delete_dataset_url,
                data=delete_dataset_request,
            )
            if status_code == 200:
                self.CRUDDataset.update(
                    dataset_id=response.get("dataset_id"), status="Deleting"
                )
                self.create_operation_record(api_response=response)
                return response
            else:
                raise Exception({"status": "delete dataset failed"})
        except Exception as error:
            logging.error(f"Error in delete_dataset_controller function: {error}")
            raise error
