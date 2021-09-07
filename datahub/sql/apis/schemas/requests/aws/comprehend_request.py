from typing import List
from pydantic import BaseModel


class AugmentedManifests(BaseModel):
    S3Uri: str
    AttributeNames: List[str]


class InputDataConfig(BaseModel):
    DataFormat: str
    AugmentedManifests: List[AugmentedManifests]


class OutputDataConfig(BaseModel):
    S3Uri: str


class CreateDocumentClassifier(BaseModel):
    pipeline_id: int
    DocumentClassifierName: str
    DataAccessRoleArn: str
    InputDataConfig: InputDataConfig
    OutputDataConfig: OutputDataConfig
    LanguageCode: str
    Mode: str


class CreateEntityRecognizer(BaseModel):
    pipeline_id: int
    RecognizerName: str
    DataAccessRoleArn: str
    InputDataConfig: InputDataConfig
    LanguageCode: str


class EntityRecognizer(BaseModel):
    pipeline_id: int
    EntityRecognizerArn: str


class DocumentClassifier(BaseModel):
    pipeline_id: int
    DocumentClassifierArn: str


class DeployModel(BaseModel):
    pipeline_id: int
    model_arn: str
    min_inference_units: int
    endpoint_name: str


class UnDeployModel(BaseModel):
    pipeline_id: int
    endpoint_arn: str
