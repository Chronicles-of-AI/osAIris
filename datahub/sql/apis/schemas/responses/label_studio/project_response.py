from io import BufferedIOBase
from typing import List
from pydantic import BaseModel


class CreatedBy(BaseModel):
    id: str
    first_name: str
    last_name: str
    email: str


class CreateProjectResponse(BaseModel):
    id: int
    title: str
    description: str
    created_by: CreatedBy
    created_at: str
    sampling: str = "Sequential sampling"


class ProjectResponse(BaseModel):
    status: str


class ExportAnnotationResponse(BaseModel):
    cloud_uri: str


class TransformAnnotationResponse(BaseModel):
    cloud_uri: str
