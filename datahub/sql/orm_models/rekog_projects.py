from sqlalchemy import Column, String, Integer
from sql import Base


class CreateProject(Base):
    __tablename__ = "rekog_projects"
    __table_args__ = {"extend_existing": True}
    row_id = Column(Integer, primary_key=True, autoincrement=True)
    uuid = Column(String)
    project_name = Column(String)
    project_arn = Column(String)
    status = Column(String)
    error = Column(String)
