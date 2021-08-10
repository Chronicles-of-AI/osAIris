from commons.external_call import APIInterface
from sql import config
from sql.crud.deployment_crud import CRUDDeployment
from sql.crud.operation_crud import CRUDOperations
from datetime import datetime


class ManageModelController:
    def __init__(self):
        self.CRUDDeployment = CRUDDeployment()
        self.CRUDOperations = CRUDOperations()
        self.gcp_config = config.get("core_engine").get("gcp")

    def create_operation_record(self, api_response: dict, functional_stage: str):
        """[summary]

        Args:
            api_response (dict): [description]
            functional_stage (str): [description]

        Raises:
            error: [description]
        """
        try:
            operation_crud_request = {
                "operation_id": api_response.get("operation_id"),
                "status": api_response.get("status"),
                "project_id": api_response.get("project_id"),
                "region": api_response.get("region"),
                "functional_stage": functional_stage,
                "service_id": api_response.get("model_id"),
                "created": datetime.now(),
            }
            self.CRUDOperations.create(**operation_crud_request)
        except Exception as error:
            raise error

    def deploy_model_controller(self, request):
        """[summary]

        Args:
            request ([type]): [description]

        Raises:
            error: [description]

        Returns:
            [type]: [description]
        """
        try:
            uuid = str(int(datetime.now().timestamp()) * 10000)
            deploy_model_url = (
                self.gcp_config.get("automl").get("common").get("deploy_model")
            )
            deploy_model_request = request.dict(exclude_none=True)
            response, status_code = APIInterface.post(
                route=deploy_model_url,
                data=deploy_model_request,
            )
            if status_code == 200:
                crud_request = {
                    "model_id": response.get("model_id"),
                    "UUID": uuid,
                    "status": response.get("status"),
                    "created": datetime.now(),
                }
                self.CRUDDeployment.upsert(crud_request)
                self.create_operation_record(
                    api_response=response, functional_stage="DEPLOY_MODEL"
                )
                return {
                    "model_id": response.get("model_id"),
                    "operation_id": response.get("operation_id"),
                    "status": response.get("status"),
                }
            else:
                # TODO: error
                pass
                return {"status": "model deployment failed"}
        except Exception as error:
            raise error

    def undeploy_model_controller(self, request):
        """[summary]

        Args:
            request ([type]): [description]

        Raises:
            error: [description]

        Returns:
            [type]: [description]
        """
        try:
            undeploy_model_url = (
                self.gcp_config.get("automl").get("common").get("undeploy_model")
            )
            undeploy_model_request = request.dict(exclude_none=True)
            response, status_code = APIInterface.post(
                route=undeploy_model_url,
                data=undeploy_model_request,
            )
            if status_code == 200:
                crud_request = {
                    "model_id": response.get("model_id"),
                    "status": response.get("status"),
                    "updated": datetime.now(),
                }
                self.CRUDDeployment.update(deployment_request=crud_request)
                self.create_operation_record(
                    api_response=response, functional_stage="UNDEPLOY_MODEL"
                )
                return {
                    "model_id": response.get("model_id"),
                    "operation_id": response.get("operation_id"),
                    "status": response.get("status"),
                }
            else:
                # TODO: error
                pass
                return {"status": "model undeployment failed"}
        except Exception as error:
            raise error

    def list_model_controller(self, request):
        """[summary]

        Args:
            request ([type]): [description]

        Raises:
            error: [description]

        Returns:
            [type]: [description]
        """
        try:
            list_model_url = (
                self.gcp_config.get("automl").get("common").get("list_models")
            )
            list_model_request = request.dict(exclude_none=True)
            response, status_code = APIInterface.post(
                route=list_model_url,
                data=list_model_request,
            )
            return response
        except Exception as error:
            raise error

    def get_model_description_controller(self, request):
        """[summary]

        Args:
            request ([type]): [description]

        Raises:
            error: [description]

        Returns:
            [type]: [description]
        """
        try:
            model_description_url = (
                self.gcp_config.get("automl").get("common").get("get_model_description")
            )
            model_description_request = request.dict(exclude_none=True)
            response, status_code = APIInterface.post(
                route=model_description_url,
                data=model_description_request,
            )
            return response
        except Exception as error:
            raise error

    def delete_model_controller(self, request):
        """[summary]

        Args:
            request ([type]): [description]

        Raises:
            error: [description]

        Returns:
            [type]: [description]
        """
        try:
            delete_model_url = (
                self.gcp_config.get("automl").get("common").get("delete_model")
            )
            delete_model_request = request.dict(exclude_none=True)
            response, status_code = APIInterface.post(
                route=delete_model_url,
                data=delete_model_request,
            )
            if status_code == 200:
                crud_request = {
                    "model_id": response.get("model_id"),
                    "status": response.get("status"),
                    "updated": datetime.now(),
                }
                self.CRUDDeployment.update(deployment_request=crud_request)
                self.create_operation_record(
                    api_response=response, functional_stage="DELETE_MODEL"
                )
                return {
                    "model_id": response.get("model_id"),
                    "operation_id": response.get("operation_id"),
                    "status": response.get("status"),
                }
            else:
                # TODO: error
                pass
                return {"status": "model undeployment failed"}
        except Exception as error:
            raise error
