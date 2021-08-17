from fastapi import APIRouter
from typing import Optional
from core_engine.apis.schemas.requests.aws.project_request import (
    CreateProject,
    DeleteProject,
)
from core_engine.apis.schemas.response.aws.project_response import (
    CreateProjectResponse,
    DeleteProjectResponse,
)
from core_engine.controllers.aws.project_controller import ProjectController
from core_engine import logger

logging = logger(__name__)

project_router = APIRouter()


@project_router.post("/aws/rekog/create_project", response_model=CreateProjectResponse)
def create_project(create_project_request: CreateProject):
    """[Create a Project in AWS]

    Args:
        create_project_request (CreateProject): [Based on Input Schema]

    Raises:
        error: [Error]

    Returns:
        [type]: [Based on Response Model]
    """
    try:
        logging.info(f"Create Project Router: {create_project_request}")
        project_arn = ProjectController().create_project_controller(
            project_name=create_project_request.project_name
        )
        return CreateProjectResponse(**{"project_arn": project_arn})
    except Exception as error:
        logging.error(f"{error=}")
        raise error


@project_router.post("/aws/rekog/delete_project", response_model=DeleteProjectResponse)
def delete_project(delete_project_request: DeleteProject):
    """[Delete a Project in AWS]

    Args:
        delete_project_request (DeleteProject): [Based on Input Schema]

    Raises:
        error: [Error]

    Returns:
        [type]: [Based on Response Model]
    """
    try:
        logging.info(f"Delete Project Router: {delete_project_request}")
        project_status = ProjectController().delete_project_controller(
            project_arn=delete_project_request.project_arn
        )
        return DeleteProjectResponse(**{"project_status": project_status})
    except Exception as error:
        logging.error(f"{error=}")
        raise error


@project_router.get("/aws/rekog/get_all_projects")
def get_all_projects():
    """[Get all Projects in AWS]

    Raises:
        error: [Error]

    Returns:
        [type]: [Based on Response Model]
    """
    try:
        logging.info(f"List Project Router")
        response = ProjectController().get_all_projects_controller()
        return response
    except Exception as error:
        logging.error(f"{error=}")
        raise error


@project_router.get("/aws/rekog/get_project_description")
def get_project_description(project_arn: str, version_name: Optional[str] = None):
    """[Describe a Project in AWS]

    Args:
        project_arn (str): [Unique Identifier for your Project]
        version_name (Optional[str], optional): [Version Name in AWS]. Defaults to None.

    Raises:
        error: [Error]

    Returns:
        [type]: [Based on Response Model]
    """
    try:
        logging.info(f"Get Project Description Router: {project_arn}")
        project_description = ProjectController().version_description_controller(
            project_arn=project_arn,
            version_name=version_name,
        )
        return project_description
    except Exception as error:
        logging.error(f"{error=}")
        raise error
