from fastapi import APIRouter, Depends, HTTPException, status
from sql.controllers.gcp.operations_controller import OperationsController
from sql.apis.schemas.responses.gcp.operations_response import OperationsResponse
from fastapi.security import OAuth2PasswordBearer
from commons.auth import decodeJWT
from sql import logger

logging = logger(__name__)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")

operations_router = APIRouter()


@operations_router.get(
    "/gcp/automl/get_operation_details", response_model=OperationsResponse
)
async def get_operations(
    operation_id: str,
    token: str = Depends(oauth2_scheme),
):
    """[API router to get operation details]

    Args:
        operation_id (str): [Unique id for the long running operation]
        token (str, optional): [Bearer token for authentication]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized exception when invalid token is passed]
        error: [Exception in underlying controller]

    Returns:
        [OperationsResponse]: [Long running operation details]
    """
    try:
        logging.info("Calling /gcp/automl/get_operation_details endpoint")
        logging.debug(f"Request: {operation_id=}")
        if decodeJWT(token=token):
            response = OperationsController().get_operation_details_controller(
                operation_id=operation_id
            )
            return OperationsResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /gcp/automl/get_operation_details endpoint: {error}")
        raise error
