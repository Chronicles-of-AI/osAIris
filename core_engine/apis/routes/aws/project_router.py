from fastapi import APIRouter
from typing import Optional
from apis.schemas.requests.aws.project_request import (
    CreateProject,
    DeleteProject,
)
from apis.schemas.response.aws.project_response import (
    CreateProjectResponse,
    DeleteProjectResponse,
)
from controllers.aws.project_controller import ProjectController

project_router = APIRouter()


@project_router.post("/aws/rekog/create_project", response_model=CreateProjectResponse)
def create_project(create_project_request: CreateProject):
    project_arn = ProjectController().create_project_controller(
        project_name=create_project_request.project_name
    )
    return CreateProjectResponse(**{"project_arn": project_arn})


@project_router.post("/aws/rekog/delete_project", response_model=DeleteProjectResponse)
def delete_project(delete_project_request: DeleteProject):
    project_status = ProjectController().delete_project_controller(
        project_arn=delete_project_request.project_arn
    )
    return DeleteProjectResponse(**{"project_status": project_status})


@project_router.get("/aws/rekog/get_all_projects")
def get_all_projects():
    response = ProjectController().get_all_projects_controller()
    return response


@project_router.get("/aws/rekog/get_project_description")
def get_project_description(project_arn: str, version_name: Optional[str] = None):
    project_description = ProjectController().version_description_controller(
        project_arn=project_arn,
        version_name=version_name,
    )
    return project_description
