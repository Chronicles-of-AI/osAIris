from sql import session
from sql.orm_models.operations import Operations


class CRUDOperations:
    def create(self, **kwargs):
        project = Operations(**kwargs)
        with session() as transaction_session:
            transaction_session.add(project)
            transaction_session.commit()
            transaction_session.refresh(project)

    def delete():
        pass

    def read(self, operation_id: str):
        with session() as transaction_session:
            obj = (
                transaction_session.query(Operations)
                .filter(Operations.operation_id == operation_id)
                .first()
            )
        return obj.__dict__

    def update(self, operation_request):
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
