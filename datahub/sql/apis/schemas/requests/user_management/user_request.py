from pydantic import BaseModel, Field


class Register(BaseModel):
    user_name: str = Field(..., description="Unique username")
    password: str
    full_name: str
    email_id: str = Field(None, description="User email Id")
    user_role: str = Field(None, description="Role to be assigned to the user")


class Login(BaseModel):
    user_name: str = Field(..., description="Username")
    password: str = Field(..., description="Password")
