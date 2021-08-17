from fastapi import APIRouter
from core_engine.controllers.gcp.operations_controller import OperationsController
from core_engine import logger

logging = logger(__name__)

operations_router = APIRouter()


@operations_router.get("/gcp/automl/get_operation_details")
def get_operations(operation_id: str):
    """[summary]

    Args:
        operation_id (str): [Based on Input Schema]

    Raises:
        error: [Error]

    Returns:
        [type]: [description]
    """
    try:
        logging.info(f"Get Operations Router: {operation_id}")
        return OperationsController().get_operation_details_controller(
            operation_id=operation_id
        )
    except Exception as error:
        logging.error(f"{error=}")
        raise error
