from commons.external_call import APIInterface
from sql import config
from sql.crud.model_crud import CRUDModel
from sql.crud.deployment_crud import CRUDDeployment
from datetime import datetime


class ComprehendController:
    def __init__(self):
        self.CRUDModel = CRUDModel()
        self.CRUDDeployment = CRUDDeployment()
        self.core_aws_comprehend_config = (
            config.get("core_engine").get("aws").get("comprehend_router")
        )

    def create_document_classifier_controller(self, request):
        uuid = str(int(datetime.now().timestamp()))
        create_document_classifier_request = request.dict(exclude_none=True)
        create_document_classifier_url = self.core_aws_comprehend_config.get(
            "create_document_classifier"
        )
        response, status_code = APIInterface.post(
            route=create_document_classifier_url,
            data=create_document_classifier_request,
        )
        if status_code == 200:
            crud_request = {
                "model_id": response.get("document_classifier_arn"),
                "dataset_id": create_document_classifier_request.get("InputDataConfig"),
                "artifacts": create_document_classifier_request.get("OutputDataConfig"),
                "alias_name": create_document_classifier_request.get(
                    "DocumentClassifierName"
                ),
                "auto_trigger": False,
                "UUID": uuid,
                "status": "Running",
                "created": datetime.now(),
            }
            self.CRUDModel.create(**crud_request)
            return {
                "document_classifier_arn": response.get("document_classifier_arn"),
                "status": "training started",
            }
        else:
            # TODO: error
            pass
            return {"status": "training failed"}

    def delete_document_classifier_controller(self, request):
        delete_document_classifier_request = request.dict(exclude_none=True)
        delete_document_classifier_url = self.core_aws_comprehend_config.get(
            "delete_document_classifier"
        )
        response, status_code = APIInterface.post(
            route=delete_document_classifier_url,
            data=delete_document_classifier_request,
        )
        if status_code == 200:
            crud_request = {
                "model_id": request.DocumentClassifierArn,
                "status": "Deleted",
                "updated": datetime.now(),
            }
            self.CRUDModel.update(crud_request)
            return {"status": "classifier deleted"}
        else:
            # TODO: error
            pass
            return {"status": "deletion failed"}

    def describe_document_classifier_controller(self, request):
        describe_document_classifier_request = request.dict(exclude_none=True)
        describe_document_classifier_url = self.core_aws_comprehend_config.get(
            "describe_document_classifier"
        )
        response, status_code = APIInterface.post(
            route=describe_document_classifier_url,
            data=describe_document_classifier_request,
        )
        return response

    def stop_training_document_classifier_controller(self, request):
        stop_training_document_classifier_request = request.dict(exclude_none=True)
        stop_training_document_classifier_url = self.core_aws_comprehend_config.get(
            "stop_training_document_classifier"
        )
        response, status_code = APIInterface.post(
            route=stop_training_document_classifier_url,
            data=stop_training_document_classifier_request,
        )
        if status_code == 200:
            crud_request = {
                "model_id": request.DocumentClassifierArn,
                "status": "Stopped",
                "updated": datetime.now(),
            }
            self.CRUDModel.update(crud_request)
            return {"status": "training stopped"}
        else:
            # TODO: error
            pass
            return {"status": "training failed"}

    def list_document_classifier_controller(self):
        list_document_classifier_url = self.core_aws_comprehend_config.get(
            "list_document_classifier"
        )
        response, status_code = APIInterface.get(
            route=list_document_classifier_url,
        )
        return response

    def deploy_document_classifier_controller(self, request):
        uuid = str(int(datetime.now().timestamp()))
        deploy_document_classifier_request = request.dict(exclude_none=True)
        deploy_document_classifier_url = self.core_aws_comprehend_config.get(
            "deploy_document_classifier"
        )
        response, status_code = APIInterface.post(
            route=deploy_document_classifier_url,
            data=deploy_document_classifier_request,
        )
        deployment_crud_request = {
            "UUID": uuid,
            "model_id": request.model_arn,
            "deployment_endpoint": response.get("endpoint_arn"),
            "created": datetime.now(),
            "status": "Deployed",
        }
        if status_code == 200:
            self.CRUDDeployment.create(**deployment_crud_request)
            response.update({"status": "model deployed successfully"})
            return response
        else:
            # TODO: error
            pass
            return {"status": "model deployment failed"}

    def undeploy_document_classifier_controller(self, request):
        undeploy_document_classifier_request = request.dict(exclude_none=True)
        undeploy_document_classifier_url = self.core_aws_comprehend_config.get(
            "undeploy_document_classifier"
        )
        response, status_code = APIInterface.post(
            route=undeploy_document_classifier_url,
            data=undeploy_document_classifier_request,
        )
        undeployment_crud_request = {
            "deployment_endpoint": request.endpoint_arn,
            "updated": datetime.now(),
            "status": "UnDeployed",
        }
        if status_code == 200:
            self.CRUDDeployment.update_by_endpoint(
                deployment_request=undeployment_crud_request
            )
            return {"status": "model undeployed successfully"}
        else:
            # TODO: error
            pass
            return {"status": "model undeployment failed"}

    def get_predictions_controller(self, endpoint_arn: str, text: str):
        get_predictions_url = self.core_aws_comprehend_config.get("get_predictions")
        response, status_code = APIInterface.get(
            route=get_predictions_url,
            params={"endpoint_arn": endpoint_arn, "text": text},
        )
        return response