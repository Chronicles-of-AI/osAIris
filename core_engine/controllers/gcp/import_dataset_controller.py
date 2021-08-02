from utils.gcp.automl_import_data import import_training_data


class ImportDatasetController:
    def __init__(self):
        pass

    def import_dataset_controller(self, request):
        return import_training_data(
            project_id=request.project_id,
            dataset_id=request.dataset_id,
            gcs_path=request.gcs_path,
            region=request.region,
        )
