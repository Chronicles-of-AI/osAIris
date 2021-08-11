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

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")

create_dataset_router = APIRouter()


@create_dataset_router.post(
    "/gcp/automl/create_text_classification_dataset",
    response_model=CreateDatasetResponse,
)
def create_text_classification_dataset(
    create_text_classification_dataset_request: CreateTextClassificationDataset,
    token: str = Depends(oauth2_scheme),
):
    """[summary]

    Args:
        create_text_classification_dataset_request (CreateTextClassificationDataset): [description]
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
        raise error


@create_dataset_router.post(
    "/gcp/automl/create_ner_dataset",
    response_model=CreateDatasetResponse,
)
def create_ner_dataset(
    create_ner_request: CreateNERDataset,
    token: str = Depends(oauth2_scheme),
):
    """[summary]

    Args:
        create_ner_request (CreateNERDataset): [description]
        token (str, optional): [description]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [description]
        error: [description]

    Returns:
        [type]: [description]
    """
    try:
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
        raise error


@create_dataset_router.post(
    "/gcp/automl/create_image_classification_dataset",
    response_model=CreateDatasetResponse,
)
def create_image_classification_dataset(
    create_image_classification_dataset_request: CreateImageClassificationDataset,
    token: str = Depends(oauth2_scheme),
):
    """[summary]

    Args:
        create_image_classification_dataset_request (CreateImageClassificationDataset): [description]
        token (str, optional): [description]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [description]
        error: [description]

    Returns:
        [type]: [description]
    """
    try:
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
        raise error


@create_dataset_router.post(
    "/gcp/automl/create_object_detection_dataset",
    response_model=CreateDatasetResponse,
)
def create_object_detection_dataset(
    create_object_detection_dataset_request: CreateObjectDetectionDataset,
    token: str = Depends(oauth2_scheme),
):
    """[summary]

    Args:
        create_object_detection_dataset_request (CreateObjectDetectionDataset): [description]
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
        raise error
