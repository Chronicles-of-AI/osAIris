from typing import List
from pydantic import BaseModel


class CreateTextClassificationDataset(BaseModel):
    project_id: str
    display_name: str
    region: str
    multi_label: bool = False


class CreateNERDataset(BaseModel):
    project_id: str
    display_name: str
    region: str


class CreateImageClassificationDataset(BaseModel):
    project_id: str
    display_name: str
    region: str
    multi_label: bool = False


class CreateObjectDetectionDataset(BaseModel):
    project_id: str
    display_name: str
    region: str


class CreateDatasetResponse(BaseModel):
    dataset_name: str
    dataset_id: str
