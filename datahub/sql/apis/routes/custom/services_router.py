from fastapi import APIRouter, Depends, HTTPException, status
from sql.apis.schemas.requests.custom.services_request import (
    AddServiceData,
    GetServiceData,
)
from sql.apis.schemas.responses.custom.services_response import (
    AddServiceDataResponse,
    ServiceDataResponse,
    AllServiceDataResponse,
)
from sql.controllers.custom.services_controller import ServicesController
from fastapi.security import OAuth2PasswordBearer
from commons.auth import decodeJWT
from sql import logger

logging = logger(__name__)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")
services_router = APIRouter()


@services_router.post(
    "/osairis/services/add",
    response_model=AddServiceDataResponse,
)
async def add_service_data(
    add_service_data_request: AddServiceData,
    token: str = Depends(oauth2_scheme),
):
    """[API router to create document classifier using AWS Comprehend]

    Args:
        create_data_record_request (CreateProjectFlow): [Create Data Record]
        token (str, optional): [Bearer token for authentication]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized exception when invalid token is passed]
        error: [Exception in underlying controller]

    Returns:
        [CreateDocumentClassifierResponse]: [Document Classifier response from AWS Comprehend]
    """
    try:
        logging.info("Calling /aws/comprehend/create_document_classifier endpoint")
        logging.debug(f"Request: {add_service_data_request}")
        if decodeJWT(token=token):
            response = ServicesController().create_service_controller(
                request=add_service_data_request
            )
            return AddServiceDataResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /osairis/data_monitoring/create endpoint: {error}")
        raise error


@services_router.get(
    "/osairis/services/list_all",
)
async def list_all_service_data(
    token: str = Depends(oauth2_scheme),
):
    """[API router to create document classifier using AWS Comprehend]

    Args:
        create_data_record_request (CreateProjectFlow): [Create Data Record]
        token (str, optional): [Bearer token for authentication]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized exception when invalid token is passed]
        error: [Exception in underlying controller]

    Returns:
        [CreateDocumentClassifierResponse]: [Document Classifier response from AWS Comprehend]
    """
    try:
        logging.info("Calling /aws/comprehend/create_document_classifier endpoint")
        if decodeJWT(token=token):
            response = ServicesController().get_all_services_controller()
            return response
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /osairis/data_monitoring/create endpoint: {error}")
        raise error


@services_router.get(
    "/osairis/services/by_cloud_and_use_case",
    response_model=ServiceDataResponse,
)
async def list_service_data(
    cloud_service_provider: str,
    use_case: str,
    token: str = Depends(oauth2_scheme),
):
    """[API router to create document classifier using AWS Comprehend]

    Args:
        create_data_record_request (CreateProjectFlow): [Create Data Record]
        token (str, optional): [Bearer token for authentication]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized exception when invalid token is passed]
        error: [Exception in underlying controller]

    Returns:
        [CreateDocumentClassifierResponse]: [Document Classifier response from AWS Comprehend]
    """
    try:
        logging.info("Calling /aws/comprehend/create_document_classifier endpoint")
        if decodeJWT(token=token):
            response = ServicesController().get_services_by_use_case_controller(
                cloud_service_provider=cloud_service_provider, use_case=use_case
            )
            return ServiceDataResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /osairis/data_monitoring/create endpoint: {error}")
        raise error