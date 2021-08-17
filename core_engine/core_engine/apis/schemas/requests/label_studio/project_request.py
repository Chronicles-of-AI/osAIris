from pydantic import BaseModel


class TransformAnnotation(BaseModel):
    input_data_uri: str
    output_data_bucket_name: str
    output_data_file_prefix: str = None
    service_provider: str
