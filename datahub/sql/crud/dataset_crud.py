from sql import session
from sql.orm_models.datasets import CreateDataset


class CRUDDataset:
    def create(self, **kwargs):
        """[summary]

        Raises:
            error: [description]
        """
        try:
            project = CreateDataset(**kwargs)
            with session() as transaction_session:
                transaction_session.add(project)
                transaction_session.commit()
                transaction_session.refresh(project)
        except Exception as error:
            raise error

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
            raise error

    def read():
        pass

    def delete():
        pass
