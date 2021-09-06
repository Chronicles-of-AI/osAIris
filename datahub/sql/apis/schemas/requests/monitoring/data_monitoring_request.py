from typing import List, Optional
from pydantic import BaseModel


class CreateClassificationDataRecord(BaseModel):
    model_uri: str
    data: str
    feedback: bool = False
    inferred_value: str
    ground_truth: Optional[str]


class ObjectDetectionCoords(BaseModel):
    x: float
    y: float
    width: float
    height: float
    rotation: float
    rectanglelabels: List[str]


class CreateObjectDetectionRecord(BaseModel):
    model_uri: str
    data: str
    feedback: bool = False
    inferred_value: List[ObjectDetectionCoords]
    ground_truth: Optional[List[ObjectDetectionCoords]]


class NERTags(BaseModel):
    end: int
    text: str
    start: int
    labels: List[str]


class CreateNERRecord(BaseModel):
    model_uri: str
    data: str
    feedback: bool = False
    inferred_value: List[NERTags]
    ground_truth: Optional[List[NERTags]]


class UpdateDataRecord(BaseModel):
    annotation_task_id: str
    ground_truth: str
