from typing import List
from pydantic import BaseModel


class CreateTextClassificationDataset(BaseModel):
    pipeline_id: int
    project_id: str
    display_name: str
    region: str
    multi_label: bool = False


class CreateNERDataset(BaseModel):
    pipeline_id: int
    project_id: str
    display_name: str
    region: str


class CreateImageClassificationDataset(BaseModel):
    pipeline_id: int
    project_id: str
    display_name: str
    region: str
    multi_label: bool = False


class CreateObjectDetectionDataset(BaseModel):
    pipeline_id: int
    project_id: str
    display_name: str
    region: str
