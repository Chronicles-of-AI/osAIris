from utils.gcp.automl_operations import get_operation_details
from core_engine import logger

logging = logger(__name__)


class OperationsController:
    def __init__(self):
        pass

    def get_operation_details_controller(self, operation_id):
        """[summary]

        Args:
            operation_id ([type]): [description]

        Raises:
            error: [description]

        Returns:
            [type]: [description]
        """
        try:
            logging.info(f"Get Operation Details Controller: {operation_id}")
            return get_operation_details(operation_id=operation_id)
        except Exception as error:
            logging.error(f"{error=}")
            raise error
