from fastapi import APIRouter, Query
from typing import List, Optional
from apis.schemas.requests.gcp.import_dataset_request import ImportDataset
from controllers.gcp.import_dataset_controller import ImportDatasetController
from core_engine import logger

logging = logger(__name__)

import_dataset_router = APIRouter()


@import_dataset_router.post("/gcp/automl/import_dataset")
def import_dataset(
    import_dataset_request: ImportDataset,
):
    """[Import Dataset into AutoML Router]

    Args:
        import_dataset_request (ImportDataset): [Based on Schema]

    Raises:
        error: [Error]

    Returns:
        [type]: [description]
    """
    try:
        logging.info(f"Import Dataset Router: {import_dataset_request}")
        return ImportDatasetController().import_dataset_controller(
            request=import_dataset_request
        )
    except Exception as error:
        logging.error(f"{error=}")
        raise error
