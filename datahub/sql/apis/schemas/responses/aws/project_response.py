from typing import List
from pydantic import BaseModel
import datetime


class CreateProjectResponse(BaseModel):
    project_arn: str = None
    uuid: str = None
    status: str = None


class DeleteProjectResponse(BaseModel):
    project_arn: str = None
    status: str = None


class OutputConfig(BaseModel):
    S3Bucket: str = None
    S3KeyPrefix: str = None


class S3Object(BaseModel):
    Bucket: str = None
    Name: str = None
    Version: str = None


class GroundTruthManifest(BaseModel):
    S3Object: S3Object


class AssetConfig(BaseModel):
    GroundTruthManifest: GroundTruthManifest


class Input(BaseModel):
    Assets: List[AssetConfig]


class TrainingDataResult(BaseModel):
    Input: Input
    Output: Input
    Validation: Input


class TestingInput(BaseModel):
    Assets: List[AssetConfig]
    AutoCreate: bool = None


class TestingDataResult(BaseModel):
    Input: TestingInput
    Output: TestingInput
    Validation: Input


class ManifestConfig(BaseModel):
    Bucket: str = None
    Name: str = None
    Version: str = None


class ManifestSummary(BaseModel):
    S3Object: ManifestConfig


class EvaluationResponse(BaseModel):
    F1Score: str = None
    Summary: ManifestSummary


class ProjectDescriptions(BaseModel):
    ProjectVersionArn: str = None
    CreationTimestamp: datetime.datetime = None
    MinInferenceUnits: int = None
    Status: str = None
    StatusMessage: str = None
    BillableTrainingTimeInSeconds: int = None
    TrainingEndTimestamp: datetime.datetime = None
    OutputConfig: OutputConfig
    TrainingDataResult: TrainingDataResult
    TestingDataResult: TestingDataResult
    EvaluationResult: EvaluationResponse
    ManifestSummary: ManifestSummary


class ProjectVersionResponse(BaseModel):
    ProjectVersionDescriptions: List[ProjectDescriptions]


class ProjectDescription(BaseModel):
    ProjectArn: str = None
    CreationTimestamp: datetime.datetime = None
    Status: str = None


class ProjectDescriptionsResponse(BaseModel):
    ProjectDescriptions: List[ProjectDescription]
    NextToken: str = None
