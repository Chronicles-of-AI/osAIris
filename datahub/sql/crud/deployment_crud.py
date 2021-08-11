from os import error
from sql import session
from sql.orm_models.deployment import Deployment


class CRUDDeployment:
    def create(self, **kwargs):
        """[summary]

        Raises:
            error: [description]
        """
        try:
            deployment = Deployment(**kwargs)
            with session() as transaction_session:
                transaction_session.add(deployment)
                transaction_session.commit()
                transaction_session.refresh(deployment)
        except Exception as error:
            raise error

    def upsert(self, deployment_request):
        """[summary]

        Args:
            deployment_request ([type]): [description]

        Raises:
            error: [description]
        """
        try:
            deployment = Deployment(deployment_request)
            obj = self.read(deployment_request=deployment_request)
            with session() as transaction_session:
                if obj:
                    obj.status = deployment_request.get("status", None)
                    obj.deployment_endpoint = deployment_request.get(
                        "deployment_endpoint", None
                    )
                    obj.updated = deployment_request.get("updated", None)
                    transaction_session.commit()
                    transaction_session.refresh(obj)
                else:
                    transaction_session.add(deployment)
                    transaction_session.commit()
                    transaction_session.refresh(deployment)
        except Exception as error:
            raise error

    def delete():
        pass

    def read(self, deployment_request):
        """[summary]

        Args:
            deployment_request ([type]): [description]

        Raises:
            error: [description]

        Returns:
            [type]: [description]
        """
        try:
            with session() as transaction_session:
                obj: Deployment = (
                    transaction_session.query(Deployment)
                    .filter(Deployment.model_id == deployment_request.get("model_id"))
                    .first()
                )
                return obj.__dict__
        except Exception as error:
            raise error

    def update(self, deployment_request):
        """[summary]

        Args:
            deployment_request ([type]): [description]

        Raises:
            error: [description]
        """
        try:
            with session() as transaction_session:
                obj: Deployment = (
                    transaction_session.query(Deployment)
                    .filter(Deployment.model_id == deployment_request.get("model_id"))
                    .first()
                )
                if obj:
                    obj.status = deployment_request.get("status", None)
                    obj.deployment_endpoint = deployment_request.get(
                        "deployment_endpoint", None
                    )
                    obj.updated = deployment_request.get("updated", None)
                    transaction_session.commit()
                    transaction_session.refresh(obj)
        except Exception as error:
            raise error

    def update_by_endpoint(self, deployment_request):
        """[summary]

        Args:
            deployment_request ([type]): [description]

        Raises:
            error: [description]
        """
        try:
            with session() as transaction_session:
                obj: Deployment = (
                    transaction_session.query(Deployment)
                    .filter(
                        Deployment.deployment_endpoint
                        == deployment_request.get("deployment_endpoint")
                    )
                    .first()
                )
                if obj:
                    obj.status = deployment_request.get("status", None)
                    obj.updated = deployment_request.get("updated", None)
                    transaction_session.commit()
                    transaction_session.refresh(obj)
        except Exception as error:
            raise error
