from sql import session
from sql.orm_models.user import User


class CRUDUser:
    def create(self, **kwargs):
        """[summary]

        Raises:
            error: [description]
        """
        try:
            user = User(**kwargs)
            with session() as transaction_session:
                transaction_session.add(user)
                transaction_session.commit()
                transaction_session.refresh(user)
        except Exception as error:
            raise error

    def read(self, user_name: str):
        """[summary]

        Args:
            user_name (str): [description]

        Raises:
            error: [description]

        Returns:
            [type]: [description]
        """
        try:
            with session() as transaction_session:
                obj: User = (
                    transaction_session.query(User)
                    .filter(User.user_name == user_name)
                    .first()
                )
            if obj is not None:
                return obj.__dict__
            else:
                return None
        except Exception as error:
            raise error

    def update():
        pass

    def delete():
        pass
