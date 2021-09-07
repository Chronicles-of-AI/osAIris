from typing import List
from pydantic import BaseModel
from datetime import datetime


class AddServiceDataResponse(BaseModel):
    service_name: str
    cloud_service_provider: str
    use_case: str
    data_type: str
    created_at: datetime


class ServiceDataResponse(BaseModel):
    use_case: str
    cloud_service_provider: str
    service_name: str
    data_type: str
    created_by: str = None
    created_at: datetime
    updated_at: datetime = None


class AllServiceDataResponse(BaseModel):
    all_service_data: List[ServiceDataResponse]
