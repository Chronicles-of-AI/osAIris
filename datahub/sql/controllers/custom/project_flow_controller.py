import json
from sql import config, logger
from commons.external_call import APIInterface
from sql.crud.project_flow_crud import CRUDProjectFlow
from sql.crud.services_crud import CRUDServices
from sql.controllers.label_studio.label_studio_controller import ProjectController
from datetime import datetime

logging = logger(__name__)


class ProjectFlowController:
    def __init__(self):
        self.CRUDProjectFlow = CRUDProjectFlow()
        self.CRUDServices = CRUDServices()
        self.label_studio_config = config.get("label_studio").get("endpoint")
        self.label_studio_token = config.get("label_studio").get("token")
        self.header = {"Authorization": f"Token {self.label_studio_token}"}

    def create_project_flow_controller(self, request):
        try:
            logging.info("executing create_project_flow_controller function")
            create_project_flow_request = request.dict(exclude_none=True)

            # Creating Label Studio Project
            create_label_studio_project_request = {
                "title": create_project_flow_request.get("annotation_project_name"),
                "description": create_project_flow_request.get(
                    "annotation_project_description"
                ),
            }
            create_project_url = self.label_studio_config.get("label_studio_project")
            logging.info(f"{create_project_url=}")
            response, status_code = APIInterface.post(
                route=create_project_url,
                data=create_label_studio_project_request,
                headers=self.header,
            )
            service_record = self.CRUDServices.read_service(
                cloud_service_provider=create_project_flow_request.get(
                    "cloud_service_provider"
                ),
                use_case=create_project_flow_request.get("use_case"),
            )
            crud_request = {
                "pipeline_name": create_project_flow_request.get("pipeline_name"),
                "pipeline_description": create_project_flow_request.get(
                    "pipeline_description"
                ),
                "service_name": service_record.get("service_name"),
                "cloud_service_provider": create_project_flow_request.get(
                    "cloud_service_provider"
                ),
                "annotation_project_id": response.get("id"),
                "annotation_project_name": create_project_flow_request.get(
                    "annotation_project_name"
                ),
                "annotation_project_description": create_project_flow_request.get(
                    "annotation_project_description"
                ),
                "use_case": create_project_flow_request.get("use_case"),
                "current_stage": "CREATE_ANNOTATION_PROJECT",
                "functional_stage_id": response.get("id"),
                "created_at": datetime.now(),
            }
            self.CRUDProjectFlow.create(**crud_request)
            return {
                "pipeline_name": create_project_flow_request.get("pipeline_name"),
                "pipeline_description": create_project_flow_request.get(
                    "pipeline_description"
                ),
                "annotation_project_id": response.get("id"),
                "annotation_project_name": create_project_flow_request.get(
                    "annotation_project_name"
                ),
            }
        except Exception as error:
            logging.error(f"Error in create_project_flow_controller function: {error}")
            raise error

    def get_all_project_flow_controller(self):
        try:
            logging.info("executing create_project_flow_controller function")
            return self.CRUDProjectFlow.read_all()
        except Exception as error:
            logging.error(f"Error in create_project_flow_controller function: {error}")
            raise error

    def get_project_flow_by_name_controller(self, pipeline_name: str):
        try:
            logging.info("executing create_project_flow_controller function")
            return self.CRUDProjectFlow.read(pipeline_name=pipeline_name)
        except Exception as error:
            logging.error(f"Error in create_project_flow_controller function: {error}")
            raise error
