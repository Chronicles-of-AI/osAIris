from fastapi import APIRouter, Depends, HTTPException, status
from sql.apis.schemas.requests.gcp.train_model_request import (
    TrainTextModel,
    TrainImageModel,
    TrainImageEdgeModel,
)
from sql.apis.schemas.responses.gcp.train_model_response import TrainModelResponse
from sql.controllers.gcp.train_model_controller import TrainModelController
from fastapi.security import OAuth2PasswordBearer
from commons.auth import decodeJWT
from sql import logger

logging = logger(__name__)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")

train_model_router = APIRouter()


@train_model_router.post(
    "/gcp/automl/train_text_classification_model", response_model=TrainModelResponse
)
async def create_text_classification_dataset(
    train_text_classification_model_request: TrainTextModel,
    token: str = Depends(oauth2_scheme),
):
    """[API router to train AutoML text classification model]

    Args:
        train_text_classification_model_request (TrainTextModel): [AutoML text classification model training request]
        token (str, optional): [Bearer token for authentication]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized exception when invalid token is passed]
        error: [Exception in underlying controller]

    Returns:
        [TrainModelResponse]: [AutoML text classification model training response]
    """
    try:
        logging.info("Calling /gcp/automl/train_text_classification_model endpoint")
        logging.debug(f"Request: {train_text_classification_model_request}")
        if decodeJWT(token=token):
            response = (
                TrainModelController().train_text_classification_model_controller(
                    request=train_text_classification_model_request
                )
            )
            return TrainModelResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(
            f"Error in /gcp/automl/train_text_classification_model endpoint: {error}"
        )
        raise error


@train_model_router.post(
    "/gcp/automl/train_ner_model", response_model=TrainModelResponse
)
async def create_ner_dataset(
    train_ner_model_request: TrainTextModel,
    token: str = Depends(oauth2_scheme),
):
    """[API router to start training AutoML NER model]

    Args:
        train_ner_model_request (TrainTextModel): [Train AutoML NER model request]
        token (str, optional): [Bearer token for authentication]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized exception when invalid token is passed]
        error: [Exception in underlying controller]

    Returns:
        [TrainModelResponse]: [AutoML Train NER model response]
    """
    try:
        logging.info("Calling /gcp/automl/train_ner_model endpoint")
        logging.debug(f"Request: {train_ner_model_request}")
        if decodeJWT(token=token):
            response = TrainModelController().train_ner_model_controller(
                request=train_ner_model_request
            )
            return TrainModelResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /gcp/automl/train_ner_model endpoint: {error}")
        raise error


@train_model_router.post(
    "/gcp/automl/train_image_classification_model", response_model=TrainModelResponse
)
async def create_image_classification_training(
    train_image_classification_model_request: TrainImageModel,
    token: str = Depends(oauth2_scheme),
):
    """[API router to train AutoML image classification model]

    Args:
        train_image_classification_model_request (TrainImageModel): [AutoML image classification train request]
        token (str, optional): [Bearer token for authentication]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized exception when invalid token is passed]
        error: [Exception in underlying controller]

    Returns:
        [TrainModelResponse]: [AutoML train image classification model response]
    """
    try:
        logging.info("Calling /gcp/automl/train_image_classification_model endpoint")
        logging.debug(f"Request: {train_image_classification_model_request}")
        if decodeJWT(token=token):
            response = (
                TrainModelController().train_image_classification_model_controller(
                    request=train_image_classification_model_request
                )
            )
            return TrainModelResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(
            f"Error in /gcp/automl/train_image_classification_model endpoint: {error}"
        )
        raise error


@train_model_router.post(
    "/gcp/automl/train_image_classification_edge_model",
    response_model=TrainModelResponse,
)
async def create_image_classification_edge_training(
    train_image_classification_edge_model_request: TrainImageEdgeModel,
    token: str = Depends(oauth2_scheme),
):
    """[API router to train image classification model for edge device]

    Args:
        train_image_classification_edge_model_request (TrainImageEdgeModel): [Image classification model for edge request]
        token (str, optional): [Bearer token for authentication]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized exception when invalid token is passed]
        error: [Exception in underlying controller]

    Returns:
        [TrainModelResponse]: [AutoML train image classification model response for edge device]
    """
    try:
        logging.info(
            "Calling /gcp/automl/train_image_classification_edge_model endpoint"
        )
        logging.debug(f"Request: {train_image_classification_edge_model_request}")
        if decodeJWT(token=token):
            response = (
                TrainModelController().train_image_classification_edge_model_controller(
                    request=train_image_classification_edge_model_request
                )
            )
            return TrainModelResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(
            f"Error in /gcp/automl/train_image_classification_edge_model endpoint: {error}"
        )
        raise error


@train_model_router.post(
    "/gcp/automl/train_object_detection_model", response_model=TrainModelResponse
)
async def create_object_detection_training(
    train_object_detection_model_request: TrainImageModel,
    token: str = Depends(oauth2_scheme),
):
    """[API router to train AutoML object detection model]

    Args:
        train_object_detection_model_request (TrainImageModel): [Train AutoML Object detection model request]
        token (str, optional): [Bearer token for authentication]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized exception when invalid token is passed]
        error: [Exception in underlying controller]

    Returns:
        [TrainModelResponse]: [AutoML train object detection model response]
    """
    try:
        logging.info("Calling /gcp/automl/train_object_detection_model endpoint")
        logging.debug(f"Request: {train_object_detection_model_request}")
        if decodeJWT(token=token):
            response = TrainModelController().train_object_detection_model_controller(
                request=train_object_detection_model_request
            )
            return TrainModelResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(
            f"Error in /gcp/automl/train_object_detection_model endpoint: {error}"
        )
        raise error


@train_model_router.post(
    "/gcp/automl/train_object_detection_edge_model", response_model=TrainModelResponse
)
async def create_object_detection_edge_training(
    train_object_detection_edge_model_request: TrainImageEdgeModel,
    token: str = Depends(oauth2_scheme),
):
    """[API router to train AutoML object detection model for edge device]

    Args:
        train_object_detection_model_request (TrainImageModel): [Train AutoML Object detection model request for edge device]
        token (str, optional): [Bearer token for authentication]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized exception when invalid token is passed]
        error: [Exception in underlying controller]

    Returns:
        [TrainModelResponse]: [AutoML train object detection model for edge device response]
    """
    try:
        logging.info("Calling /gcp/automl/train_object_detection_edge_model endpoint")
        logging.debug(f"Request: {train_object_detection_edge_model_request}")
        if decodeJWT(token=token):
            response = (
                TrainModelController().train_object_detection_edge_model_controller(
                    request=train_object_detection_edge_model_request
                )
            )
            return TrainModelResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(
            f"Error in /gcp/automl/train_object_detection_edge_model endpoint: {error}"
        )
        raise error
