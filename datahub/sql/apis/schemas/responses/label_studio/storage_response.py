from typing import List
from pydantic import BaseModel


class CreateStorageResponse(BaseModel):
    id: int
    type: str
    presign: bool
    title: str
    description: str
    created_at: str
    last_sync: str = None
    bucket: str
    prefix: str = None
    use_blob_urls: bool
    region_name: str
    s3_endpoint: str = None
    project: int


class StorageResponse(BaseModel):
    id: int
    type: str
    presign: bool
    title: str
    description: str
    created_at: str
    last_sync: str = None
    bucket: str
    prefix: str = None
    use_blob_urls: bool
    region_name: str
    s3_endpoint: str = None
    project: int


class StorageDeleteResponse(BaseModel):
    status: str


class CreateGCSStorageResponse(BaseModel):
    id: int
    type: str
    presign: bool
    bucket: str
    prefix: str
    use_blob_urls: bool
    title: str
    description: str
    created_at: str
    last_sync: str
    project: int