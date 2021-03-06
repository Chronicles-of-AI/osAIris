from typing import List
from pydantic import BaseModel
from datetime import datetime


class CreateProjectFlowResponse(BaseModel):
    pipeline_id: int
    pipeline_name: str
    pipeline_description: str
    annotation_project_name: str
    annotation_project_id: str


class ProjectFlowResponse(BaseModel):
    pipeline_id: int
    pipeline_name: str
    pipeline_description: str
    use_case: str
    cloud_service_provider: str
    service_name: str
    annotation_project_id: int
    annotation_project_name: str
    annotation_project_description: str = None
    raw_annotation_uri: str = None
    transform_annotation_uri: str = None
    model_id: str = None
    functional_stage_id: str
    current_stage: str
    created_by: str = None
    created_at: datetime
    updated_at: datetime
    status: str = None


class AllProjectFlowResponse(BaseModel):
    project_flows: List[ProjectFlowResponse]
