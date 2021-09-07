from fastapi import APIRouter, Depends, HTTPException, status
from sql.apis.schemas.requests.aws.comprehend_request import (
    CreateDocumentClassifier,
    CreateEntityRecognizer,
    DocumentClassifier,
    EntityRecognizer,
    DeployModel,
    UnDeployModel,
)
from sql.apis.schemas.responses.aws.comprehend_response import (
    CreateDocumentClassifierResponse,
    CreateEntityRecognizerResponse,
    DocumentClassifierResponse,
    EntiyRecognizerResponse,
    DeployModelResponse,
    UnDeployModelResponse,
)
from sql.controllers.aws.comprehend_controller import ComprehendController
from fastapi.security import OAuth2PasswordBearer
from commons.auth import decodeJWT
from sql import logger

logging = logger(__name__)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")
comprehend_router = APIRouter()


@comprehend_router.post(
    "/aws/comprehend/create_document_classifier",
    response_model=CreateDocumentClassifierResponse,
)
async def create_document_classifier(
    create_document_classifier_request: CreateDocumentClassifier,
    token: str = Depends(oauth2_scheme),
):
    """[API router to create document classifier using AWS Comprehend]

    Args:
        create_document_classifier_request (CreateDocumentClassifier): [Create Document Classifier request expected by AWS Comprehend]
        token (str, optional): [Bearer token for authentication]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized exception when invalid token is passed]
        error: [Exception in underlying controller]

    Returns:
        [CreateDocumentClassifierResponse]: [Document Classifier response from AWS Comprehend]
    """
    try:
        logging.info("Calling /aws/comprehend/create_document_classifier endpoint")
        logging.debug(f"Request: {create_document_classifier_request}")
        if decodeJWT(token=token):
            response = ComprehendController().create_document_classifier_controller(
                create_document_classifier_request
            )
            return CreateDocumentClassifierResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(
            f"Error in /aws/comprehend/create_document_classifier endpoint: {error}"
        )
        raise error


@comprehend_router.post(
    "/aws/comprehend/create_entity_recognizer",
    response_model=CreateEntityRecognizerResponse,
)
async def create_entity_recognizer(
    create_entity_recognizer_request: CreateEntityRecognizer,
    token: str = Depends(oauth2_scheme),
):
    """[API router to create entity recognizer using AWS Comprehend]

    Args:
        create_entity_recognizer_request (CreateEntityRecognizer): [Create Document Classifier request expected by AWS Comprehend]
        token (str, optional): [Bearer token for authentication]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized exception when invalid token is passed]
        error: [Exception in underlying controller]

    Returns:
        [CreateEntityRecognizerResponse]: [Document Classifier response from AWS Comprehend]
    """
    try:
        logging.info("Calling /aws/comprehend/create_entity_recognizer endpoint")
        logging.debug(f"Request: {create_entity_recognizer_request}")
        if decodeJWT(token=token):
            response = ComprehendController().create_document_classifier_controller(
                create_entity_recognizer_request
            )
            return CreateEntityRecognizerResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(
            f"Error in /aws/comprehend/create_document_classifier endpoint: {error}"
        )
        raise error


@comprehend_router.post(
    "/aws/comprehend/stop_training_document_classifier",
    response_model=DocumentClassifierResponse,
)
async def stop_training_document_classifier(
    stop_training_document_classifier_request: DocumentClassifier,
    token: str = Depends(oauth2_scheme),
):
    """[API router to stop training process of document classifier using AWS Comprehend]

    Args:
        stop_training_document_classifier_request (DocumentClassifier): [Stop Document classifier training request]
        token (str, optional): [Bearer token for authentication]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized exception when invalid token is passed]
        error: [Exception in underlying controller]

    Returns:
        [DocumentClassifierResponse]: [Response from AWS Comprehend]
    """
    try:
        logging.info(
            "Calling /aws/comprehend/stop_training_document_classifier endpoint"
        )
        logging.debug(f"Request: {stop_training_document_classifier_request}")
        if decodeJWT(token=token):
            response = (
                ComprehendController().stop_training_document_classifier_controller(
                    stop_training_document_classifier_request
                )
            )
            return DocumentClassifierResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(
            f"Error in /aws/comprehend/stop_training_document_classifier endpoint: {error}"
        )
        raise error


@comprehend_router.post(
    "/aws/comprehend/stop_training_entity_recognizer",
    response_model=EntiyRecognizerResponse,
)
async def stop_training_entity_recognizer(
    stop_training_entity_recognizer_request: EntityRecognizer,
    token: str = Depends(oauth2_scheme),
):
    """[API router to stop training process of Entity Recognizer using AWS Comprehend]

    Args:
        stop_training_document_classifier_request (EntityRecognizer): [Stop Entity Recognizer training request]
        token (str, optional): [Bearer token for authentication]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized exception when invalid token is passed]
        error: [Exception in underlying controller]

    Returns:
        [EntiyRecognizerResponse]: [Response from AWS Comprehend]
    """
    try:
        logging.info("Calling /aws/comprehend/stop_training_entity_recognizer endpoint")
        logging.debug(f"Request: {stop_training_entity_recognizer_request}")
        if decodeJWT(token=token):
            response = (
                ComprehendController().stop_training_document_classifier_controller(
                    stop_training_entity_recognizer_request
                )
            )
            return EntiyRecognizerResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(
            f"Error in /aws/comprehend/stop_training_entity_recognizer_request endpoint: {error}"
        )
        raise error


@comprehend_router.post(
    "/aws/comprehend/delete_document_classifier",
    response_model=DocumentClassifierResponse,
)
async def delete_document_classifier(
    delete_document_classifier_requeset: DocumentClassifier,
    token: str = Depends(oauth2_scheme),
):
    """[API router to delete document classifier using AWS Comprehend]

    Args:
        delete_document_classifier_requeset (DocumentClassifier): [Delete Document classifier request]
        token (str, optional): [Bearer token for authentication]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized exception when invalid token is passed]
        error: [Exception in underlying controller]

    Returns:
        [DocumentClassifierResponse]: [Response from AWS Comprehend]
    """
    try:
        logging.info("Calling /aws/comprehend/delete_document_classifier endpoint")
        logging.debug(f"Request: {delete_document_classifier_requeset}")
        if decodeJWT(token=token):
            response = ComprehendController().delete_document_classifier_controller(
                delete_document_classifier_requeset
            )
            return DocumentClassifierResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(
            f"Error in /aws/comprehend/delete_document_classifier endpoint: {error}"
        )
        raise error


@comprehend_router.post(
    "/aws/comprehend/delete_entity_recognizer",
    response_model=EntiyRecognizerResponse,
)
async def delete_entity_recognizer(
    delete_entity_recognizer_request: EntityRecognizer,
    token: str = Depends(oauth2_scheme),
):
    """[API router to delete document classifier using AWS Comprehend]

    Args:
        delete_document_classifier_requeset (EntityRecognizer): [Delete Document classifier request]
        token (str, optional): [Bearer token for authentication]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized exception when invalid token is passed]
        error: [Exception in underlying controller]

    Returns:
        [EntiyRecognizerResponse]: [Response from AWS Comprehend]
    """
    try:
        logging.info("Calling /aws/comprehend/delete_document_classifier endpoint")
        logging.debug(f"Request: {delete_entity_recognizer_request}")
        if decodeJWT(token=token):
            response = ComprehendController().delete_entity_recognizer_controller(
                delete_entity_recognizer_request
            )
            return EntiyRecognizerResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(
            f"Error in /aws/comprehend/delete_entity_recognizer endpoint: {error}"
        )
        raise error


@comprehend_router.post("/aws/comprehend/describe_document_classifier")
async def describe_document_classifier(
    describe_document_classifier_request: DocumentClassifier,
    token: str = Depends(oauth2_scheme),
):
    """[API router to describe document classifier using AWS Comprehend]

    Args:
        describe_document_classifier_request (DocumentClassifier): [Describe Document classifier request]
        token (str, optional): [Bearer token for authentication]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized exception when invalid token is passed]
        error: [Exception in underlying controller]

    Returns:
        [dict]: [Response with all the document classifier details]
    """
    try:
        logging.info("Calling /aws/comprehend/describe_document_classifier endpoint")
        logging.debug(f"Request: {describe_document_classifier_request}")
        if decodeJWT(token=token):
            response = ComprehendController().describe_document_classifier_controller(
                describe_document_classifier_request
            )
            return response
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(
            f"Error in /aws/comprehend/describe_document_classifier endpoint: {error}"
        )
        raise error


@comprehend_router.post("/aws/comprehend/describe_document_classifier_status")
async def describe_document_classifier_status(
    describe_document_classifier_status_request: DocumentClassifier,
    token: str = Depends(oauth2_scheme),
):
    """[API router to describe document classifier status using AWS Comprehend]

    Args:
        describe_document_classifier_request (DocumentClassifier): [Describe Document classifier request]
        token (str, optional): [Bearer token for authentication]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized exception when invalid token is passed]
        error: [Exception in underlying controller]

    Returns:
        [dict]: [Response with all the document classifier details]
    """
    try:
        logging.info("Calling /aws/comprehend/describe_document_classifier endpoint")
        logging.debug(f"Request: {describe_document_classifier_status_request}")
        if decodeJWT(token=token):
            response = (
                ComprehendController().describe_document_classifier_status_controller(
                    describe_document_classifier_status_request
                )
            )
            return response
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(
            f"Error in /aws/comprehend/describe_document_classifier_status endpoint: {error}"
        )
        raise error


@comprehend_router.post("/aws/comprehend/describe_entity_recognizer")
async def describe_entity_recognizer(
    describe_entity_recognizer_request: EntityRecognizer,
    token: str = Depends(oauth2_scheme),
):
    """[API router to describe Entity Recognizer using AWS Comprehend]

    Args:
        describe_entity_recognizer_request (EntityRecognizer): [Describe Entity Recognizer request]
        token (str, optional): [Bearer token for authentication]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized exception when invalid token is passed]
        error: [Exception in underlying controller]

    Returns:
        [dict]: [Response with all the entity recognizer details]
    """
    try:
        logging.info("Calling /aws/comprehend/describe_entity_recognizer endpoint")
        logging.debug(f"Request: {describe_entity_recognizer_request}")
        if decodeJWT(token=token):
            response = ComprehendController().describe_entity_recognizer_controller(
                describe_entity_recognizer_request
            )
            return response
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(
            f"Error in /aws/comprehend/describe_entity_recognizer endpoint: {error}"
        )
        raise error


@comprehend_router.post("/aws/comprehend/describe_entity_recognizer_status")
async def describe_entity_recognizer_status(
    describe_entity_recognizer_status_request: EntityRecognizer,
    token: str = Depends(oauth2_scheme),
):
    """[API router to describe Entity Recognizer using AWS Comprehend]

    Args:
        describe_entity_recognizer_request (EntityRecognizer): [Describe Entity Recognizer request]
        token (str, optional): [Bearer token for authentication]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized exception when invalid token is passed]
        error: [Exception in underlying controller]

    Returns:
        [dict]: [Response with all the entity recognizer details]
    """
    try:
        logging.info(
            "Calling /aws/comprehend/describe_entity_recognizer_status endpoint"
        )
        logging.debug(f"Request: {describe_entity_recognizer_status_request}")
        if decodeJWT(token=token):
            response = (
                ComprehendController().describe_entity_recognizer_status_controller(
                    describe_entity_recognizer_status_request
                )
            )
            return response
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(
            f"Error in /aws/comprehend/describe_entity_recognizer_status endpoint: {error}"
        )
        raise error


@comprehend_router.get("/aws/comprehend/list_document_classifier")
async def list_document_classifier(
    token: str = Depends(oauth2_scheme),
):
    """[API router to list all document classifier using AWS Comprehend]

    Args:
        token (str, optional): [Bearer token for authentication]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized exception when invalid token is passed]
        error: [Exception in underlying controller]

    Returns:
        [dict]: [list of all the document classifiers]
    """
    try:
        logging.info("Calling /aws/comprehend/list_document_classifier endpoint")
        if decodeJWT(token=token):
            response = ComprehendController().list_document_classifier_controller()
            return response
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(
            f"Error in /aws/comprehend/list_document_classifier endpoint: {error}"
        )
        raise error


@comprehend_router.get("/aws/comprehend/list_entity_recognizer")
async def list_entity_recognizer(
    token: str = Depends(oauth2_scheme),
):
    """[API router to list all document classifier using AWS Comprehend]

    Args:
        token (str, optional): [Bearer token for authentication]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized exception when invalid token is passed]
        error: [Exception in underlying controller]

    Returns:
        [dict]: [list of all the document classifiers]
    """
    try:
        logging.info("Calling /aws/comprehend/list_entity_recognizer endpoint")
        if decodeJWT(token=token):
            response = ComprehendController().list_entity_recognizer_controller()
            return response
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(
            f"Error in /aws/comprehend/list_entity_recognizer endpoint: {error}"
        )
        raise error


@comprehend_router.post(
    "/aws/comprehend/deploy_model", response_model=DeployModelResponse
)
async def deploy_model(
    deploy_model_request: DeployModel,
    token: str = Depends(oauth2_scheme),
):
    """[API router to deploy a document classifier using AWS Comprehend]

    Args:
        deploy_model_request (DeployModel): [Deploy AWS Comprehend classifier request]
        token (str, optional): [Bearer token for authentication]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized exception when invalid token is passed]
        error: [Exception in underlying controller]

    Returns:
        [DeployModelResponse]: [Deployed model response]
    """
    try:
        logging.info("Calling /aws/comprehend/deploy_model endpoint")
        logging.debug(f"Request: {deploy_model_request}")
        if decodeJWT(token=token):
            response = ComprehendController().deploy_model_controller(
                deploy_model_request
            )
            return DeployModelResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /aws/comprehend/deploy_model endpoint: {error}")
        raise error


@comprehend_router.post(
    "/aws/comprehend/undeploy_model", response_model=UnDeployModelResponse
)
async def undeploy_model(
    undeploy_model_request: UnDeployModel,
    token: str = Depends(oauth2_scheme),
):
    """[API router to undeploy a document classifier using AWS Comprehend]

    Args:
        undeploy_model_request (UnDeployModel): [Un-Deploy AWS Comprehend classifier request]
        token (str, optional): [Bearer token for authentication]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized exception when invalid token is passed]
        error: [Exception in underlying controller]

    Returns:
        [UnDeployModelResponse]: [Un-Deployed model response]
    """
    try:
        logging.info("Calling /aws/comprehend/undeploy_model endpoint")
        logging.debug(f"Request: {undeploy_model_request}")
        if decodeJWT(token=token):
            response = ComprehendController().undeploy_model_controller(
                undeploy_model_request
            )
            return UnDeployModelResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /aws/comprehend/undeploy_model endpoint: {error}")
        raise error


@comprehend_router.get("/aws/comprehend/get_predictions")
async def get_predictions(
    endpoint_arn: str, text: str, token: str = Depends(oauth2_scheme)
):
    """[API router to get predicts from a AWS Comprehend document classifier]

    Args:
        endpoint_arn (str): [Deployed AWS Comprehend model endpoint]
        text (str): [text to be classified]
        token (str, optional): [Bearer token for authentication]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Unauthorized exception when invalid token is passed]
        error: [Exception in underlying controller]

    Returns:
        [dict]: [Prediction results]
    """
    try:
        logging.info("Calling /aws/comprehend/get_predictions endpoint")
        logging.debug(f"Request: {endpoint_arn=},{text=}")
        if decodeJWT(token=token):
            return ComprehendController().get_predictions_controller(
                endpoint_arn=endpoint_arn, text=text
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        logging.error(f"Error in /aws/comprehend/get_predictions endpoint: {error}")
        raise error
