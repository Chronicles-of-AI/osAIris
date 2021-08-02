from datetime import datetime
from commons.external_call import APIInterface
from sql.crud.dataset_crud import CRUDDataset
from sql.crud.operation_crud import CRUDOperations
from sql import config


class ManageDatasetController:
    def __init__(self):
        self.CRUDDataset = CRUDDataset()
        self.CRUDOperations = CRUDOperations()
        self.gcp_config = config.get("core_engine").get("gcp")

    def create_operation_record(self, api_response: dict):
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

    def list_datasets_controller(self, request):
        list_dataset_url = (
            self.gcp_config.get("automl").get("common").get("list_datasets")
        )
        list_dataset_request = request.dict(exclude_none=True)
        response, status_code = APIInterface.post(
            route=list_dataset_url,
            data=list_dataset_request,
        )
        return response

    def get_dataset_description_controller(self, request):
        get_dataset_description_url = (
            self.gcp_config.get("automl").get("common").get("get_dataset_description")
        )
        get_dataset_description_request = request.dict(exclude_none=True)
        response, status_code = APIInterface.post(
            route=get_dataset_description_url,
            data=get_dataset_description_request,
        )
        return response

    def delete_dataset_controller(self, request):
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
            # TODO: error
            pass
            return {"status": "delete dataset failed"}
