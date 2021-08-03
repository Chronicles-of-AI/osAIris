from fastapi import APIRouter, Depends
from sql.controllers.gcp.operations_controller import OperationsController
from fastapi.security import OAuth2PasswordBearer
from commons.auth import decodeJWT

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")

operations_router = APIRouter()


@operations_router.get("/gcp/automl/get_operation_details")
def get_operations(
    operation_id: str,
    token: str = Depends(oauth2_scheme),
):
    return OperationsController().get_operation_details_controller(
        operation_id=operation_id
    )
