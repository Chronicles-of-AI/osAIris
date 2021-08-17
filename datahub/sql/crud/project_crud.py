import logging
from sql import session, logger
from sql.orm_models.projects import CreateProject

logging = logger(__name__)


class CRUDProject:
    def create(self, **kwargs):
        """[CRUD function to create a new Project record]

        Raises:
            error: [Error returned from the DB layer]
        """
        try:
            logging.info("CRUDProject create function")
            project = CreateProject(**kwargs)
            with session() as transaction_session:
                transaction_session.add(project)
                transaction_session.commit()
                transaction_session.refresh(project)
        except Exception as error:
            logging.error(f"Error in CRUDProject create function : {error}")
            raise error

    def delete(self, project_arn: str):
        """[CRUD function to delete a Project record]

        Args:
            project_arn (str): [Unique identifier for project created]

        Raises:
            error: [Error returned from the DB layer]
        """
        try:
            logging.info("CRUDProject delete function")
            with session() as transaction_session:
                obj: CreateProject = (
                    transaction_session.query(CreateProject)
                    .filter(CreateProject.project_arn == project_arn)
                    .first()
                )
                if obj:
                    obj.status = "DELETED"
                    transaction_session.commit()
                    transaction_session.refresh(obj)
        except Exception as error:
            logging.error(f"Error in CRUDProject delete function : {error}")
            raise error

    def read():
        pass

    def update():
        pass
