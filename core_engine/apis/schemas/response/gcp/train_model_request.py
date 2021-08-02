from typing import List
from pydantic import BaseModel


class TrainTextModel(BaseModel):
    project_id: str
    dataset_id: str
    model_display_name: str
    region: str


class TrainImageModel(BaseModel):
    project_id: str
    dataset_id: str
    model_display_name: str
    region: str


class TrainImageEdgeModel(BaseModel):
    project_id: str
    dataset_id: str
    model_display_name: str
    region: str
    model_type: str
