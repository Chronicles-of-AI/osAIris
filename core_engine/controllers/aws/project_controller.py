from utils.aws.rekognition_helper import (
    create_project,
    delete_project,
    version_description,
    get_all_projects,
)
from core_engine import logger

logging = logger(__name__)


class ProjectController:
    def __init__(self):
        pass

    def create_project_controller(self, project_name: str):
        """[Create a project in AWS]

        Args:
            project_name (str): [Project NAme]

        Raises:
            error: [Error]

        Returns:
            [type]: [description]
        """
        try:
            logging.info(f"Create Project Controller: {project_name}")
            return create_project(project_name)
        except Exception as error:
            logging.error(f"{error=}")
            raise error

    def delete_project_controller(self, project_arn: str):
        """[Deletes a project in AWS]

        Args:
            project_arn (str): [description]

        Raises:
            error: [Error]

        Returns:
            [type]: [description]
        """
        try:
            logging.info(f"Create Project Controller: {project_arn}")
            return delete_project(project_arn=project_arn)
        except Exception as error:
            logging.error(f"{error=}")
            raise error

    def get_all_projects_controller(self):
        """[Lists all the project in AWS]

        Raises:
            error: [Error]

        Returns:
            [type]: [description]
        """
        try:
            logging.info(f"Create Project Controller")
            return get_all_projects()
        except Exception as error:
            logging.error(f"{error=}")
            raise error

    def version_description_controller(self, project_arn: str, version_name: str):
        """[Describws a project in AWS]

        Args:
            project_arn (str): [Unique Identifier for your Project in AWS]
            version_name (str): [Version name on AWS console]

        Raises:
            error: [Error]

        Returns:
            [type]: [description]
        """
        try:
            logging.info(f"Create Project Controller: {project_arn}")
            return version_description(
                project_arn=project_arn, version_name=version_name
            )
        except Exception as error:
            logging.error(f"{error=}")
            raise error
