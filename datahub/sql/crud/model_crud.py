from sql import session, logger
from sql.orm_models.models import Models

logging = logger(__name__)


class CRUDModel:
    def create(self, **kwargs):
        """[CRUD function to create a new Model record]

        Raises:
            error: [Error returned from the DB layer]
        """
        try:
            logging.info("CRUDModel create function")
            model = Models(**kwargs)
            with session() as transaction_session:
                transaction_session.add(model)
                transaction_session.commit()
                transaction_session.refresh(model)
        except Exception as error:
            logging.error(f"Error in CRUDModel create function : {error}")
            raise error

    def delete():
        pass

    def read(self, model_request):
        """[CRUD function to read a Model record]

        Args:
            model_request ([dict]): [model data request]

        Raises:
            error: [Error returned from the DB layer]

        Returns:
            [dict]: [model record matching the model id]
        """
        try:
            logging.info("CRUDModel read function")
            with session() as transaction_session:
                obj = (
                    transaction_session.query(Models)
                    .filter(Models.model_id == model_request.get("model_id"))
                    .first()
                )
            return obj.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDModel read function : {error}")
            raise error

    def update(self, model_request):
        """[CRUD function to read a Model record]

        Args:
            model_request ([dict]): [model data request]

        Raises:
            error: [Error returned from the DB layer]
        """
        try:
            logging.info("CRUDModel update function")
            with session() as transaction_session:
                obj: Models = (
                    transaction_session.query(Models)
                    .filter(Models.model_id == model_request.get("model_id"))
                    .first()
                )
                if obj:
                    obj.status = model_request.get("status", None)
                    obj.updated = model_request.get("updated", None)
                    transaction_session.commit()
                    transaction_session.refresh(obj)
        except Exception as error:
            logging.error(f"Error in CRUDModel update function : {error}")
            raise error

    def update_by_alias_name(self, model_request):
        """[CRUD function to update a Model record by alias name]

        Args:
            model_request ([dict]): [model data request]

        Raises:
            error: [Error returned from the DB layer]
        """
        try:
            logging.info("CRUDModel update_by_alias_name function")
            with session() as transaction_session:
                obj: Models = (
                    transaction_session.query(Models)
                    .filter(Models.alias_name == model_request.get("alias_name"))
                    .first()
                )
                if obj:
                    obj.status = model_request.get("status", None)
                    obj.updated = model_request.get("updated", None)
                    transaction_session.commit()
                    transaction_session.refresh(obj)
        except Exception as error:
            logging.error(f"Error in CRUDModel update_by_alias_name function : {error}")
            raise error

    def update_by_operation_id(self, model_request):
        """[CRUD function to update a Model record by operation id]

        Args:
            model_request ([dict]): [model data request]

        Raises:
            error: [Error returned from the DB layer]
        """
        try:
            logging.info("CRUDModel update_by_alias_name function")
            with session() as transaction_session:
                obj: Models = (
                    transaction_session.query(Models)
                    .filter(Models.model_id == model_request.get("operation_id"))
                    .first()
                )
                if obj:
                    obj.model_id = model_request.get("model_id")
                    obj.status = model_request.get("status", None)
                    obj.updated = model_request.get("updated", None)
                    transaction_session.commit()
                    transaction_session.refresh(obj)
        except Exception as error:
            logging.error(
                f"Error in CRUDModel update_by_operation_id function : {error}"
            )
            raise error
