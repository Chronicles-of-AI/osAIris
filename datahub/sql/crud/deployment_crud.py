from sql import session
from sql.orm_models.deployment import Deployment


class CRUDDeployment:
    def create(self, **kwargs):
        deployment = Deployment(**kwargs)
        with session() as transaction_session:
            transaction_session.add(deployment)
            transaction_session.commit()
            transaction_session.refresh(deployment)

    def upsert(self, deployment_request):
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

    def delete():
        pass

    def read(self, deployment_request):
        with session() as transaction_session:
            obj: Deployment = (
                transaction_session.query(Deployment)
                .filter(Deployment.model_id == deployment_request.get("model_id"))
                .first()
            )
            return obj.__dict__

    def update(self, deployment_request):
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

    def update_by_endpoint(self, deployment_request):
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
