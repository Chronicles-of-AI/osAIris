from sqlalchemy import Column, String, DateTime, Integer, ForeignKey, Enum
from sqlalchemy.sql.sqltypes import Boolean
from sql import Base


class Config(Base):
    __tablename__ = "service_config"
    __table_args__ = {"extend_existing": True}
    row_id = Column(Integer, primary_key=True, autoincrement=True)
    alias_name = Column(String)
    problem_type = Column(
        String,
        Enum(
            "image-classification(single-label)",
            "image-classification(multi-label)",
            "text-classification(multi-label)",
            "text-classification(single-label)",
            name="problem_type",
        ),
    )
    service_name = Column(String)
