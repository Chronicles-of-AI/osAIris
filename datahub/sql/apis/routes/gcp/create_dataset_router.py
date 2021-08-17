import logging
from fastapi import APIRouter, Depends, HTTPException, status
from sql.apis.schemas.requests.gcp.create_dataset_request import (
    CreateTextClassificationDataset,
    CreateNERDataset,
    CreateImageClassificationDataset,
    CreateObjectDetectionDataset,
)
from sql.apis.schemas.responses.gcp.create_dataset_response import CreateDatasetResponse
from sql.controllers.gcp.create_dataset_controller import CreateDatasetController
from fastapi.security import OAuth2PasswordBearer
from commons.auth import decodeJWT
from sql import logger

logging = logger(__name__)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")
create_dataset_router = APIRouter()


@create_dataset_router.post(
    "/gcp/automl/create_text_classification_dataset",
    response_model=CreateDatasetResponse,
)
async def create_text_classification_dataset(
    create_text_classification_dataset_request: CreateTextClassificationDataset,
    token: str = Depends(oauth2_scheme),
):
    """[API router to AutoML text classification dataset]

    Args:
        create_text_classification_dataset_request (CreateTextClassificationDataset): [AutoML text classification create dataset request]
        token (str, optional): [Bearer token for authentication]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized exception when invalid token is passed]
        error: [Exception in underlying controller]

    Returns:
        [CreateDatasetResponse]: [AutoML Create Dataset response]
    """
    try:
        logging.info("Calling /gcp/automl/create_text_classification_dataset endpoint")
        logging.debug(f"Request: {create_text_classification_dataset_request}")
        if decodeJWT(token=token):
            response = (
                CreateDatasetController().create_text_classification_dataset_controller(
                    create_text_classification_dataset_request
                )
            )
            return CreateDatasetResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(
            f"Error in /gcp/automl/create_text_classification_dataset endpoint: {error}"
        )
        raise error


@create_dataset_router.post(
    "/gcp/automl/create_ner_dataset",
    response_model=CreateDatasetResponse,
)
async def create_ner_dataset(
    create_ner_request: CreateNERDataset,
    token: str = Depends(oauth2_scheme),
):
    """[API router to create AutoML NER dataset]

    Args:
        create_ner_request (CreateNERDataset): [AutoML NER create dataset request]
        token (str, optional): [Bearer token for authentication]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized exception when invalid token is passed]
        error: [Exception in underlying controller]

    Returns:
        [CreateDatasetResponse]: [AutoML NER Create Dataset response]
    """
    try:
        logging.info("Calling /gcp/automl/create_ner_dataset endpoint")
        logging.debug(f"Request: {create_ner_request}")
        if decodeJWT(token=token):
            response = CreateDatasetController().create_ner_dataset_controller(
                create_ner_request
            )
            return CreateDatasetResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /gcp/automl/create_ner_dataset endpoint: {error}")
        raise error


@create_dataset_router.post(
    "/gcp/automl/create_image_classification_dataset",
    response_model=CreateDatasetResponse,
)
async def create_image_classification_dataset(
    create_image_classification_dataset_request: CreateImageClassificationDataset,
    token: str = Depends(oauth2_scheme),
):
    """[API router to create AutoML image classification dataset]

    Args:
        create_image_classification_dataset_request (CreateImageClassificationDataset): [AutoML create image classification dataset request]
        token (str, optional): [Bearer token for authentication]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized exception when invalid token is passed]
        error: [Exception in underlying controller]

    Returns:
        [CreateDatasetResponse]: [AutoML image classification create Dataset response]
    """
    try:
        logging.info("Calling /gcp/automl/create_image_classification_dataset endpoint")
        logging.debug(f"Request: {create_image_classification_dataset_request}")
        if decodeJWT(token=token):
            response = CreateDatasetController().create_image_classification_dataset_controller(
                create_image_classification_dataset_request
            )
            return CreateDatasetResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(
            f"Error in /gcp/automl/create_image_classification_dataset endpoint: {error}"
        )
        raise error


@create_dataset_router.post(
    "/gcp/automl/create_object_detection_dataset",
    response_model=CreateDatasetResponse,
)
async def create_object_detection_dataset(
    create_object_detection_dataset_request: CreateObjectDetectionDataset,
    token: str = Depends(oauth2_scheme),
):
    """[API router to create AutoML Object Detection Dataset]

    Args:
        create_object_detection_dataset_request (CreateObjectDetectionDataset): [AutoML Object Detection dataset creation request]
        token (str, optional): [Bearer token for authentication]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized exception when invalid token is passed]
        error: [Exception in underlying controller]

    Returns:
        [CreateDatasetResponse]: [AutoML Object detection create dataset response]
    """
    try:
        logging.info("Calling /gcp/automl/create_object_detection_dataset endpoint")
        logging.debug(f"Request: {create_object_detection_dataset_request}")
        if decodeJWT(token=token):
            response = (
                CreateDatasetController().create_object_detection_dataset_controller(
                    create_object_detection_dataset_request
                )
            )
            return CreateDatasetResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(
            f"Error in /gcp/automl/create_object_detection_dataset endpoint: {error}"
        )
        raise error
