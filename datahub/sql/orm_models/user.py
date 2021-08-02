from sqlalchemy import Column, String
from sql import Base


class User(Base):
    __tablename__ = "user"
    __table_args__ = {"extend_existing": True}
    user_name = Column(String, primary_key=True)
    password = Column(String)
    full_name = Column(String)
    email_id = Column(String)
    user_role = Column(String)
