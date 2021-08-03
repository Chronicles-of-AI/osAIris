from typing import List
from pydantic import BaseModel


class GetPredictions(BaseModel):
    project_id: str
    model_id: str
    content: str
    region: str
