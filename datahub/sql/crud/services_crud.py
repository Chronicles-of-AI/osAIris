from sql import session, logger
from sql.orm_models.services import Services

logging = logger(__name__)


class CRUDServices:
    def create(self, **kwargs):
        """[CRUD function to create a new Services record]

        Raises:
            error: [Error returned from the DB layer]
        """
        try:
            logging.info("CRUDServices create function")
            project = Services(**kwargs)
            with session() as transaction_session:
                transaction_session.add(project)
                transaction_session.commit()
                transaction_session.refresh(project)
        except Exception as error:
            logging.error(f"Error in CRUDServices create function : {error}")
            raise error

    def delete():
        pass

    def read_all(self):
        """[CRUD function to read all Services]

        Raises:
            error: [Error returned from the DB layer]
        """
        try:
            logging.info("CRUDServices read function")
            with session() as transaction_session:
                obj: Services = transaction_session.query(Services).all()
            return [row.__dict__ for row in obj]
        except Exception as error:
            logging.error(f"Error in CRUDServices read function : {error}")
            raise error

    def read_service(self, cloud_service_provider: str, use_case: str):
        """[CRUD function to read a Services]

        Raises:
            error: [Error returned from the DB layer]
        """
        try:
            logging.info("CRUDServices read function")
            with session() as transaction_session:
                obj: Services = (
                    transaction_session.query(Services)
                    .filter(Services.cloud_service_provider == cloud_service_provider)
                    .filter(Services.use_case == use_case)
                    .first()
                )
            return obj.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDServices read function : {error}")
            raise error

    def update():
        pass
