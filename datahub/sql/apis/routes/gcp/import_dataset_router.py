from fastapi import APIRouter, Depends, HTTPException, status
from typing import List, Optional
from sql.apis.schemas.requests.gcp.import_dataset_request import ImportDataset
from sql.apis.schemas.responses.gcp.import_dataset_response import ImportDatasetResponse
from sql.controllers.gcp.import_dataset_controller import ImportDatasetController
from fastapi.security import OAuth2PasswordBearer
from commons.auth import decodeJWT
from sql import logger

logging = logger(__name__)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")
import_dataset_router = APIRouter()


@import_dataset_router.post(
    "/gcp/automl/import_dataset", response_model=ImportDatasetResponse
)
def import_dataset(
    import_dataset_request: ImportDataset,
    token: str = Depends(oauth2_scheme),
):
    """[API router to import dataset to AutoML]

    Args:
        import_dataset_request (ImportDataset): [AutoML import dataset request]
        token (str, optional): [Bearer token for authentication]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized exception when invalid token is passed]
        error: [Exception in underlying controller]

    Returns:
        [ImportDatasetResponse]: [AutoML import dataset response]
    """
    try:
        logging.info("Calling /gcp/automl/import_dataset endpoint")
        logging.debug(f"Request: {import_dataset_request}")
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
    except Exception as error:
        logging.error(f"Error in /gcp/automl/import_dataset endpoint: {error}")
        raise error
