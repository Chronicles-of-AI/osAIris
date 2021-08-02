from utils.gcp.automl_manage_datasets import (
    list_datasets,
    delete_datasets,
    get_dataset_description,
)


class ManageDatasetController:
    def __init__(self):
        pass

    def list_datasets_controller(self, request):
        return list_datasets(
            project_id=request.project_id,
            region=request.region,
        )

    def get_dataset_description_controller(self, request):
        return get_dataset_description(
            project_id=request.project_id,
            region=request.region,
            dataset_id=request.dataset_id,
        )

    def delete_dataset_controller(self, request):
        return delete_datasets(
            project_id=request.project_id,
            region=request.region,
            dataset_id=request.dataset_id,
        )
