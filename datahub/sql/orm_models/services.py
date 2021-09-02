from sqlalchemy import Column, String, Integer
from sqlalchemy.sql.sqltypes import DateTime
from sql import Base


class ProjectFlow(Base):
    __tablename__ = "project_flow"
    __table_args__ = {"extend_existing": True}
    row_id = Column(Integer, primary_key=True, autoincrement=True)
    use_case = Column(String)
    cloud_service_provider = Column(String)
    service_name = Column(String)
    created_by = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
