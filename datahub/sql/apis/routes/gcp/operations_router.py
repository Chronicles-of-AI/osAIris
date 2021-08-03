from fastapi import APIRouter, Depends, HTTPException, status
from sql.controllers.gcp.operations_controller import OperationsController
from sql.apis.schemas.responses.gcp.operations_response import OperationsResponse
from fastapi.security import OAuth2PasswordBearer
from commons.auth import decodeJWT

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")

operations_router = APIRouter()


@operations_router.get(
    "/gcp/automl/get_operation_details", response_model=OperationsResponse
)
def get_operations(
    operation_id: str,
    token: str = Depends(oauth2_scheme),
):
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
