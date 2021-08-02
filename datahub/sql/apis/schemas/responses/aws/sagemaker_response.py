from typing import List
from pydantic import BaseModel
import datetime


class TrainingJobSummaries(BaseModel):
    TrainingJobName: str
    TrainingJobArn: str
    CreationTime: datetime.datetime
    TrainingEndTime: datetime.datetime
    LastModifiedTime: datetime.datetime
    TrainingJobStatus: str


class ListTrainingJobResponse(BaseModel):
    TrainingJobSummaries: List[TrainingJobSummaries]
    NextToken: str


class TrainingJobResponse(BaseModel):
    training_job_arn: str
    status: str


class TrainingStatus(BaseModel):
    status: str
