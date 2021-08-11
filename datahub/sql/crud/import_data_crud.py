from sql import session
from sql.orm_models.data_import import DataImport


class CRUDDataImport:
    def create(self, **kwargs):
        """[summary]

        Raises:
            error: [description]
        """
        try:
            project = DataImport(**kwargs)
            with session() as transaction_session:
                transaction_session.add(project)
                transaction_session.commit()
                transaction_session.refresh(project)
        except Exception as error:
            raise error

    def delete(self, dataset_id: str):
        """[summary]

        Args:
            dataset_id (str): [description]

        Raises:
            error: [description]
        """
        try:
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
            raise error

    def read():
        pass

    def update(self, dataset_id: str, status: str):
        """[summary]

        Args:
            dataset_id (str): [description]
            status (str): [description]

        Raises:
            error: [description]
        """
        try:
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
            raise error
