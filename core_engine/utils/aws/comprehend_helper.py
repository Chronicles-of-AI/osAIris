import boto3
import subprocess
import json
from core_engine import logger

client = boto3.client("comprehend")
logging = logger(__name__)


def create_document_classifier(
    document_classifier_name: str,
    data_access_role_arn: str,
    input_data_config: dict,
    output_data_config: dict,
    language_code: str,
    classification_mode: str,
):
    """[Creates a Document Classifier for Text Classification on AWS]

    Args:
        document_classifier_name (str): [Sample name]
        data_access_role_arn (str): [Role used by AWS]
        input_data_config (dict): [Input Dataset]
        output_data_config (dict): [Output bucket to dump all the results]
        language_code (str): [Language]
        classification_mode (str): [MULTICLASS / MULTILABEL]

    Raises:
        error: [description]

    Returns:
        [type]: [Unique Identifier for Document Classifier]
    """
    try:
        logging.info(f"Create Document Classifier: {document_classifier_name}")
        logging.info(f"{classification_mode=}")
        logging.info(f"{input_data_config=}")
        response = client.create_document_classifier(
            DocumentClassifierName=document_classifier_name,
            DataAccessRoleArn=data_access_role_arn,
            InputDataConfig=input_data_config,
            OutputDataConfig=output_data_config,
            LanguageCode=language_code,
            Mode=classification_mode,
        )
        return {"document_classifier_arn": response["DocumentClassifierArn"]}
    except Exception as error:
        logging.error(f"{error=}")
        raise error


def delete_document_classifier(document_classifier_arn: str):
    """[Deletes a Document Classifier for Text Classification on AWS]

    Args:
        document_classifier_arn (str): [Unique Identifier for Document Classifier]

    Raises:
        error: [description]

    Returns:
        [type]: [description]
    """
    try:
        logging.info(f"Delete Document Classifier: {document_classifier_arn}")
        client.delete_document_classifier(DocumentClassifierArn=document_classifier_arn)
        return {"status": "Deleted"}
    except Exception as error:
        logging.error(f"{error=}")
        raise error


def describe_document_classifier(document_classifier_arn: str):
    """[Describes a Document Classifier for Text Classification on AWS]

    Args:
        document_classifier_arn (str): [description]

    Raises:
        error: [Error]

    Returns:
        [type]: [Description of Document Classifier]
    """
    try:
        logging.info(f"Describe Document Classifier: {document_classifier_arn}")
        return client.describe_document_classifier(
            DocumentClassifierArn=document_classifier_arn
        )
    except Exception as error:
        logging.error(f"{error=}")
        raise error


def list_document_classifier():
    """[Lists Document Classifiers for Text Classification on AWS]

    Raises:
        error: [description]

    Returns:
        [list]: [List of Document Classifiers]
    """
    try:
        logging.info(f"List Document Classifiers")
        return client.list_document_classifiers()
    except Exception as error:
        logging.error(f"{error=}")
        raise error


def stop_training_document_classifier(document_classifier_arn: str):
    """[Stops Training a Document Classifier for Text Classification on AWS]

    Args:
        document_classifier_arn (str): [Unique Identifier for Document Classifier]

    Raises:
        error: [Error]

    Returns:
        [dict]: [Status]
    """
    try:
        logging.info(f"Stop Training Document Classifier: {document_classifier_arn}")
        client.stop_training_document_classifier(
            DocumentClassifierArn=document_classifier_arn
        )
        return {"status": "Stopped"}
    except Exception as error:
        logging.error(f"{error=}")
        raise error


def deploy_document_classifier(
    min_inference_units: int, endpoint_name: str, model_arn: str
):
    """[Deploys a Document Classifier for Text Classification on AWS]

    Args:
        min_inference_units (int): [Minimun Inference units based on demands]
        endpoint_name (str): [End point Name]
        model_arn (str): [Model Identifier from AWS]

    Raises:
        error: [Error]

    Returns:
        [type]: [End point name]
    """
    try:
        logging.info(f"Deploy Document Classifier: {endpoint_name}")
        logging.info(f"{model_arn=}")
        response = client.create_endpoint(
            EndpointName=endpoint_name,
            ModelArn=model_arn,
            DesiredInferenceUnits=min_inference_units,
        )
        # bashCommand = f"aws comprehend create-endpoint --desired-inference-units {min_inference_units} --endpoint-name {endpoint_name} --model-arn {model_arn}"
        # process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
        # output, error = process.communicate()
        # response = json.loads(output.decode("UTF-8"))
        return {"endpoint_arn": response.get("EndpointArn", None)}
    except Exception as error:
        logging.error(f"{error=}")
        raise error


def undeploy_document_classifier(endpoint_arn: str):
    """[Un-deploys a Document Classifier for Text Classification on AWS]

    Args:
        endpoint_arn (str): [End point name]

    Raises:
        error: [Error]
    """
    try:
        logging.info(f"Deploy Document Classifier: {endpoint_arn}")
        response = client.delete_endpoint(EndpointArn=endpoint_arn)
        # bashCommand = f"aws comprehend delete-endpoint --endpoint-arn {endpoint_arn}"
        # process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
        # output, error = process.communicate()
    except Exception as error:
        logging.error(f"{error=}")
        raise error


def get_predictions(endpoint_arn: str, text: str):
    """[Gets predictions from a Document Classifier for Text Classification on AWS]

    Args:
        endpoint_arn (str): [End point names]
        text (str): [sample input text]

    Raises:
        error: [Error]

    Returns:
        [type]: [Predictions]
    """
    try:
        response = client.classify_document(Text=text, EndpointArn=endpoint_arn)
        # bashCommand = (
        #     f"aws comprehend classify-document --endpoint-arn {endpoint_arn} --text"
        # )
        # bashCommand_list = bashCommand.split()
        # bashCommand_list.append(text)
        # process = subprocess.Popen(bashCommand_list, stdout=subprocess.PIPE)
        # output, error = process.communicate()
        return json.loads(response)
    except Exception as error:
        raise error
