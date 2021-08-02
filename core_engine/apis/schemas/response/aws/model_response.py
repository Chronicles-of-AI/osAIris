from typing import List
from pydantic import BaseModel


class StartTrainingResponse(BaseModel):
    project_version_arn: str


class ModelStatus(BaseModel):
    status: str


class ManifestConfig(BaseModel):
    Bucket: str
    Name: str
    Version: str


class ManifestSummary(BaseModel):
    S3Object: ManifestConfig


class EvaluationResponse(BaseModel):
    F1Score: str
    Summary: ManifestSummary
