from sql.crud.operation_crud import CRUDOperations
from sql.crud.dataset_crud import CRUDDataset
from sql.crud.import_data_crud import CRUDDataImport
from sql.crud.model_crud import CRUDModel
from sql.crud.deployment_crud import CRUDDeployment
from sql.controllers.gcp.model_management_controller import ManageModelController
from sql.apis.schemas.requests.gcp.model_management_request import ListModels
from datetime import datetime


def update_operations_record(operation_id: str, status: str, error: str):
    """[summary]

    Args:
        operation_id (str): [description]
        status (str): [description]
        error (str): [description]

    Raises:
        error: [description]
    """
    try:
        operation_request = {
            "operation_id": operation_id,
            "status": status,
            "error": error,
            "updated": datetime.now(),
        }
        CRUDOperations().update(operation_request=operation_request)
    except Exception as error:
        raise error


def delete_dataset_operation(
    operation_id: str, service_id: str, status: str, error: str = ""
):
    """[summary]

    Args:
        operation_id (str): [description]
        service_id (str): [description]
        status (str): [description]
        error (str, optional): [description]. Defaults to "".

    Raises:
        error: [description]
    """
    try:
        update_operations_record(operation_id=operation_id, status=status, error=error)
        CRUDDataset().update(dataset_id=service_id, status="Deleted")
    except Exception as error:
        raise error


def import_dataset_operation(
    operation_id: str, service_id: str, status: str, error: str = ""
):
    """[summary]

    Args:
        operation_id (str): [description]
        service_id (str): [description]
        status (str): [description]
        error (str, optional): [description]. Defaults to "".

    Raises:
        error: [description]
    """
    try:
        update_operations_record(operation_id=operation_id, status=status, error=error)
        CRUDDataImport().update(dataset_id=service_id, status=status)
    except Exception as error:
        raise error


def deploy_model_operation(
    operation_id: str, service_id: str, status: str, error: str = ""
):
    """[summary]

    Args:
        operation_id (str): [description]
        service_id (str): [description]
        status (str): [description]
        error (str, optional): [description]. Defaults to "".

    Raises:
        error: [description]
    """
    try:
        update_operations_record(operation_id=operation_id, status=status, error=error)
        deployment_request = {
            "model_id": service_id,
            "status": status,
            "updated": datetime.now(),
        }
        CRUDDeployment().update(deployment_request=deployment_request)
    except Exception as error:
        raise error


def undeploy_model_operation(
    operation_id: str, service_id: str, status: str, error: str = ""
):
    """[summary]

    Args:
        operation_id (str): [description]
        service_id (str): [description]
        status (str): [description]
        error (str, optional): [description]. Defaults to "".

    Raises:
        error: [description]
    """
    try:
        update_operations_record(operation_id=operation_id, status=status, error=error)
        deployment_request = {
            "model_id": service_id,
            "status": "Model Undeployed",
            "updated": datetime.now(),
        }
        CRUDDeployment().update(deployment_request=deployment_request)
    except Exception as error:
        raise error


def delete_model_operation(
    operation_id: str, service_id: str, status: str, error: str = ""
):
    """[summary]

    Args:
        operation_id (str): [description]
        service_id (str): [description]
        status (str): [description]
        error (str, optional): [description]. Defaults to "".

    Raises:
        error: [description]
    """
    try:
        update_operations_record(operation_id=operation_id, status=status, error=error)
        model_request = {
            "model_id": service_id,
            "status": "Model Deleted",
            "updated": datetime.now(),
        }
        CRUDModel().update(model_request=model_request)
        CRUDDeployment().update(deployment_request=model_request)
    except Exception as error:
        raise error


def train_model_operation(
    operation_id: str, service_id: str, status: str, error: str = ""
):
    """[summary]

    Args:
        operation_id (str): [description]
        service_id (str): [description]
        status (str): [description]
        error (str, optional): [description]. Defaults to "".

    Raises:
        error: [description]
    """
    try:
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
                CRUDModel().update_by_operation_id(model_request=model_request)
    except Exception as error:
        raise error
