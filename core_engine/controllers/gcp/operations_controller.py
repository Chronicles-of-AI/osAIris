from utils.gcp.automl_operations import get_operation_details


class OperationsController:
    def __init__(self):
        pass

    def get_operation_details_controller(self, operation_id):
        return get_operation_details(operation_id=operation_id)
