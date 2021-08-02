from typing import List
from pydantic import BaseModel


class ImportDataset(BaseModel):
    project_id: str
    dataset_id: str
    gcs_path: str
    region: str