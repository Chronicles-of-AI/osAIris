from pydantic import BaseModel


class OperationsResponse(BaseModel):
    operation_id: str
    operation_completed: bool
    status_metadata: str
    error_message: str
