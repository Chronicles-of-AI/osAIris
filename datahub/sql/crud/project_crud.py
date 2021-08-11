from sql import session
from sql.orm_models.projects import CreateProject


class CRUDProject:
    def create(self, **kwargs):
        """[summary]

        Raises:
            error: [description]
        """
        try:
            project = CreateProject(**kwargs)
            with session() as transaction_session:
                transaction_session.add(project)
                transaction_session.commit()
                transaction_session.refresh(project)
        except Exception as error:
            raise error

    def delete(self, project_arn: str):
        """[summary]

        Args:
            project_arn (str): [description]

        Raises:
            error: [description]
        """
        try:
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
            raise error

    def read():
        pass

    def update():
        pass
