from fastapi import APIRouter, HTTPException, status, Depends
from sql.apis.schemas.requests.user_management.user_request import Register
from sql.controllers.user_management.user_management_controller import (
    UserManagementController,
)
from sql.apis.schemas.responses.user_management.user_response import (
    RegisterResponse,
    LoginResponse,
)
from fastapi.security import OAuth2PasswordRequestForm

user_router = APIRouter()


@user_router.post("/user/register", response_model=RegisterResponse)
def register_user(register_user_request: Register):
    user_obj = UserManagementController().register_user_controller(
        register_user_request
    )
    if user_obj.get("access_token") is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=user_obj["status"]
        )
    else:
        return RegisterResponse(**user_obj)


@user_router.post("/user/login", response_model=LoginResponse)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    valid_user = UserManagementController().login_user_controller(form_data)
    if not valid_user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    return LoginResponse(**valid_user)
