import boto3
import subprocess
import json

client = boto3.client("comprehend")


def create_document_classifier(
    document_classifier_name: str,
    data_access_role_arn: str,
    input_data_config: dict,
    output_data_config: dict,
    language_code: str,
    classification_mode: str,
):
    response = client.create_document_classifier(
        DocumentClassifierName=document_classifier_name,
        DataAccessRoleArn=data_access_role_arn,
        InputDataConfig=input_data_config,
        OutputDataConfig=output_data_config,
        LanguageCode=language_code,
        Mode=classification_mode,
    )
    return {"document_classifier_arn": response["DocumentClassifierArn"]}


def delete_document_classifier(document_classifier_arn: str):
    client.delete_document_classifier(DocumentClassifierArn=document_classifier_arn)
    return {"status": "Deleted"}


def describe_document_classifier(document_classifier_arn: str):
    return client.describe_document_classifier(
        DocumentClassifierArn=document_classifier_arn
    )


def list_document_classifier():
    return client.list_document_classifiers()


def stop_training_document_classifier(document_classifier_arn: str):
    client.stop_training_document_classifier(
        DocumentClassifierArn=document_classifier_arn
    )
    return {"status": "Stopped"}


def deploy_document_classifier(
    min_inference_units: int, endpoint_name: str, model_arn: str
):

    bashCommand = f"aws comprehend create-endpoint --desired-inference-units {min_inference_units} --endpoint-name {endpoint_name} --model-arn {model_arn}"
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    response = json.loads(output.decode("UTF-8"))
    return {"endpoint_arn": response.get("EndpointArn", None)}


def undeploy_document_classifier(endpoint_arn: str):
    bashCommand = f"aws comprehend delete-endpoint --endpoint-arn {endpoint_arn}"
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()


def get_predictions(endpoint_arn: str, text: str):
    bashCommand = (
        f"aws comprehend classify-document --endpoint-arn {endpoint_arn} --text"
    )
    bashCommand_list = bashCommand.split()
    bashCommand_list.append(text)
    process = subprocess.Popen(bashCommand_list, stdout=subprocess.PIPE)
    output, error = process.communicate()
    return json.loads(output.decode("UTF-8"))