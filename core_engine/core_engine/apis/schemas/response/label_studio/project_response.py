from pydantic import BaseModel


class TransformAnnotationResponse(BaseModel):
    cloud_uri: str
