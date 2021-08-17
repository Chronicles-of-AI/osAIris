from pydantic import BaseModel


class CreateProject(BaseModel):
    project_name: str


class DeleteProject(BaseModel):
    project_arn: str


class ProjectDescription(BaseModel):
    project_arn: str
    version_name: str
