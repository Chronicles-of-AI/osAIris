from typing import List
from pydantic import BaseModel
import datetime


class CreateDocumentClassifierResponse(BaseModel):
    document_classifier_arn: str
    status: str


class CreateEntityRecognizerResponse(BaseModel):
    entity_recognizer_arn: str
    status: str


class DocumentClassifierResponse(BaseModel):
    status: str


class DocumentClassifierStatusResponse(BaseModel):
    model_status: str


class EntiyRecognizerResponse(BaseModel):
    status: str


class EntiyRecognizerStatusResponse(BaseModel):
    model_status: str


class AugmentedManifests(BaseModel):
    S3Uri: str
    AttributeNames: List[str]


class InputDataConfig(BaseModel):
    DataFormat: str
    S3Uri: str
    LabelDelimiter: str
    AugmentedManifests: List[AugmentedManifests]


class OutputDataConfig(BaseModel):
    S3Uri: str
    KmsKeyId: str


class EvaluationMetrics(BaseModel):
    Accuracy: int
    Precision: int
    Recall: int
    F1Score: int
    MicroPrecision: int
    MicroRecall: int
    MicroF1Score: int
    HammingLoss: int


class ClassifierMetadata(BaseModel):
    NumberOfLabels: str
    NumberOfTrainedDocuments: str
    NumberOfTestDocuments: str
    EvaluationMetrics: EvaluationMetrics


class DocumentClassifier(BaseModel):
    DocumentClassifierArn: str
    LanguageCode: str
    Status: str
    SubmitTime: datetime.datetime
    EndTime: datetime.datetime
    TrainingStartTime: datetime.datetime
    TrainingEndTime: datetime.datetime
    InputDataConfig: InputDataConfig
    OutputDataConfig: OutputDataConfig
    ClassifierMetadata: ClassifierMetadata
    Mode: str


class DescribeClassifierResponse(BaseModel):
    DocumentClassifierProperties: DocumentClassifier


class ListClassifierResponse(BaseModel):
    DocumentClassifierProperties: List[DocumentClassifier]


class DeployModelResponse(BaseModel):
    endpoint_arn: str
    status: str


class UnDeployModelResponse(BaseModel):
    status: str
