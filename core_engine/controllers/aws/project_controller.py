from utils.aws.rekognition_helper import (
    create_project,
    delete_project,
    version_description,
    get_all_projects,
)


class ProjectController:
    def __init__(self):
        pass

    def create_project_controller(self, project_name: str):
        return create_project(project_name)

    def delete_project_controller(self, project_arn: str):
        return delete_project(project_arn=project_arn)

    def get_all_projects_controller(self):
        return get_all_projects()

    def version_description_controller(self, project_arn: str, version_name: str):
        return version_description(project_arn=project_arn, version_name=version_name)
