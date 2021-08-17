from typing import List
from pydantic import BaseModel


class DatasetMetaInformation(BaseModel):
    dataset_name: str
    dataset_id: str
    display_name: str


class DescriptionDatasetsResponse(BaseModel):
    dataset_description: DatasetMetaInformation


class ListDatasetsResponse(BaseModel):
    all_datasets: List[DatasetMetaInformation]


class DeleteDatasetResponse(BaseModel):
    operation_id: str
    project_id: str
    dataset_id: str
    status: str
    region: str
