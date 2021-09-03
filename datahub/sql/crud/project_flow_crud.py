from sql import session, logger
from sql.orm_models.project_flow import ProjectFlow

logging = logger(__name__)


class CRUDProjectFlow:
    def create(self, **kwargs):
        """[CRUD function to create a new Project Flow record]

        Raises:
            error: [Error returned from the DB layer]
        """
        try:
            logging.info("CRUDProjectFlow create function")
            project = ProjectFlow(**kwargs)
            with session() as transaction_session:
                transaction_session.add(project)
                transaction_session.commit()
                transaction_session.refresh(project)
        except Exception as error:
            logging.error(f"Error in CRUDProjectFlow create function : {error}")
            raise error

    def delete(self, pipeline_name: str):
        """[CRUD function to delete a Project Flow record]

        Args:
            dataset_id (str): [Unique identifier for the Project Flow record]

        Raises:
            error: [Error returned from the DB layer]
        """
        try:
            logging.info("CRUDProjectFlow delete function")
            with session() as transaction_session:
                obj: ProjectFlow = (
                    transaction_session.query(ProjectFlow)
                    .filter(ProjectFlow.pipeline_name == pipeline_name)
                    .first()
                    .delete()
                )
                transaction_session.commit()
                transaction_session.refresh(obj)
        except Exception as error:
            logging.error(f"Error in CRUDProjectFlow delete function : {error}")
            raise error

    def read_all(self):
        """[CRUD function to Read all Project Flow]

        Raises:
            error: [Error returned from the DB layer]
        """
        try:
            logging.info("CRUDProjectFlow Read All function")
            with session() as transaction_session:
                obj: ProjectFlow = transaction_session.query(ProjectFlow).all()
                return [row.__dict__ for row in obj]
        except Exception as error:
            logging.error(f"Error in CRUDProjectFlow Read aLL function : {error}")
            raise error

    def read(self, pipeline_name: str):
        """[CRUD function to Read a Project Flow]

        Args:
            pipeline_name (str): [Unique identifier for the Project Flow record]

        Raises:
            error: [Error returned from the DB layer]
        """
        try:
            logging.info("CRUDProjectFlow delete function")
            with session() as transaction_session:
                obj: ProjectFlow = (
                    transaction_session.query(ProjectFlow)
                    .filter(ProjectFlow.pipeline_name == pipeline_name)
                    .first()
                )
                return obj.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDProjectFlow Read function : {error}")
            raise error

    def read_by_model_id(self, model_id: str):
        """[CRUD function to Read a Project Flow]

        Args:
            pipeline_name (str): [Unique identifier for the Project Flow record]

        Raises:
            error: [Error returned from the DB layer]
        """
        try:
            logging.info("CRUDProjectFlow delete function")
            with session() as transaction_session:
                obj: ProjectFlow = (
                    transaction_session.query(ProjectFlow)
                    .filter(ProjectFlow.model_id == model_id)
                    .first()
                )
                return obj.__dict__
        except Exception as error:
            logging.error(f"Error in CRUDProjectFlow Read function : {error}")
            raise error

    def update(self, **kwargs):
        """[CRUD function to update a Project Flow record]

        Raises:
            error: [Error returned from the DB layer]
        """
        try:
            logging.info("CRUDProjectFlow update function")
            with session() as transaction_session:
                obj: ProjectFlow = (
                    transaction_session.query(ProjectFlow)
                    .filter(ProjectFlow.pipeline_name == kwargs.get("pipeline_name"))
                    .first()
                    .update(kwargs)
                )
                transaction_session.commit()
                transaction_session.refresh(obj)
        except Exception as error:
            logging.error(f"Error in CRUDProjectFlow update function : {error}")
            raise error

    def update_by_functional_id(self, **kwargs):
        """[CRUD function to update a Project Flow record]

        Raises:
            error: [Error returned from the DB layer]
        """
        try:
            logging.info("CRUDProjectFlow update function")
            with session() as transaction_session:
                obj: ProjectFlow = (
                    transaction_session.query(ProjectFlow)
                    .filter(
                        ProjectFlow.functional_stage_id
                        == kwargs.get("functional_stage_id")
                    )
                    .first()
                    .update(kwargs)
                )
                transaction_session.commit()
                transaction_session.refresh(obj)
        except Exception as error:
            logging.error(f"Error in CRUDProjectFlow update function : {error}")
            raise error
