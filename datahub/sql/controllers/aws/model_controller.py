from sql.crud.model_crud import CRUDModel
from sql.crud.deployment_crud import CRUDDeployment
from sql import config
from commons.external_call import APIInterface
from datetime import datetime


class ModelController:
    def __init__(self):
        self.CRUDModel = CRUDModel()
        self.CRUDDeployment = CRUDDeployment()
        self.core_aws_model_config = (
            config.get("core_engine").get("aws").get("model_router")
        )

    def train_model_controller(self, request):
        uuid = str(int(datetime.now().timestamp()))
        start_training_request = request.dict(exclude_none=True)
        start_training_url = self.core_aws_model_config.get("start_training")
        response, status_code = APIInterface.post(
            route=start_training_url, data=start_training_request
        )
        if status_code == 200:
            crud_request = {
                "model_id": response.get("project_version_arn"),
                "dataset_id": start_training_request.get("training_data"),
                "artifacts": start_training_request.get("output_config"),
                "alias_name": start_training_request.get("version_name"),
                "auto_trigger": False,
                "UUID": uuid,
                "status": "Running",
                "created": datetime.now(),
            }
            self.CRUDModel.create(**crud_request)
            return {"status": "training started"}
        else:
            # TODO: error
            pass
            return {"status": "training failed"}

    def deploy_model_controller(self, request):
        uuid = str(int(datetime.now().timestamp()))
        deploy_model_request = dict(request)
        deploy_model_url = self.core_aws_model_config.get("deploy_model")
        response, status_code = APIInterface.post(
            route=deploy_model_url, data=deploy_model_request
        )
        deployment_crud_request = {
            "UUID": uuid,
            "model_id": request.project_version_arn,
            "created": datetime.now(),
            "status": response.get("status"),
        }
        if status_code == 200:
            self.CRUDDeployment.create(**deployment_crud_request)
            return {"status": "model deployed successfully"}
        else:
            # TODO: error
            pass
            return {"status": "model deployment failed"}

    def undeploy_model_controller(self, request):
        undeploy_model_request = dict(request)
        deploy_model_url = self.core_aws_model_config.get("undeploy_model")
        response, status_code = APIInterface.post(
            route=deploy_model_url, data=undeploy_model_request
        )
        undeployment_crud_request = {
            "model_id": request.project_version_arn,
            "updated": datetime.now(),
            "status": response.get("status"),
        }
        if status_code == 200:
            self.CRUDDeployment.update(undeployment_crud_request)
            return {"status": "model undeployed successfully"}
        else:
            # TODO: error
            pass
            return {"status": "model undeployment failed"}

    def delete_model_controller(self, request):
        delete_model_request = dict(request)
        delete_model_url = self.core_aws_model_config.get("delete_model")
        response, status_code = APIInterface.post(
            route=delete_model_url, data=delete_model_request
        )
        delete_model_crud_request = {
            "model_id": request.project_version_arn,
            "status": response.get("status"),
            "updated": datetime.now(),
        }
        if status_code == 200:
            self.CRUDModel.update(delete_model_crud_request)
            return {"status": "model deleted successfully"}
        else:
            # TODO: error
            pass
            return {"status": "model deletion failed"}

    def get_evaluation_controller(self, project_arn, version_name):
        get_evaluation_url = self.core_aws_model_config.get("get_model_evaluation")
        response, status_code = APIInterface.get(
            route=get_evaluation_url,
            params={"project_arn": project_arn, "version_name": version_name},
        )
        if status_code == 200:
            return response
        else:
            return {"status": "Error in getting model evaluation"}

    def get_manifest_controller(self, project_arn, version_name):
        get_manifest_url = self.core_aws_model_config.get("get_model_manifest")
        response, status_code = APIInterface.get(
            route=get_manifest_url,
            params={"project_arn": project_arn, "version_name": version_name},
        )
        if status_code == 200:
            return response
        else:
            return {"status": "Error in getting model manifest"}

    def get_predictions_controller(
        self, project_version_arn: str, s3_uri: str, confidence_threshold: int
    ):
        get_predictions_url = self.core_aws_model_config.get("get_predictions")
        response, status_code = APIInterface.get(
            route=get_predictions_url,
            params={
                "project_version_arn": project_version_arn,
                "s3_uri": s3_uri,
                "confidence_threshold": confidence_threshold,
            },
        )
        return response
