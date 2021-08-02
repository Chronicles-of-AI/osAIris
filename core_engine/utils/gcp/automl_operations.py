from google.cloud import automl

client = automl.AutoMlClient()


def get_operation_details(operation_id: str):
    response = client._transport.operations_client.get_operation(operation_id)
    if response.done:
        if response.error.code != 0:
            operation_status = "Failed"
            error_message = response.error.message
        else:
            operation_status = "Success"
            error_message = ""
    else:
        operation_status = "In-Progress"
        error_message = ""
    return {
        "operation_id": operation_id,
        "operation_completed": response.done,
        "status_metadata": operation_status,
        "error_message": error_message,
    }
