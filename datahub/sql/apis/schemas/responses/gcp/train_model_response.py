from pydantic import BaseModel


class TrainModelResponse(BaseModel):
    operation_id: str
    status: str
