from pydantic import BaseModel


class ImportDataset(BaseModel):
    pipeline_id: int
    project_id: str
    dataset_id: str
    gcs_path: str
    region: str
