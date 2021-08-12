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
from sql import logger

logging = logger(__name__)
user_router = APIRouter()


@user_router.post("/user/register", response_model=RegisterResponse)
def register_user(register_user_request: Register):
    """[API router to register new user into the system]

    Args:
        register_user_request (Register): [New user details]

    Raises:
        HTTPException: [Unauthorized exception when invalid token is passed]
        error: [Exception in underlying controller]

    Returns:
        [RegisterResponse]: [Register new user response]
    """
    try:
        logging.info("Calling /user/register endpoint")
        logging.debug(f"Request: {register_user_request}")
        user_obj = UserManagementController().register_user_controller(
            register_user_request
        )
        if user_obj.get("access_token") is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail=user_obj["status"]
            )
        else:
            return RegisterResponse(**user_obj)
    except Exception as error:
        logging.error(f"Error in /user/register endpoint: {error}")
        raise error


@user_router.post("/user/login", response_model=LoginResponse)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    """[API router to login existing user]

    Args:
        form_data (OAuth2PasswordRequestForm, optional): [User details to login the user]. Defaults to Depends().

    Raises:
        error: [Exception in underlying controller]

    Returns:
        [LoginResponse]: [Login response]
    """
    try:
        logging.info("Calling /user/login endpoint")
        valid_user = UserManagementController().login_user_controller(form_data)
        if not valid_user:
            raise HTTPException(
                status_code=400, detail="Incorrect username or password"
            )
        return LoginResponse(**valid_user)
    except Exception as error:
        logging.error(f"Error in /user/login endpoint: {error}")
        raise error
