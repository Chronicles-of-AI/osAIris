from sql import session, logger
from sql.orm_models.deployment import Deployment

logging = logger(__name__)


class CRUDDeployment:
    def create(self, **kwargs):
        """[CRUD function to create a new Deployment record]

        Raises:
            error: [Error returned from the DB layer]
        """
        try:
            logging.info("CRUDDeployment create function")
            deployment = Deployment(**kwargs)
            with session() as transaction_session:
                transaction_session.add(deployment)
                transaction_session.commit()
                transaction_session.refresh(deployment)
        except Exception as error:
            logging.error(f"Error in CRUDDeployment create function : {error}")
            raise error

    def upsert(self, deployment_request):
        """[CRUD function to upsert a Deployment record]

        Args:
            deployment_request ([dict]): [deployment request to be updated]

        Raises:
            error: [Error returned from the DB layer]
        """
        try:
            logging.info("CRUDDeployment upsert function")
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
            logging.error(f"Error in CRUDDeployment upsert function : {error}")
            raise error

    def delete():
        pass

    def read(self, deployment_request):
        """[CRUD function to read a Deployment record]

        Args:
            deployment_request ([dict]): [deployment request to be read]

        Raises:
            error: [Error returned from the DB layer]

        Returns:
            [dict]: [deployment request matching the model id]
        """
        try:
            logging.info("CRUDDeployment read function")
            with session() as transaction_session:
                obj: Deployment = (
                    transaction_session.query(Deployment)
                    .filter(Deployment.model_id == deployment_request.get("model_id"))
                    .first()
                )
                return obj.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDDeployment read function : {error}")
            raise error

    def update(self, deployment_request):
        """[CRUD function to update a Deployment record]

        Args:
            deployment_request ([dict]): [deployment request to be updated]

        Raises:
            error: [Error returned from the DB layer]
        """
        try:
            logging.info("CRUDDeployment update function")
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
            logging.error(f"Error in CRUDDeployment update function : {error}")
            raise error

    def update_by_endpoint(self, deployment_request):
        """[CRUD function to update a Deployment record by endpoint]

        Args:
            deployment_request ([dict]): [deployment request to be updated]

        Raises:
            error: [Error returned from the DB layer]
        """
        try:
            logging.info("CRUDDeployment update_by_endpoint function")
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
            logging.error(
                f"Error in CRUDDeployment update_by_endpoint function : {error}"
            )
            raise error
