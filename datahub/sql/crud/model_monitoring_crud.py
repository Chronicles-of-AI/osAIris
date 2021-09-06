from sql import session, logger
from sql.orm_models.model_monitoring import ModelMonitoring

logging = logger(__name__)


class CRUDModelMonitoring:
    def create(self, **kwargs):
        """[CRUD function to create a new Model Monitoring record]

        Raises:
            error: [Error returned from the DB layer]
        """
        try:
            logging.info("CRUDModelMonitoring create function")
            project = ModelMonitoring(**kwargs)
            with session() as transaction_session:
                transaction_session.add(project)
                transaction_session.commit()
                transaction_session.refresh(project)
        except Exception as error:
            logging.error(f"Error in CRUDModelMonitoring create function : {error}")
            raise error

    def delete(self, model_uri: str):
        """[CRUD function to delete a Model Monitoring record]

        Args:
            model_uri (str): [Unique identifier for the Model record]

        Raises:
            error: [Error returned from the DB layer]
        """
        try:
            logging.info("CRUDModelMonitoring delete function")
            with session() as transaction_session:
                obj: ModelMonitoring = (
                    transaction_session.query(ModelMonitoring)
                    .filter(ModelMonitoring.model_uri == model_uri)
                    .first()
                    .delete()
                )
        except Exception as error:
            logging.error(f"Error in CRUDModelMonitoring delete function : {error}")
            raise error

    def read(self, model_uri: str):
        """[CRUD function to Read a Model Monitoring record]

        Args:
            model_uri (str): [Unique identifier for the Model record]

        Raises:
            error: [Error returned from the DB layer]
        """
        try:
            logging.info("CRUDModelMonitoring Read function")
            with session() as transaction_session:
                obj: ModelMonitoring = (
                    transaction_session.query(ModelMonitoring)
                    .filter(ModelMonitoring.model_uri == model_uri)
                    .all()
                )
                return [row.__dict__ for row in obj]
        except Exception as error:
            logging.error(f"Error in CRUDModelMonitoring Read function : {error}")
            raise error

    def update(self, **kwargs):
        """[CRUD function to update a Model Monitoring record]

        Args:
            model_uri (str): [Unique identifier for the Model record]

        Raises:
            error: [Error returned from the DB layer]
        """
        try:
            logging.info("CRUDModelMonitoring update function")
            with session() as transaction_session:
                obj: ModelMonitoring = (
                    transaction_session.query(ModelMonitoring)
                    .filter(ModelMonitoring.model_uri == kwargs.get("model_uri"))
                    .update(kwargs)
                )
                transaction_session.commit()
        except Exception as error:
            logging.error(f"Error in CRUDModelMonitoring update function : {error}")
            raise error
