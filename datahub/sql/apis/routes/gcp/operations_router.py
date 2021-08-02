from fastapi import APIRouter
from sql.controllers.gcp.operations_controller import OperationsController

operations_router = APIRouter()


@operations_router.get("/gcp/automl/get_operation_details")
def get_operations(operation_id: str):
    return OperationsController().get_operation_details_controller(
        operation_id=operation_id
    )
