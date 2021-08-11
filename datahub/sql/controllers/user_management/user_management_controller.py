import logging
from sql.crud.user_crud import CRUDUser
from commons.auth import encrypt_password, verify_hash_password, signJWT
from sql import logger

logging = logger(__name__)


class UserManagementController:
    def __init__(self):
        self.CRUDUser = CRUDUser()

    def register_user_controller(self, request):
        """[Controller to register new user]

        Args:
            request ([dict]): [create new user request]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [dict]: [authorization details]
        """
        try:
            logging.info("executing register new user function")
            password_hash = encrypt_password(password=request.password)
            user_obj = self.CRUDUser.read(user_name=request.user_name)
            if user_obj is not None:
                return {"access_token": None, "status": "User already exists"}
            user_request = {
                "user_name": request.user_name,
                "password": password_hash,
                "full_name": request.full_name,
                "email_id": request.email_id,
                "user_role": request.user_role,
            }
            self.CRUDUser.create(**user_request)
            access_token = signJWT(username=request.user_name)
            return {"access_token": access_token, "token_type": "bearer"}
        except Exception as error:
            logging.error(f"Error in register_user_controller function: {error}")
            raise error

    def login_user_controller(self, request):
        """[Controller for user login]

        Args:
            request ([dict]): [user login details]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [dict]: [authorization details]
        """
        try:
            logging.info("executing login user function")
            user_obj = self.CRUDUser.read(user_name=request.username)
            if verify_hash_password(
                plain_password=request.password,
                hashed_password=user_obj.get("password"),
            ):
                access_token = signJWT(username=request.username)
                return {"access_token": access_token, "token_type": "bearer"}
            else:
                return None
        except Exception as error:
            logging.error(f"Error in login_user_controller function: {error}")
            raise error
