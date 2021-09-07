from typing import List
from pydantic import BaseModel


class AugmentedManifests(BaseModel):
    S3Uri: str
    AttributeNames: List[str]
