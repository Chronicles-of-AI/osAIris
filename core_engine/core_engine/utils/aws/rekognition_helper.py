import boto3
from core_engine import logger

client = boto3.client("rekognition")
logging = logger(__name__)


def create_project(project_name):
    """[Creates a Project on Rekognition in AWS]

    Args:
        project_name ([type]): [Display name for AWS]

    Raises:
        error: [Error]

    Returns:
        [type]: [Unique Identifier for a Project on Rekognition in AWS]
    """
    try:
        # Create a project
        logging.info("Creating project:" + project_name)
        response = client.create_project(ProjectName=project_name)
        logging.info("project ARN: " + response["ProjectArn"])
        logging.info("Done...")
        return response["ProjectArn"]
    except Exception as error:
        logging.error(f"{error=}")
        raise error


def delete_project(project_arn):
    """[Deletes a Project on Rekognition in AWS]

    Args:
        project_arn ([type]): [Unique Identifier for a Project on Rekognition in AWS]

    Raises:
        error: [Error]

    Returns:
        [type]: [Status]
    """
    try:
        # Delete a project
        logging.info("Deleting project:" + project_arn)
        response = client.delete_project(ProjectArn=project_arn)
        logging.info("Status: " + response["Status"])
        logging.info("Done...")
        return response["Status"]
    except Exception as error:
        logging.error(f"{error=}")
        raise error


def get_all_projects():
    """[Lists all Projects on Rekognition in AWS]

    Raises:
        error: [Error]

    Returns:
        [list]: [List of Projects]
    """
    try:
        logging.info(f"Get all Projects")
        return client.describe_projects()
    except Exception as error:
        logging.error(f"{error=}")
        raise error


def version_description(project_arn: str, version_name: str = None):
    """[Describes a Project on Rekognition in AWS]

    Args:
        project_arn (str): [Unique Identifier for a Project on Rekognition in AWS]
        version_name (str, optional): [Display Name]. Defaults to None.

    Raises:
        error: [Error]

    Returns:
        [type]: [Description]
    """
    try:
        logging.info(f"Version Description: {project_arn}")
        # Get the completion status
        if version_name:
            describe_response = client.describe_project_versions(
                ProjectArn=project_arn, VersionNames=[version_name]
            )
        else:
            describe_response = client.describe_project_versions(ProjectArn=project_arn)
        return describe_response
    except Exception as error:
        logging.error(f"{error=}")
        raise error


def train_model(
    project_arn, version_name, output_config, training_dataset, testing_dataset
):
    """[Trains a Model on Rekognition in AWS]

    Args:
        project_arn ([type]): [Unique Identifier for a Project on Rekognition in AWS]
        version_name ([type]): [Display Name on AWS]
        output_config ([type]): [Output Bucket to dump training results]
        training_dataset ([type]): [Training Dataset]
        testing_dataset ([type]): [Testing Dataset]

    Raises:
        e: [Error]

    Returns:
        [type]: [Unique Identifier for a Project Version on Rekognition in AWS]
    """
    try:
        logging.info("Training Started: " + version_name)
        response = client.create_project_version(
            ProjectArn=project_arn,
            VersionName=version_name,
            OutputConfig=output_config,
            TrainingData=training_dataset,
            TestingData=testing_dataset,
        )
        return response["ProjectVersionArn"]
    except Exception as e:
        logging.error(e)
        raise e


def start_model(project_version_arn, min_inference_units):
    """[Deploys a Model on Rekognition in AWS]

    Args:
        project_version_arn ([type]): [Unique Identifier for a Project on Rekognition in AWS]
        min_inference_units ([type]): [Minimum Inference Units]

    Raises:
        e: [Error]

    Returns:
        [type]: [Status]
    """
    try:
        # Start the model
        logging.info("Starting model: " + project_version_arn)
        response = client.start_project_version(
            ProjectVersionArn=project_version_arn, MinInferenceUnits=min_inference_units
        )
        return response["Status"]
    except Exception as e:
        logging.error(e)
        raise e


def stop_model(project_version_arn):
    """[Un-deploys a Model on Rekognition in AWS]

    Args:
        project_version_arn ([type]): [Unique Identifier for a Project on Rekognition in AWS]

    Raises:
        e: [Error]

    Returns:
        [type]: [Status]
    """
    # Stop the model
    try:
        logging.info("Stopping model:" + project_version_arn)
        response = client.stop_project_version(ProjectVersionArn=project_version_arn)
        return response["Status"]
    except Exception as e:
        logging.error(e)
        raise e


def delete_model(project_version_arn):
    """[Deletes a Model on Rekognition in AWS]

    Args:
        project_version_arn ([type]): [Unique Identifier for a Project on Rekognition in AWS]

    Raises:
        e: [Error]

    Returns:
        [type]: [Status]
    """
    try:
        logging.info(f"Delete Model :{project_version_arn}")
        response = client.delete_project_version(ProjectVersionArn=project_version_arn)
        return response["Status"]
    except Exception as e:
        logging.error(e)
        raise e


def get_predictions(
    project_version_arn: str, bucket: str, file_prefix: str, min_confidence: int
):
    """[Gets Predictions from a Model on Rekognition in AWS]

    Args:
        project_version_arn (str): [Unique Identifier for a Project on Rekognition in AWS]
        bucket (str): [S3 Bucket name]
        file_prefix (str): [File path to the input data]
        min_confidence (int): [Confidence threshold]

    Raises:
        error: [Error]

    Returns:
        [type]: [Predictions]
    """
    try:
        logging.info(f"Get Predictions: {project_version_arn}")
        response = client.detect_custom_labels(
            Image={"S3Object": {"Bucket": bucket, "Name": file_prefix}},
            MinConfidence=min_confidence,
            ProjectVersionArn=project_version_arn,
        )

        return response.get("CustomLabels", None)
    except Exception as error:
        logging.error(f"{error=}")
        raise error
