from pydantic import BaseModel


class CreateProject(BaseModel):
    pipeline_id: int
    project_name: str


class DeleteProject(BaseModel):
    project_arn: str
