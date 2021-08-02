from fastapi import APIRouter
from apis.schemas.requests.aws.comprehend_request import (
    CreateDocumentClassifier,
    DocumentClassifier,
    DeployModel,
    UnDeployModel,
)
from apis.schemas.response.aws.comprehend_response import (
    CreateDocumentClassifierResponse,
    DocumentClassifierResponse,
    DeployModelResponse,
    UnDeployModelResponse,
)
from controllers.aws.comprehend_controller import ComprehendController

comprehend_router = APIRouter()


@comprehend_router.post(
    "/aws/comprehend/create_document_classifier",
    response_model=CreateDocumentClassifierResponse,
)
def create_document_classifier(
    create_document_classifier_request: CreateDocumentClassifier,
):
    response = ComprehendController().create_document_classifier_controller(
        create_document_classifier_request
    )
    return CreateDocumentClassifierResponse(**response)


@comprehend_router.post(
    "/aws/comprehend/stop_training_document_classifier",
    response_model=DocumentClassifierResponse,
)
def stop_training_document_classifier(
    stop_training_document_classifier_request: DocumentClassifier,
):
    response = ComprehendController().stop_training_document_classifier_controller(
        stop_training_document_classifier_request
    )
    return DocumentClassifierResponse(**response)


@comprehend_router.post(
    "/aws/comprehend/delete_document_classifier",
    response_model=DocumentClassifierResponse,
)
def delete_document_classifier(
    delete_document_classifier_requeset: DocumentClassifier,
):
    response = ComprehendController().delete_document_classifier_controller(
        delete_document_classifier_requeset
    )
    return DocumentClassifierResponse(**response)


@comprehend_router.post("/aws/comprehend/describe_document_classifier")
def describe_document_classifier(
    describe_document_classifier_request: DocumentClassifier,
):
    response = ComprehendController().describe_document_classifier_controller(
        describe_document_classifier_request
    )
    return response


@comprehend_router.get("/aws/comprehend/list_document_classifier")
def list_document_classifier():
    response = ComprehendController().list_document_classifier_controller()
    return response


@comprehend_router.post(
    "/aws/comprehend/deploy_document_classifier", response_model=DeployModelResponse
)
def deploy_document_classifier(deploy_model_request: DeployModel):
    response = ComprehendController().deploy_document_classifier_controller(
        deploy_model_request
    )
    return DeployModelResponse(**response)


@comprehend_router.post(
    "/aws/comprehend/undeploy_document_classifier", response_model=UnDeployModelResponse
)
def undeploy_document_classifier(undeploy_model_request: UnDeployModel):
    response = ComprehendController().undeploy_document_classifier_controller(
        undeploy_model_request
    )
    return UnDeployModelResponse(**response)


@comprehend_router.get("/aws/comprehend/get_predictions")
def get_predictions(endpoint_arn: str, text: str):
    return ComprehendController().get_predictions_controller(
        endpoint_arn=endpoint_arn, text=text
    )
