from typing import List
from pydantic import BaseModel


class OutputConfig(BaseModel):
    S3Bucket: str
    S3KeyPrefix: str


class ManifestConfig(BaseModel):
    Bucket: str
    Name: str


class GroundTruthManifest(BaseModel):
    S3Object: ManifestConfig


class AssetConfig(BaseModel):
    GroundTruthManifest: GroundTruthManifest


class TrainingData(BaseModel):
    Assets: List[AssetConfig]


class TestingData(BaseModel):
    Assets: List[AssetConfig] = None
    AutoCreate: bool = True


class StartTraining(BaseModel):
    pipeline_id: int
    project_arn: str
    version_name: str
    output_config: OutputConfig
    training_data: TrainingData
    testing_data: TestingData


class DeployModel(BaseModel):
    pipeline_id: int
    project_version_arn: str
    min_inference_units: int


class UndeployModel(BaseModel):
    pipeline_id: int
    project_version_arn: str


class DeleteModel(BaseModel):
    project_version_arn: str
