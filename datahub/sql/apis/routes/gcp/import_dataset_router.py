from fastapi import APIRouter, Depends
from typing import List, Optional
from sql.apis.schemas.requests.gcp.import_dataset_request import ImportDataset
from sql.controllers.gcp.import_dataset_controller import ImportDatasetController
from fastapi.security import OAuth2PasswordBearer
from commons.auth import decodeJWT

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")

import_dataset_router = APIRouter()


@import_dataset_router.post("/gcp/automl/import_dataset")
def import_dataset(
    import_dataset_request: ImportDataset,
    token: str = Depends(oauth2_scheme),
):
    return ImportDatasetController().create_import_dataset_controller(
        request=import_dataset_request
    )
