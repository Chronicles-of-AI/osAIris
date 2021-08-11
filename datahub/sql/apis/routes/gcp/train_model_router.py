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

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")

train_model_router = APIRouter()


@train_model_router.post(
    "/gcp/automl/train_text_classification_model", response_model=TrainModelResponse
)
def create_text_classification_dataset(
    train_text_classification_model_request: TrainTextModel,
    token: str = Depends(oauth2_scheme),
):
    """[summary]

    Args:
        train_text_classification_model_request (TrainTextModel): [description]
        token (str, optional): [description]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [description]
        error: [description]

    Returns:
        [type]: [description]
    """
    try:
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
        raise error


@train_model_router.post(
    "/gcp/automl/train_ner_model", response_model=TrainModelResponse
)
def create_ner_dataset(
    train_ner_model_request: TrainTextModel,
    token: str = Depends(oauth2_scheme),
):
    """[summary]

    Args:
        train_ner_model_request (TrainTextModel): [description]
        token (str, optional): [description]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [description]
        error: [description]

    Returns:
        [type]: [description]
    """
    try:
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
        raise error


@train_model_router.post(
    "/gcp/automl/train_image_classification_model", response_model=TrainModelResponse
)
def create_image_classification_training(
    train_image_classification_model_request: TrainImageModel,
    token: str = Depends(oauth2_scheme),
):
    """[summary]

    Args:
        train_image_classification_model_request (TrainImageModel): [description]
        token (str, optional): [description]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [description]
        error: [description]

    Returns:
        [type]: [description]
    """
    try:
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
        raise error


@train_model_router.post(
    "/gcp/automl/train_image_classification_edge_model",
    response_model=TrainModelResponse,
)
def create_image_classification_edge_training(
    train_image_classification_edge_model_request: TrainImageEdgeModel,
    token: str = Depends(oauth2_scheme),
):
    """[summary]

    Args:
        train_image_classification_edge_model_request (TrainImageEdgeModel): [description]
        token (str, optional): [description]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [description]
        error: [description]

    Returns:
        [type]: [description]
    """
    try:
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
        raise error


@train_model_router.post(
    "/gcp/automl/train_object_detection_model", response_model=TrainModelResponse
)
def create_object_detection_training(
    train_object_detection_model_request: TrainImageModel,
    token: str = Depends(oauth2_scheme),
):
    """[summary]

    Args:
        train_object_detection_model_request (TrainImageModel): [description]
        token (str, optional): [description]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [description]
        error: [description]

    Returns:
        [type]: [description]
    """
    try:
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
        raise error


@train_model_router.post(
    "/gcp/automl/train_object_detection_edge_model", response_model=TrainModelResponse
)
def create_object_detection_edge_training(
    train_object_detection_edge_model_request: TrainImageEdgeModel,
    token: str = Depends(oauth2_scheme),
):
    """[summary]

    Args:
        train_object_detection_edge_model_request (TrainImageEdgeModel): [description]
        token (str, optional): [description]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [description]
        error: [description]

    Returns:
        [type]: [description]
    """
    try:
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
        raise error
