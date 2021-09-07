from sql import session, logger
from sql.orm_models.data_monitoring import DataMonitoring

logging = logger(__name__)


class CRUDDataMonitoring:
    def create(self, **kwargs):
        """[CRUD function to create a new Data Monitoring record]

        Raises:
            error: [Error returned from the DB layer]
        """
        try:
            logging.info("CRUDDataMonitoring create function")
            project = DataMonitoring(**kwargs)
            with session() as transaction_session:
                transaction_session.add(project)
                transaction_session.commit()
                transaction_session.refresh(project)
        except Exception as error:
            logging.error(f"Error in CRUDDataMonitoring create function : {error}")
            raise error

    def delete(self, model_uri: str):
        """[CRUD function to Delete all Data Monitoring records for a Model URI]

        Args:
            model_uri (str): [Unique identifier for the annotation record]

        Raises:
            error: [Error returned from the DB layer]

        Returns:
            [type]: [List of all Data inferred and passed to the engine]
        """
        try:
            logging.info("CRUDDataMonitoring Delete function")
            with session() as transaction_session:
                obj: DataMonitoring = (
                    transaction_session.query(DataMonitoring)
                    .filter(DataMonitoring.model_uri == model_uri)
                    .all()
                    .delete()
                )
        except Exception as error:
            logging.error(f"Error in CRUDDataMonitoring Delete function : {error}")
            raise error

    def read(self, model_uri: str):
        """[CRUD function to Read all Data Monitoring records for a Model URI]

        Args:
            model_uri (str): [Unique identifier for the annotation record]

        Raises:
            error: [Error returned from the DB layer]

        Returns:
            [type]: [List of all Data inferred and passed to the engine]
        """
        try:
            logging.info("CRUDDataMonitoring Read function")
            with session() as transaction_session:
                obj: DataMonitoring = (
                    transaction_session.query(DataMonitoring)
                    .filter(DataMonitoring.model_uri == model_uri)
                    .all()
                )
                return [row.__dict__ for row in obj]
        except Exception as error:
            logging.error(f"Error in CRUDDataMonitoring Read function : {error}")
            raise error

    def update(self, annotation_task_id: str, ground_truth: str):
        """[CRUD function to update a Data Monitoring record]

        Args:
            annotation_task_id (str): [Unique identifier for the annotation record]
            ground_truth (str): [Ground Truth by Label Studio]

        Raises:
            error: [Error returned from the DB layer]
        """
        try:
            logging.info("CRUDDataMonitoring update function")
            with session() as transaction_session:
                obj: DataMonitoring = (
                    transaction_session.query(DataMonitoring)
                    .filter(DataMonitoring.annotation_task_id == annotation_task_id)
                    .first()
                )
                if obj:
                    obj.ground_truth = ground_truth
                    transaction_session.commit()
                    transaction_session.refresh(obj)
        except Exception as error:
            logging.error(f"Error in CRUDDataMonitoring update function : {error}")
            raise error
