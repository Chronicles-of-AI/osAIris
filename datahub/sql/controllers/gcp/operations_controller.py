from commons.external_call import APIInterface
from sql import config
from sql.crud.operation_crud import CRUDOperations
from sql.utils.operation_helper import (
    import_dataset_operation,
    delete_dataset_operation,
    delete_model_operation,
    deploy_model_operation,
    undeploy_model_operation,
    train_model_operation,
)


class OperationsController:
    def __init__(self):
        self.gcp_config = config.get("core_engine").get("gcp")
        self.CRUDOperations = CRUDOperations()
        self.functional_stages = {
            "DELETE_DATASET": delete_dataset_operation,
            "IMPORT_DATASET": import_dataset_operation,
            "DEPLOY_MODEL": deploy_model_operation,
            "UNDEPLOY_MODEL": undeploy_model_operation,
            "DELETE_MODEL": delete_model_operation,
            "TRAIN_MODEL": train_model_operation,
        }

    def get_operation_details_controller(self, operation_id):
        get_operation_details_url = (
            self.gcp_config.get("automl").get("common").get("get_operation_details")
        )
        response, status_code = APIInterface.get(
            route=get_operation_details_url, params={"operation_id": operation_id}
        )
        if response.get("operation_completed"):
            operation_data = self.CRUDOperations.read(operation_id=operation_id)
            current_stage = operation_data.get("functional_stage")
            service_id = operation_data.get("service_id")
            self.functional_stages.get(current_stage)(
                operation_id=operation_id,
                service_id=service_id,
                status=response.get("status_metadata"),
                error=response.get("error_message"),
            )
            return response
        else:
            return response
