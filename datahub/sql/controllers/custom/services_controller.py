from sql import config, logger
from sql.crud.services_crud import CRUDServices
from datetime import datetime

logging = logger(__name__)


class ServicesController:
    def __init__(self):
        self.CRUDServices = CRUDServices()
        self.label_studio_config = config.get("label_studio")

    def create_service_controller(self, request):
        """[Create a Service in Table]

        Args:
            request ([type]): [description]

        Raises:
            error: [Error]

        Returns:
            [type]: [description of created service]
        """
        try:
            logging.info("executing create_service_controller function")
            create_service_request = request.dict(exclude_none=True)
            crud_request = {
                "service_name": create_service_request.get("service_name"),
                "cloud_service_provider": create_service_request.get(
                    "cloud_service_provider"
                ),
                "use_case": create_service_request.get("use_case"),
                "data_type": create_service_request.get("data_type"),
                "created_at": datetime.now(),
            }
            self.CRUDServices.create(**crud_request)
            return crud_request
        except Exception as error:
            logging.error(f"Error in create_project_flow_controller function: {error}")
            raise error

    def get_all_services_controller(self):
        """[List all Services in Table]

        Raises:
            error: [Error]

        Returns:
            [type]: [List of all supported services]
        """
        try:
            logging.info("executing create_project_flow_controller function")
            return self.CRUDServices.read_all()
        except Exception as error:
            logging.error(f"Error in create_project_flow_controller function: {error}")
            raise error

    def get_services_by_use_case_controller(
        self, cloud_service_provider: str, use_case: str
    ):
        """[List a Service by Use Case and Cloud Vendor in Table]

        Args:
            cloud_service_provider (str): [Cloud Vendor's name in lower case]
            use_case (str): [use case as defined in table]

        Raises:
            error: [Error]

        Returns:
            [type]: [Filtered Services]
        """
        try:
            logging.info("executing create_project_flow_controller function")
            return self.CRUDServices.read_service(
                cloud_service_provider=cloud_service_provider,
                use_case=use_case,
            )
        except Exception as error:
            logging.error(f"Error in create_project_flow_controller function: {error}")
            raise error
