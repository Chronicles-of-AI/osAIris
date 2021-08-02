from sqlalchemy import Column, String, DateTime, Integer, ForeignKey, Enum
from sqlalchemy.sql.sqltypes import Boolean
from sql import Base


class Input(Base):
    __tablename__ = "input_data"
    __table_args__ = {"extend_existing": True}
    row_id = Column(Integer, primary_key=True, autoincrement=True)
    uri = Column(String)
    feedback = Column(Boolean)
    inferred_value = Column(String)
    UUID = Column(String)
    alias_name = Column(String)
    status = Column(
        String,
        Enum("Running", "Completed", "Failed", name="status_enum", create_type=False),
    )
    error = Column(String)
