from typing import List
from pydantic import BaseModel


class GetPredictions(BaseModel):
    project_id: str
    model_id: str
    content: str
    region: str


class GetImagePredictions(BaseModel):
    project_id: str
    model_id: str
    region: str
    gcs_uri: str
