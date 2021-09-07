from pydantic import BaseModel


class DataMonitoringRecord(BaseModel):
    annotation_id: int
    task_id: int
