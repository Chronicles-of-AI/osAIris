from typing import List
from pydantic import BaseModel


class ManageModel(BaseModel):
    pipeline_id: int
    project_id: str
    model_id: str
    region: str


class ListModels(BaseModel):
    project_id: str
    region: str
    dataset_id: str = None


class DescriptionModels(BaseModel):
    project_id: str
    region: str
    model_id: str = None


class DeleteModels(BaseModel):
    project_id: str
    region: str
    model_id: str = None
