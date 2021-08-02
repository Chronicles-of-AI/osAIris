from sqlalchemy import Column, String, Integer, ForeignKey, Enum
from sql import Base


class CreateDataset(Base):
    __tablename__ = "datasets"
    __table_args__ = {"extend_existing": True}
    dataset_id = Column(String, primary_key=True)
    uri = Column(String)
    UUID = Column(String)
    alias_name = Column(String)
    problem_type = Column(String)
    status = Column(String)
    error = Column(String)