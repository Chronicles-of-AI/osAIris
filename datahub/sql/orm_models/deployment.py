from sqlalchemy import Column, String, DateTime, Integer, ForeignKey
from sql import Base


class Deployment(Base):
    __tablename__ = "deployment"
    __table_args__ = {"extend_existing": True}
    row_id = Column(Integer, primary_key=True, autoincrement=True)
    UUID = Column(String)
    model_id = Column(String, ForeignKey("models.model_id"))
    deployment_endpoint = Column(String)
    pipeline_id = Column(Integer)
    created = Column(DateTime)
    updated = Column(DateTime)
    status = Column(String)
    error = Column(String)
