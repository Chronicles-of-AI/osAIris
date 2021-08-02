from sql import session
from sql.orm_models.models import Models


class CRUDModel:
    def create(self, **kwargs):
        model = Models(**kwargs)
        with session() as transaction_session:
            transaction_session.add(model)
            transaction_session.commit()
            transaction_session.refresh(model)

    def delete():
        pass

    def read(self, model_request):
        with session() as transaction_session:
            obj = (
                transaction_session.query(Models)
                .filter(Models.model_id == model_request.get("model_id"))
                .first()
            )
        return obj.__dict__

    def update(self, model_request):
        print(f"CRUDModel update request : {model_request}")
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

    def update_by_alias_name(self, model_request):
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

    def update_by_operation_id(self, model_request):
        print(f"CRUDModel update_by_operation_id request : {model_request}")
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
