from sql import session, logger
from sql.orm_models.data_import import DataImport

logging = logger(__name__)


class CRUDDataImport:
    def create(self, **kwargs):
        """[CRUD function to create a new Data Import record]

        Raises:
            error: [Error returned from the DB layer]
        """
        try:
            logging.info("CRUDDataImport create function")
            project = DataImport(**kwargs)
            with session() as transaction_session:
                transaction_session.add(project)
                transaction_session.commit()
                transaction_session.refresh(project)
        except Exception as error:
            logging.error(f"Error in CRUDDataImport create function : {error}")
            raise error

    def delete(self, dataset_id: str):
        """[CRUD function to delete a Data Import record]

        Args:
            dataset_id (str): [Unique identifier for the dataset record]

        Raises:
            error: [Error returned from the DB layer]
        """
        try:
            logging.info("CRUDDataImport delete function")
            with session() as transaction_session:
                obj: DataImport = (
                    transaction_session.query(DataImport)
                    .filter(DataImport.dataset_id == dataset_id)
                    .first()
                )
                if obj:
                    obj.status = "DELETED"
                    transaction_session.commit()
                    transaction_session.refresh(obj)
        except Exception as error:
            logging.error(f"Error in CRUDDataImport delete function : {error}")
            raise error

    def read():
        pass

    def update(self, dataset_id: str, status: str):
        """[CRUD function to update a Data Import record]

        Args:
            dataset_id (str): [Unique identifier for the dataset record]
            status (str): [Status of the data import record]

        Raises:
            error: [Error returned from the DB layer]
        """
        try:
            logging.info("CRUDDataImport update function")
            with session() as transaction_session:
                obj: DataImport = (
                    transaction_session.query(DataImport)
                    .filter(DataImport.dataset_id == dataset_id)
                    .first()
                )
                if obj:
                    obj.status = status
                    transaction_session.commit()
                    transaction_session.refresh(obj)
        except Exception as error:
            logging.error(f"Error in CRUDDataImport update function : {error}")
            raise error
