from sqlalchemy import Column, String, DateTime, Integer, ForeignKey, Enum
from sql import Base


class Operations(Base):
    __tablename__ = "operations"
    __table_args__ = {"extend_existing": True}
    row_id = Column(Integer, primary_key=True, autoincrement=True)
    project_id = Column(String)
    region = Column(String)
    operation_id = Column(String)
    functional_stage = Column(String)
    service_id = Column(String)
    status = Column(String)
    created = Column(DateTime)
    updated = Column(DateTime)
    error = Column(String)
