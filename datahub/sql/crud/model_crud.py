from sql import session
from sql.orm_models.models import Models


class CRUDModel:
    def create(self, **kwargs):
        """[summary]

        Raises:
            error: [description]
        """
        try:
            model = Models(**kwargs)
            with session() as transaction_session:
                transaction_session.add(model)
                transaction_session.commit()
                transaction_session.refresh(model)
        except Exception as error:
            raise error

    def delete():
        pass

    def read(self, model_request):
        """[summary]

        Args:
            model_request ([type]): [description]

        Raises:
            error: [description]

        Returns:
            [type]: [description]
        """
        try:
            with session() as transaction_session:
                obj = (
                    transaction_session.query(Models)
                    .filter(Models.model_id == model_request.get("model_id"))
                    .first()
                )
            return obj.__dict__
        except Exception as error:
            raise error

    def update(self, model_request):
        """[summary]

        Args:
            model_request ([type]): [description]

        Raises:
            error: [description]
        """
        try:
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
        except Exception as error:
            raise error

    def update_by_alias_name(self, model_request):
        """[summary]

        Args:
            model_request ([type]): [description]

        Raises:
            error: [description]
        """
        try:
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
        except Exception as error:
            raise error

    def update_by_operation_id(self, model_request):
        """[summary]

        Args:
            model_request ([type]): [description]

        Raises:
            error: [description]
        """
        try:
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
        except Exception as error:
            raise error
