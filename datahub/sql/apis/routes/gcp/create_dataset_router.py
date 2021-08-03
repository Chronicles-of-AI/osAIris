from fastapi import APIRouter, Depends
from typing import List, Optional
from sql.apis.schemas.requests.gcp.create_dataset_request import (
    CreateTextClassificationDataset,
    CreateNERDataset,
    CreateImageClassificationDataset,
    CreateObjectDetectionDataset,
)
from sql.controllers.gcp.create_dataset_controller import CreateDatasetController
from fastapi.security import OAuth2PasswordBearer
from commons.auth import decodeJWT

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")

create_dataset_router = APIRouter()


@create_dataset_router.post("/gcp/automl/create_text_classification_dataset")
def create_text_classification_dataset(
    create_text_classification_dataset_request: CreateTextClassificationDataset,
    token: str = Depends(oauth2_scheme),
):
    return CreateDatasetController().create_text_classification_dataset_controller(
        create_text_classification_dataset_request
    )


@create_dataset_router.post("/gcp/automl/create_ner_dataset")
def create_ner_dataset(
    create_ner_request: CreateNERDataset,
    token: str = Depends(oauth2_scheme),
):
    return CreateDatasetController().create_ner_dataset_controller(create_ner_request)


@create_dataset_router.post("/gcp/automl/create_image_classification_dataset")
def create_image_classification_dataset(
    create_image_classification_dataset_request: CreateImageClassificationDataset,
    token: str = Depends(oauth2_scheme),
):
    return CreateDatasetController().create_image_classification_dataset_controller(
        create_image_classification_dataset_request
    )


@create_dataset_router.post("/gcp/automl/create_object_detection_dataset")
def create_object_detection_dataset(
    create_object_detection_dataset_request: CreateObjectDetectionDataset,
    token: str = Depends(oauth2_scheme),
):
    return CreateDatasetController().create_object_detection_dataset_controller(
        create_object_detection_dataset_request
    )
