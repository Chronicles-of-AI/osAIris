from sql import session
from sql.orm_models.data_import import DataImport


class CRUDDataImport:
    def create(self, **kwargs):
        project = DataImport(**kwargs)
        with session() as transaction_session:
            transaction_session.add(project)
            transaction_session.commit()
            transaction_session.refresh(project)

    def delete(self, dataset_id: str):
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

    def read():
        pass

    def update(self, dataset_id: str, status: str):
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
