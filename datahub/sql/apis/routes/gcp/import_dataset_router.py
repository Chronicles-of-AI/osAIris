from fastapi import APIRouter
from typing import List, Optional
from sql.apis.schemas.requests.gcp.import_dataset_request import ImportDataset
from sql.controllers.gcp.import_dataset_controller import ImportDatasetController

import_dataset_router = APIRouter()


@import_dataset_router.post("/gcp/automl/import_dataset")
def import_dataset(
    import_dataset_request: ImportDataset,
):
    return ImportDatasetController().create_import_dataset_controller(
        request=import_dataset_request
    )
