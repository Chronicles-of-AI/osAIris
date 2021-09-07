from sqlalchemy import Column, String, DateTime, Integer
from sqlalchemy.sql.sqltypes import JSON, Boolean
from sql import Base


class DataMonitoring(Base):
    __tablename__ = "data_monitoring"
    __table_args__ = {"extend_existing": True}
    row_id = Column(Integer, primary_key=True, autoincrement=True)
    model_uri = Column(String)
    data = Column(String)
    feedback = Column(Boolean)
    inferred_value = Column(JSON)
    ground_truth = Column(String)
    annotation_task_id = Column(String)
    created_by = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
