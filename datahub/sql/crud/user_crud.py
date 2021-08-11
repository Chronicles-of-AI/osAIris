import logging
from sql import session, logger
from sql.orm_models.user import User

logging = logger(__name__)


class CRUDUser:
    def create(self, **kwargs):
        """[CRUD function to create a new User record]

        Raises:
            error: [Error returned from the DB layer]
        """
        try:
            logging.info("CRUDUser create request")
            user = User(**kwargs)
            with session() as transaction_session:
                transaction_session.add(user)
                transaction_session.commit()
                transaction_session.refresh(user)
        except Exception as error:
            logging.error(f"Error in CRUDUser create function : {error}")
            raise error

    def read(self, user_name: str):
        """[CRUD function to read a User record]

        Args:
            user_name (str): [User name to filter the record]

        Raises:
            error: [Error returned from the DB layer]

        Returns:
            [dict]: [user record matching the criteria]
        """
        try:
            logging.info("CRUDUser read request")
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
            logging.error(f"Error in CRUDUser read function : {error}")
            raise error

    def update():
        pass

    def delete():
        pass
