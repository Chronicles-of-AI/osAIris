from pydantic import BaseModel


class CreateProject(BaseModel):
    project_name: str


class DeleteProject(BaseModel):
    project_arn: str
