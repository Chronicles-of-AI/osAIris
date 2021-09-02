from sql import session, logger
from sql.orm_models.datasets import CreateDataset

logging = logger(__name__)


class CRUDDataset:
    def create(self, **kwargs):
        """[CRUD function to create a new Dataset record]

        Raises:
            error: [Error returned from the DB layer]
        """
        try:
            logging.info("CRUDDataset create function")
            project = CreateDataset(**kwargs)
            with session() as transaction_session:
                transaction_session.add(project)
                transaction_session.commit()
                transaction_session.refresh(project)
        except Exception as error:
            logging.error(f"Error in CRUDDataset create function : {error}")
            raise error

    def update(self, dataset_id: str, status: str):
        """[CRUD function to update a dataset record on DB]

        Args:
            dataset_id (str): [Unique identifier for dataset record]
            status (str): [Status of the dataset record]

        Raises:
            error: [Error returned from the DB layer]
        """
        try:
            logging.info("CRUDDataset update function")
            with session() as transaction_session:
                obj: CreateDataset = (
                    transaction_session.query(CreateDataset)
                    .filter(CreateDataset.dataset_id == dataset_id)
                    .first()
                )
                if obj:
                    obj.status = status
                    transaction_session.commit()
                    transaction_session.refresh(obj)
        except Exception as error:
            logging.error(f"Error in CRUDDataset update function : {error}")
            raise error

    def read():
        pass

    def delete():
        pass
