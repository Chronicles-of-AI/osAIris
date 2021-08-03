from fastapi import APIRouter, Depends, HTTPException, status
from typing import List, Optional
from sql.apis.schemas.requests.gcp.import_dataset_request import ImportDataset
from sql.apis.schemas.responses.gcp.import_dataset_response import ImportDatasetResponse
from sql.controllers.gcp.import_dataset_controller import ImportDatasetController
from fastapi.security import OAuth2PasswordBearer
from commons.auth import decodeJWT

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")

import_dataset_router = APIRouter()


@import_dataset_router.post(
    "/gcp/automl/import_dataset", response_model=ImportDatasetResponse
)
def import_dataset(
    import_dataset_request: ImportDataset,
    token: str = Depends(oauth2_scheme),
):
    if decodeJWT(token=token):
        response = ImportDatasetController().create_import_dataset_controller(
            request=import_dataset_request
        )
        return ImportDatasetResponse(**response)
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid access token",
            headers={"WWW-Authenticate": "Bearer"},
        )
