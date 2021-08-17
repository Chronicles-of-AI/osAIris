from core_engine.utils.gcp.automl_import_data import import_training_data
from core_engine import logger

logging = logger(__name__)


class ImportDatasetController:
    def __init__(self):
        pass

    def import_dataset_controller(self, request):
        """[summary]

        Args:
            request ([type]): [Based on the Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [description]
        """
        try:
            logging.info(f"Import Dataset Controller: {request}")
            return import_training_data(
                project_id=request.project_id,
                dataset_id=request.dataset_id,
                gcs_path=request.gcs_path,
                region=request.region,
            )
        except Exception as error:
            logging.error(f"{error=}")
            raise error
