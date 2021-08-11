from fastapi import APIRouter, Depends, HTTPException, status
from sql.apis.schemas.requests.aws.comprehend_request import (
    CreateDocumentClassifier,
    DocumentClassifier,
    DeployModel,
    UnDeployModel,
)
from sql.apis.schemas.responses.aws.comprehend_response import (
    CreateDocumentClassifierResponse,
    DocumentClassifierResponse,
    DeployModelResponse,
    UnDeployModelResponse,
)
from sql.controllers.aws.comprehend_controller import ComprehendController
from fastapi.security import OAuth2PasswordBearer
from commons.auth import decodeJWT

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")
comprehend_router = APIRouter()


@comprehend_router.post(
    "/aws/comprehend/create_document_classifier",
    response_model=CreateDocumentClassifierResponse,
)
def create_document_classifier(
    create_document_classifier_request: CreateDocumentClassifier,
    token: str = Depends(oauth2_scheme),
):
    """[summary]

    Args:
        create_document_classifier_request (CreateDocumentClassifier): [description]
        token (str, optional): [description]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [description]
        e: [description]

    Returns:
        [type]: [description]
    """
    try:
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
    except Exception as e:
        raise e


@comprehend_router.post(
    "/aws/comprehend/stop_training_document_classifier",
    response_model=DocumentClassifierResponse,
)
def stop_training_document_classifier(
    stop_training_document_classifier_request: DocumentClassifier,
    token: str = Depends(oauth2_scheme),
):
    """[summary]

    Args:
        stop_training_document_classifier_request (DocumentClassifier): [description]
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
        raise error


@comprehend_router.post(
    "/aws/comprehend/delete_document_classifier",
    response_model=DocumentClassifierResponse,
)
def delete_document_classifier(
    delete_document_classifier_requeset: DocumentClassifier,
    token: str = Depends(oauth2_scheme),
):
    """[summary]

    Args:
        delete_document_classifier_requeset (DocumentClassifier): [description]
        token (str, optional): [description]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [description]
        error: [description]

    Returns:
        [type]: [description]
    """
    try:
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
        raise error


@comprehend_router.post("/aws/comprehend/describe_document_classifier")
def describe_document_classifier(
    describe_document_classifier_request: DocumentClassifier,
    token: str = Depends(oauth2_scheme),
):
    """[summary]

    Args:
        describe_document_classifier_request (DocumentClassifier): [description]
        token (str, optional): [description]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [description]
        error: [description]

    Returns:
        [type]: [description]
    """
    try:
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
        raise error


@comprehend_router.get("/aws/comprehend/list_document_classifier")
def list_document_classifier(
    token: str = Depends(oauth2_scheme),
):
    """[summary]

    Args:
        token (str, optional): [description]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [description]
        error: [description]

    Returns:
        [type]: [description]
    """
    try:
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
        raise error


@comprehend_router.post(
    "/aws/comprehend/deploy_document_classifier", response_model=DeployModelResponse
)
def deploy_document_classifier(
    deploy_model_request: DeployModel,
    token: str = Depends(oauth2_scheme),
):
    """[summary]

    Args:
        deploy_model_request (DeployModel): [description]
        token (str, optional): [description]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [description]
        error: [description]

    Returns:
        [type]: [description]
    """
    try:
        if decodeJWT(token=token):
            response = ComprehendController().deploy_document_classifier_controller(
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
        raise error


@comprehend_router.post(
    "/aws/comprehend/undeploy_document_classifier", response_model=UnDeployModelResponse
)
def undeploy_document_classifier(
    undeploy_model_request: UnDeployModel,
    token: str = Depends(oauth2_scheme),
):
    """[summary]

    Args:
        undeploy_model_request (UnDeployModel): [description]
        token (str, optional): [description]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [description]
        error: [description]

    Returns:
        [type]: [description]
    """
    try:
        if decodeJWT(token=token):
            response = ComprehendController().undeploy_document_classifier_controller(
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
        raise error


@comprehend_router.get("/aws/comprehend/get_predictions")
def get_predictions(endpoint_arn: str, text: str, token: str = Depends(oauth2_scheme)):
    """[summary]

    Args:
        endpoint_arn (str): [description]
        text (str): [description]
        token (str, optional): [description]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [description]
        error: [description]

    Returns:
        [type]: [description]
    """
    try:
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
        raise error
