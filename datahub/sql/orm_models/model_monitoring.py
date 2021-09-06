from sqlalchemy import Column, String, DateTime, Integer, ForeignKey
from sqlalchemy.sql.sqltypes import Boolean
from sql import Base


class ModelMonitoring(Base):
    __tablename__ = "model_monitoring"
    __table_args__ = {"extend_existing": True}
    row_id = Column(Integer, primary_key=True, autoincrement=True)
    model_uri = Column(String, ForeignKey("models.model_id"))
    model_f1_score = Column(String)
    model_recall = Column(String)
    model_precision = Column(String)
    model_drift_threshold = Column(String)
    production_f1_score = Column(String)
    production_recall = Column(String)
    production_precision = Column(String)
    model_drift = Column(Boolean)
    timestamp = Column(DateTime)
    created_by = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
