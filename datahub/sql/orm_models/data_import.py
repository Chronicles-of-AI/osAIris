from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.sql.sqltypes import Boolean
from sql import Base


class DataImport(Base):
    __tablename__ = "data_import"
    __table_args__ = {"extend_existing": True}
    row_id = Column(Integer, primary_key=True, autoincrement=True)
    uri = Column(String)
    dataset_id = Column(String, ForeignKey("datasets.dataset_id"))
    auto_trigger = Column(Boolean)
    next_stage = Column(String)
    UUID = Column(String)
    status = Column(String)
    error = Column(String)
