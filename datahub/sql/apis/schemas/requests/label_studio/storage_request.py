from typing import List
from pydantic import BaseModel


class CreateStorage(BaseModel):
    project: int
    title: str
    description: str
    bucket: str
    region_name: str = "us-east-2"
    prefix: str = None
    presign: bool = True
    use_blob_urls: bool = True


class Storage(BaseModel):
    storage_id: int


class CreateGCSStorage(BaseModel):
    project: int
    title: str
    description: str
    bucket: str
    prefix: str = None
    presign: bool = True
    use_blob_urls: bool = True
