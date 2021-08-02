from typing import List
from pydantic import BaseModel


class AlgorithmSpecification(BaseModel):
    TrainingImage: str = None
    AlgorithmName: str = None
    TrainingInputMode: str


class S3DataSource(BaseModel):
    S3DataType: str
    S3Uri: str
    S3DataDistributionType: str


class DataSource(BaseModel):
    S3DataSource: S3DataSource


class InputDataConfig(BaseModel):
    ChannelName: str
    DataSource: DataSource
    ContentType: str


class OutputDataConfig(BaseModel):
    S3OutputPath: str


class ResourceConfig(BaseModel):
    InstanceType: str
    InstanceCount: int
    VolumeSizeInGB: int


class StoppingCondition(BaseModel):
    MaxRuntimeInSeconds: int


class CreateTrainingJob(BaseModel):
    TrainingJobName: str
    AlgorithmSpecification: AlgorithmSpecification
    RoleArn: str
    InputDataConfig: List[InputDataConfig]
    OutputDataConfig: OutputDataConfig
    ResourceConfig: ResourceConfig
    StoppingCondition: StoppingCondition


class TrainingJob(BaseModel):
    TrainingJobName: str
