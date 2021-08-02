from sql import session
from sql.orm_models.datasets import CreateDataset


class CRUDDataset:
    def create(self, **kwargs):
        project = CreateDataset(**kwargs)
        with session() as transaction_session:
            transaction_session.add(project)
            transaction_session.commit()
            transaction_session.refresh(project)

    def update(self, dataset_id: str, status: str):
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

    def read():
        pass

    def delete():
        pass
