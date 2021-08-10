from sql.crud.user_crud import CRUDUser
from commons.auth import encrypt_password, verify_hash_password, signJWT


class UserManagementController:
    def __init__(self):
        self.CRUDUser = CRUDUser()

    def register_user_controller(self, request):
        """[summary]

        Args:
            request ([type]): [description]

        Raises:
            error: [description]

        Returns:
            [type]: [description]
        """
        try:
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
            raise error

    def login_user_controller(self, request):
        """[summary]

        Args:
            request ([type]): [description]

        Raises:
            error: [description]

        Returns:
            [type]: [description]
        """
        try:
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
            raise error
