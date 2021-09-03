from pydantic import BaseModel


class CreateProjectFlow(BaseModel):
    pipeline_name: str
    pipeline_description: str
    cloud_service_provider: str
    annotation_project_name: str
    annotation_project_description: str = None
    use_case: str


class GetProjectFlow(BaseModel):
    pipeline_name: str
