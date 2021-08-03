from typing import List
from pydantic import BaseModel


class ManageModelResponse(BaseModel):
    operation_id: str
    model_id: str
    status: str
