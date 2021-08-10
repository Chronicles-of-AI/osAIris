from sql.crud.project_crud import CRUDProject
from commons.external_call import APIInterface
from sql import config
from datetime import datetime


class ProjectController:
    def __init__(self):
        self.CRUDProject = CRUDProject()
        self.core_aws_project_config = (
            config.get("core_engine").get("aws").get("project_router")
        )

    def create_project(self, request: dict):
        """[summary]

        Args:
            request (dict): [description]

        Raises:
            error: [description]

        Returns:
            [type]: [description]
        """
        try:
            uuid = str(int(datetime.now().timestamp()))
            project_request = dict(request)
            create_project_url = self.core_aws_project_config.get("create_project")
            response, status_code = APIInterface.post(
                route=create_project_url, data=project_request
            )
            project_request.update(response)
            project_request.update({"uuid": uuid, "status": "CREATED"})
            self.CRUDProject.create(**project_request)
            return project_request
        except Exception as error:
            raise error

    def delete_project(self, request: dict):
        """[summary]

        Args:
            request (dict): [description]

        Raises:
            error: [description]

        Returns:
            [type]: [description]
        """
        try:
            project_request = dict(request)
            delete_project_url = self.core_aws_project_config.get("delete_project")
            response, status_code = APIInterface.post(
                route=delete_project_url, data=project_request
            )
            if status_code == 200:
                self.CRUDProject.delete(request.project_arn)
            else:
                # TODO: Add error in DB
                pass
            return {
                "project_arn": request.project_arn,
                "status": response.get("project_status"),
            }
        except Exception as error:
            raise error

    def get_all_projects(self):
        """[summary]

        Raises:
            error: [description]

        Returns:
            [type]: [description]
        """
        try:
            get_all_projects_url = self.core_aws_project_config.get("get_all_projects")
            response, _ = APIInterface.get(route=get_all_projects_url)
            return response
        except Exception as error:
            raise error

    def get_project_description(self, project_arn: str, version_names: str = None):
        """[summary]

        Args:
            project_arn (str): [description]
            version_names (str, optional): [description]. Defaults to None.

        Raises:
            error: [description]

        Returns:
            [type]: [description]
        """
        try:
            project_description_url = self.core_aws_project_config.get(
                "project_description"
            )
            project_params = {"project_arn": project_arn, "version_name": version_names}
            response, _ = APIInterface.get(
                route=project_description_url, params=project_params
            )
            return response
        except Exception as error:
            raise error
