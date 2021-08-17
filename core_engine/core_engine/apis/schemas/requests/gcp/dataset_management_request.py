from typing import List
from pydantic import BaseModel


class ListDatasets(BaseModel):
    project_id: str
    region: str


class DescriptionDataset(BaseModel):
    project_id: str
    region: str
    dataset_id: str


class DeleteDataset(BaseModel):
    project_id: str
    region: str
    dataset_id: str
