from sqlalchemy import Column, String, DateTime, Integer, ForeignKey, Enum
from sqlalchemy.sql.sqltypes import Boolean
from sqlalchemy_utils import JSONType
from sql import Base


class Models(Base):
    # TODO: create unique contraint with model_id and alias_name
    __tablename__ = "models"
    __table_args__ = {"extend_existing": True}
    model_id = Column(String, primary_key=True)
    artifacts = Column(JSONType)
    dataset_id = Column(JSONType)
    alias_name = Column(String)
    auto_trigger = Column(Boolean)
    next_stage = Column(String)
    UUID = Column(String)
    status = Column(String)
    error = Column(String)
    created = Column(DateTime)
    updated = Column(DateTime)
