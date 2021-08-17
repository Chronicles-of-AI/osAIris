from typing import List
from pydantic import BaseModel


class ImportDatasetResponse(BaseModel):
    operation_id: str
    project_id: str
    dataset_id: str
    status: str
    region: str
