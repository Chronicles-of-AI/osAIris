from sql.crud.operation_crud import CRUDOperations
from sql.crud.dataset_crud import CRUDDataset
from sql.crud.import_data_crud import CRUDDataImport
from sql.crud.model_crud import CRUDModel
from sql.crud.deployment_crud import CRUDDeployment
from sql.crud.project_flow_crud import CRUDProjectFlow
from sql.crud.model_monitoring_crud import CRUDModelMonitoring
from sql.controllers.gcp.model_management_controller import ManageModelController
from sql.apis.schemas.requests.gcp.model_management_request import (
    ListModels,
    DescriptionModels,
)
from datetime import datetime
from sql import logger

logging = logger(__name__)


def update_operations_record(operation_id: str, status: str, error: str):
    """[The function is used to update the GCP operation record on osAIris DB]

    Args:
        operation_id (str): [Unique identifier for operation]
        status (str): [Current status of the operation]
        error (str): [Error if any in the operation execution]

    Raises:
        error: [Error returned from osAIris CRUD operation]
    """
    try:
        logging.info("Update Operation Record")
        operation_request = {
            "operation_id": operation_id,
            "status": status,
            "error": error,
            "updated": datetime.now(),
        }
        CRUDOperations().update(operation_request=operation_request)
    except Exception as error:
        logging.error(f"Error in update_operation_record: {error}")
        raise error


def delete_dataset_operation(
    operation_id: str, service_id: str, status: str, error: str = ""
):
    """[This function is used to the update operations table when a dataset is deleted]

    Args:
        operation_id (str): [Unique identifier for operation]
        service_id (str): [Unique identifier for the dataset]
        status (str): [Current status of the operation]
        error (str, optional): [Error if any in the operation execution]. Defaults to "".

    Raises:
        error: [Error returned from osAIris CRUD operation]
    """
    try:
        logging.info("Detele Dataset Operation")
        update_operations_record(operation_id=operation_id, status=status, error=error)
        CRUDDataset().update(dataset_id=service_id, status="Deleted")
    except Exception as error:
        logging.error(f"Error in delete_dataset_operation: {error}")
        raise error


def import_dataset_operation(
    operation_id: str, service_id: str, status: str, error: str = ""
):
    """[This function is used to the update operations table when dataset is imported]

    Args:
        operation_id (str): [Unique identifier for operation]
        service_id (str): [Unique identifier for the dataset]
        status (str): [Current status of the operation]
        error (str, optional): [Error if any in the operation execution]. Defaults to "".

    Raises:
        error: [Error returned from osAIris CRUD operation]
    """
    try:
        logging.info("Import Dataset Operation")
        update_operations_record(operation_id=operation_id, status=status, error=error)
        pipeline_id = (
            CRUDOperations().read(operation_id=operation_id).get("pipeline_id")
        )
        project_flow_crud_request = {
            "pipeline_id": pipeline_id,
            "updated_at": datetime.now(),
            "functional_stage_id": service_id,
            "current_stage": "DATA_IMPORTED",
        }
        CRUDProjectFlow().update(**project_flow_crud_request)
        CRUDDataImport().update(dataset_id=service_id, status=status)
    except Exception as error:
        logging.error(f"Error in import_dataset_operation: {error}")
        raise error


def deploy_model_operation(
    operation_id: str, service_id: str, status: str, error: str = ""
):
    """[This function is used to the update operations table when a model is deployed]

    Args:
        operation_id (str): [Unique identifier for operation]
        service_id (str): [Unique identifier for the dataset]
        status (str): [Current status of the operation]
        error (str, optional): [Error if any in the operation execution]. Defaults to "".

    Raises:
        error: [Error returned from osAIris CRUD operation]
    """
    try:
        logging.info("Deploy Model Operation")
        update_operations_record(operation_id=operation_id, status=status, error=error)
        deployment_request = {
            "model_id": service_id,
            "status": status,
            "updated": datetime.now(),
        }
        pipeline_id = (
            CRUDOperations().read(operation_id=operation_id).get("pipeline_id")
        )
        project_flow_crud_request = {
            "pipeline_id": pipeline_id,
            "updated_at": datetime.now(),
            "functional_stage_id": service_id,
            "current_stage": "MODEL_DEPLOYED",
        }
        CRUDProjectFlow().update(**project_flow_crud_request)
        CRUDDeployment().update(deployment_request=deployment_request)
    except Exception as error:
        logging.error(f"Error in deploy_model_operation: {error}")
        raise error


def undeploy_model_operation(
    operation_id: str, service_id: str, status: str, error: str = ""
):
    """[This function is used to the update operations table when a model is undeployed]

    Args:
        operation_id (str): [Unique identifier for operation]
        service_id (str): [Unique identifier for the dataset]
        status (str): [Current status of the operation]
        error (str, optional): [Error if any in the operation execution]. Defaults to "".

    Raises:
        error: [Error returned from osAIris CRUD operation]
    """
    try:
        logging.info("Un-Deploy Model Operation")
        update_operations_record(operation_id=operation_id, status=status, error=error)
        deployment_request = {
            "model_id": service_id,
            "status": "Model Undeployed",
            "updated": datetime.now(),
        }
        pipeline_id = (
            CRUDOperations().read(operation_id=operation_id).get("pipeline_id")
        )
        project_flow_crud_request = {
            "pipeline_id": pipeline_id,
            "updated_at": datetime.now(),
            "functional_stage_id": service_id,
            "current_stage": "MODEL_UNDEPLOYED",
        }
        CRUDProjectFlow().update(**project_flow_crud_request)
        CRUDDeployment().update(deployment_request=deployment_request)
    except Exception as error:
        logging.error(f"Error in undeploy_model_operation: {error}")
        raise error


def delete_model_operation(
    operation_id: str, service_id: str, status: str, error: str = ""
):
    """[This function is used to the update operations table when a model is deleted]

    Args:
        operation_id (str): [Unique identifier for operation]
        service_id (str): [Unique identifier for the dataset]
        status (str): [Current status of the operation]
        error (str, optional): [Error if any in the operation execution]. Defaults to "".

    Raises:
        error: [Error returned from osAIris CRUD operation]
    """
    try:
        logging.info("Delete Model Operation")
        update_operations_record(operation_id=operation_id, status=status, error=error)
        model_request = {
            "model_id": service_id,
            "status": "Model Deleted",
            "updated": datetime.now(),
        }
        CRUDModel().update(model_request=model_request)
        CRUDDeployment().update(deployment_request=model_request)
    except Exception as error:
        logging.error(f"Error in delete_model_operation: {error}")
        raise error


def train_model_operation(
    operation_id: str, service_id: str, status: str, error: str = ""
):
    """[This function is used to the update operations table when a model is trained]

    Args:
        operation_id (str): [Unique identifier for operation]
        service_id (str): [Unique identifier for the dataset]
        status (str): [Current status of the operation]
        error (str, optional): [Error if any in the operation execution]. Defaults to "".

    Raises:
        error: [Error returned from osAIris CRUD operation]
    """
    try:
        logging.info("Train Model Operation")
        update_operations_record(operation_id=operation_id, status=status, error=error)
        operation_data = CRUDOperations().read(operation_id=operation_id)
        project_id, region = operation_data.get("project_id"), operation_data.get(
            "region"
        )
        model_data = CRUDModel().read(model_request={"model_id": operation_id})
        list_model_request = ListModels(
            project_id=project_id, region=region, dataset_id=service_id
        )
        models_response = ManageModelController().list_model_controller(
            request=list_model_request
        )
        for model in models_response.get("models"):
            if model.get("model_display_name") == model_data.get("alias_name"):
                model_id = model.get("model_id")
                model_request = {
                    "operation_id": operation_id,
                    "model_id": model_id,
                    "status": status,
                    "updated": datetime.now(),
                }
                pipeline_id = (
                    CRUDOperations().read(operation_id=operation_id).get("pipeline_id")
                )
                project_flow_crud_request = {
                    "pipeline_id": pipeline_id,
                    "updated_at": datetime.now(),
                    "model_id": model_id,
                    "functional_stage_id": model_id,
                    "current_stage": "TRAINED",
                }
                CRUDProjectFlow().update(**project_flow_crud_request)
                CRUDModel().update_by_operation_id(model_request=model_request)
                evaluate_model_request = DescriptionModels(
                    project_id=project_id, region=region, model_id=model_id
                )
                model_evaluation_response = (
                    ManageModelController().get_model_evaluation_controller(
                        request=evaluate_model_request
                    )
                )
                create_model_monitoring_request = {
                    "model_uri": model_id,
                    "model_f1_score": model_evaluation_response.get("f1_score"),
                    "model_recall": model_evaluation_response.get("recall"),
                    "model_precision": model_evaluation_response.get("precision"),
                    "model_drift_threshold": "0.8",
                    "created_at": datetime.now(),
                    "updated_at": datetime.now(),
                }
                CRUDModelMonitoring().create(**create_model_monitoring_request)
    except Exception as error:
        logging.error(f"Error in train_model_operation: {error}")
        raise error
