from pydantic import BaseModel


class AddServiceData(BaseModel):
    service_name: str
    cloud_service_provider: str
    use_case: str
    data_type: str


class GetServiceData(BaseModel):
    cloud_service_provider: str
    use_case: str
