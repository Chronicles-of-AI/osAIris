from typing import List
from pydantic import BaseModel
from datetime import datetime


class CreateProjectFlowResponse(BaseModel):
    pipeline_name: str
    pipeline_description: str
    annotation_project_name: str
    annotation_project_description: str = None


class ProjectFlowResponse(BaseModel):
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
    functional_stage_id: str = None
    current_stage: str = None
    created_by: str = None
    created_at: datetime
    updated_at: datetime = None
    status: str = None


class AllProjectFlowResponse(BaseModel):
    project_flows: List[ProjectFlowResponse]
