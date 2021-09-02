from sql import session, logger
from sql.orm_models.operations import Operations

logging = logger(__name__)


class CRUDOperations:
    def create(self, **kwargs):
        """[CRUD function to create a new Operation record]

        Raises:
            error: [Error returned from the DB layer]
        """
        try:
            logging.info("CRUDOperations create function")
            project = Operations(**kwargs)
            with session() as transaction_session:
                transaction_session.add(project)
                transaction_session.commit()
                transaction_session.refresh(project)
        except Exception as error:
            logging.error(f"Error in CRUDOperations create function : {error}")
            raise error

    def delete():
        pass

    def read(self, operation_id: str):
        """[CRUD function to read an Operation record]

        Args:
            operation_id (str): [Unique identifier for an operations record]

        Raises:
            error: [Error returned from the DB layer]

        Returns:
            [dict]: [Operations record matching operation id]
        """
        try:
            logging.info("CRUDOperations read function")
            with session() as transaction_session:
                obj = (
                    transaction_session.query(Operations)
                    .filter(Operations.operation_id == operation_id)
                    .first()
                )
            return obj.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDOperations read function : {error}")
            raise error

    def update(self, operation_request):
        """[CRUD function to update an Operation record]

        Args:
            operation_request ([dict]): [operation request to be updated]

        Raises:
            error: [Error returned from the DB layer]
        """
        try:
            logging.info("CRUDOperations update function")
            with session() as transaction_session:
                obj: Operations = (
                    transaction_session.query(Operations)
                    .filter(
                        Operations.operation_id == operation_request.get("operation_id")
                    )
                    .first()
                )
                if obj:
                    obj.status = operation_request.get("status")
                    obj.updated = operation_request.get("updated")
                    obj.error = operation_request.get("error")
                    transaction_session.commit()
                    transaction_session.refresh(obj)
        except Exception as error:
            logging.error(f"Error in CRUDOperations update function : {error}")
            raise error
