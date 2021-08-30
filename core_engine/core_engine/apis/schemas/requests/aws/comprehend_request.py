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
    DocumentClassifierName: str
    DataAccessRoleArn: str
    InputDataConfig: InputDataConfig
    OutputDataConfig: OutputDataConfig
    LanguageCode: str
    Mode: str


class CreateEntityRecognizer(BaseModel):
    RecognizerName: str
    DataAccessRoleArn: str
    InputDataConfig: InputDataConfig
    LanguageCode: str


class DocumentClassifier(BaseModel):
    DocumentClassifierArn: str


class EntityRecognizer(BaseModel):
    EntityRecognizerArn: str


class DeployModel(BaseModel):
    model_arn: str
    min_inference_units: int
    endpoint_name: str


class UnDeployModel(BaseModel):
    endpoint_arn: str
