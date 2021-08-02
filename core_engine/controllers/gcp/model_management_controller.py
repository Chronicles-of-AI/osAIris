from utils.gcp.automl_manage_model import (
    model_deployment,
    model_undeployment,
    get_model_description,
    delete_model,
)
from utils.gcp.automl_list_models import list_models


class ManageModelController:
    def __init__(self):
        pass

    def deploy_model_controller(self, request):
        return model_deployment(
            project_id=request.project_id,
            model_id=request.model_id,
            region=request.region,
        )

    def undeploy_model_controller(self, request):
        return model_undeployment(
            project_id=request.project_id,
            model_id=request.model_id,
            region=request.region,
        )

    def list_model_controller(self, request):
        return list_models(
            project_id=request.project_id,
            region=request.region,
            dataset_id=request.dataset_id,
        )

    def get_model_description_controller(self, request):
        return get_model_description(
            project_id=request.project_id,
            region=request.region,
            model_id=request.model_id,
        )

    def delete_model_controller(self, request):
        return delete_model(
            project_id=request.project_id,
            region=request.region,
            model_id=request.model_id,
        )
