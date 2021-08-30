from fastapi import APIRouter
from core_engine.apis.schemas.requests.aws.comprehend_request import (
    CreateDocumentClassifier,
    CreateEntityRecognizer,
    DocumentClassifier,
    EntityRecognizer,
    DeployModel,
    UnDeployModel,
)
from core_engine.apis.schemas.response.aws.comprehend_response import (
    CreateDocumentClassifierResponse,
    CreateEntityRecognizerResponse,
    DocumentClassifierResponse,
    EntiyRecognizerResponse,
    DeployModelResponse,
    UnDeployModelResponse,
)
from core_engine.controllers.aws.comprehend_controller import ComprehendController
from core_engine import logger

logging = logger(__name__)

comprehend_router = APIRouter()


@comprehend_router.post(
    "/aws/comprehend/create_document_classifier",
    response_model=CreateDocumentClassifierResponse,
)
def create_document_classifier(
    create_document_classifier_request: CreateDocumentClassifier,
):
    """[Create a Document Classifier Router]

    Args:
        create_document_classifier_request (CreateDocumentClassifier): [Based on Input Schema]

    Raises:
        error: [Error]

    Returns:
        [type]: [Based on Response Model]
    """
    try:
        logging.info(
            f"Create Document Classifier Router: {create_document_classifier_request}"
        )
        response = ComprehendController().create_document_classifier_controller(
            create_document_classifier_request
        )
        return CreateDocumentClassifierResponse(**response)
    except Exception as error:
        logging.error(f"{error=}")
        raise error


@comprehend_router.post(
    "/aws/comprehend/create_entity_recognizer",
    response_model=CreateEntityRecognizerResponse,
)
def create_entity_recognizer(
    create_entity_recognizer_request: CreateEntityRecognizer,
):
    """[Create a Entity Recognizer Router]

    Args:
        create_entity_recognizer_request (CreateEntityRecognizer): [Based on Input Schema]

    Raises:
        error: [Error]

    Returns:
        [type]: [Based on Response Model]
    """
    try:
        logging.info(
            f"Create Entity Recognizer Router: {create_entity_recognizer_request}"
        )
        response = ComprehendController().create_entity_recognizer_controller(
            create_entity_recognizer_request
        )
        return CreateEntityRecognizerResponse(**response)
    except Exception as error:
        logging.error(f"{error=}")
        raise error


@comprehend_router.post(
    "/aws/comprehend/stop_training_document_classifier",
    response_model=DocumentClassifierResponse,
)
def stop_training_document_classifier(
    stop_training_document_classifier_request: DocumentClassifier,
):
    """[Stop Training a Document Classifier Router]

    Args:
        stop_training_document_classifier_request (DocumentClassifier): [Based on Input Schema]

    Raises:
        error: [Error]

    Returns:
        [type]: [Based on Response Model]
    """
    try:
        logging.info(
            f"Stop Training Document Classifier Router: {stop_training_document_classifier_request}"
        )
        response = ComprehendController().stop_training_document_classifier_controller(
            stop_training_document_classifier_request
        )
        return DocumentClassifierResponse(**response)
    except Exception as error:
        logging.error(f"{error=}")
        raise error


@comprehend_router.post(
    "/aws/comprehend/stop_training_entity_recognizer",
    response_model=EntiyRecognizerResponse,
)
def stop_training_entity_recognizer(
    stop_training_entity_recognizer_request: EntityRecognizer,
):
    """[Stop Training a Entity Recognizer Router]

    Args:
        stop_training_entity_recognizer_request (EntityRecognizer): [Based on Input Schema]

    Raises:
        error: [Error]

    Returns:
        [type]: [Based on Response Model]
    """
    try:
        logging.info(
            f"Stop Training Entity Recognizer Router: {stop_training_entity_recognizer_request}"
        )
        response = ComprehendController().stop_training_entity_recognizer_controller(
            stop_training_entity_recognizer_request
        )
        return DocumentClassifierResponse(**response)
    except Exception as error:
        logging.error(f"{error=}")
        raise error


@comprehend_router.post(
    "/aws/comprehend/delete_document_classifier",
    response_model=DocumentClassifierResponse,
)
def delete_document_classifier(
    delete_document_classifier_requeset: DocumentClassifier,
):
    """[Delete a Document Classifier Router]

    Args:
        delete_document_classifier_requeset (DocumentClassifier): [Based on Input Schema]

    Raises:
        error: [Error]

    Returns:
        [type]: [Based on Response Model]
    """
    try:
        logging.info(
            f"Delete Document Classifier Router: {delete_document_classifier_requeset}"
        )
        response = ComprehendController().delete_document_classifier_controller(
            delete_document_classifier_requeset
        )
        return DocumentClassifierResponse(**response)
    except Exception as error:
        logging.error(f"{error=}")
        raise error


@comprehend_router.post(
    "/aws/comprehend/delete_entity_recognizer",
    response_model=EntiyRecognizerResponse,
)
def delete_entity_recognizer(
    delete_entity_recognizer_request: EntityRecognizer,
):
    """[Delete a Entity Recognizer Router]

    Args:
        delete_document_classifier_requeset (DocumentClassifier): [Based on Input Schema]

    Raises:
        error: [Error]

    Returns:
        [type]: [Based on Response Model]
    """
    try:
        logging.info(
            f"Delete Entity Recognizer Router: {delete_entity_recognizer_request}"
        )
        response = ComprehendController().delete_entity_recognizer_controller(
            delete_entity_recognizer_request
        )
        return EntiyRecognizerResponse(**response)
    except Exception as error:
        logging.error(f"{error=}")
        raise error


@comprehend_router.post("/aws/comprehend/describe_document_classifier")
def describe_document_classifier(
    describe_document_classifier_request: DocumentClassifier,
):
    """[Describe a Document Classifier Router]

    Args:
        describe_document_classifier_request (DocumentClassifier): [Based on Input Schema]

    Raises:
        error: [Error]

    Returns:
        [type]: [Based on Response Model]
    """
    try:
        logging.info(
            f"Describe Document Classifier Router: {describe_document_classifier_request}"
        )
        response = ComprehendController().describe_document_classifier_controller(
            describe_document_classifier_request
        )
        return response
    except Exception as error:
        logging.error(f"{error=}")
        raise error


@comprehend_router.post("/aws/comprehend/describe_entity_recognizer")
def describe_entity_recognizer(
    describe_entity_recognizer_request: EntityRecognizer,
):
    """[Describe a Entity Recognizer Router]

    Args:
        describe_entity_recognizer_request (EntityRecognizer): [Based on Input Schema]

    Raises:
        error: [Error]

    Returns:
        [type]: [Based on Response Model]
    """
    try:
        logging.info(
            f"Describe Entity Recognizer Router: {describe_entity_recognizer_request}"
        )
        response = ComprehendController().describe_entity_recognizer_controller(
            describe_entity_recognizer_request
        )
        return response
    except Exception as error:
        logging.error(f"{error=}")
        raise error


@comprehend_router.get("/aws/comprehend/list_document_classifier")
def list_document_classifier():
    """[Lists Document Classifiers Router]

    Raises:
        error: [Error]

    Returns:
        [type]: [Based on Response Model]
    """
    try:
        logging.info(f"List Document Classifier Router")
        response = ComprehendController().list_document_classifier_controller()
        return response
    except Exception as error:
        logging.error(f"{error=}")
        raise error


@comprehend_router.get("/aws/comprehend/list_entity_recognizer")
def list_entity_recognizer():
    """[Lists Entity Recognizer Router]

    Raises:
        error: [Error]

    Returns:
        [type]: [Based on Response Model]
    """
    try:
        logging.info(f"List Entity Recognizer Router")
        response = ComprehendController().list_entity_recognizer_controller()
        return response
    except Exception as error:
        logging.error(f"{error=}")
        raise error


@comprehend_router.post(
    "/aws/comprehend/deploy_document_classifier", response_model=DeployModelResponse
)
def deploy_document_classifier(deploy_model_request: DeployModel):
    """[Deploy a Document Classifier Router]

    Args:
        deploy_model_request (DeployModel): [Based on Input Schema]

    Raises:
        error: [Error]

    Returns:
        [type]: [Based on Response Model]
    """
    try:
        logging.info(f"Deploy Document Classifier Router: {deploy_model_request}")
        response = ComprehendController().deploy_document_classifier_controller(
            deploy_model_request
        )
        return DeployModelResponse(**response)
    except Exception as error:
        logging.error(f"{error=}")
        raise error


@comprehend_router.post(
    "/aws/comprehend/undeploy_document_classifier", response_model=UnDeployModelResponse
)
def undeploy_document_classifier(undeploy_model_request: UnDeployModel):
    """[Un-Deploy a Document Classifier Router]

    Args:
        undeploy_model_request (UnDeployModel): [Based on Input Schema]

    Raises:
        error: [Error]

    Returns:
        [type]: [Based on Response Model]
    """
    try:
        logging.info(f"Un-Deploy Document Classifier Router: {undeploy_model_request}")
        response = ComprehendController().undeploy_document_classifier_controller(
            undeploy_model_request
        )
        return UnDeployModelResponse(**response)
    except Exception as error:
        logging.error(f"{error=}")
        raise error


@comprehend_router.get("/aws/comprehend/get_predictions")
def get_predictions(endpoint_arn: str, text: str):
    """[Get predictions from a Document Classifier Router]

    Args:
        endpoint_arn (str): [End point ARN]
        text (str): [Sample Text]

    Raises:
        error: [Error]

    Returns:
        [type]: [Based on Response Model]
    """
    try:
        logging.info(f"Get Predictions Document Classifier Router: {endpoint_arn}")
        return ComprehendController().get_predictions_controller(
            endpoint_arn=endpoint_arn, text=text
        )
    except Exception as error:
        logging.error(f"{error=}")
        raise error
