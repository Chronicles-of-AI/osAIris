import boto3
from core_engine import logger

client = boto3.client("sagemaker")
logging = logger(__name__)


def start_training_job(
    training_job,
    algorithm_specification,
    role_arn,
    input_data_config,
    output_data_config,
    resource_config,
    stopping_condition,
):
    """[summary]

    Args:
        training_job ([type]): [Display Name for Training Job]
        algorithm_specification ([type]): [Pre-trained Algorithm if using from AWS]
        role_arn ([type]): [Role ARN used by AWS]
        input_data_config ([type]): [Input Dataset]
        output_data_config ([type]): [Output Bucket Name to dump training results]
        resource_config ([type]): [Basic Instance name]
        stopping_condition ([type]): [Stopping Condition]

    Raises:
        error: [Error]

    Returns:
        [type]: [Unique Identifier for your Training Job]
    """
    try:
        logging.info(f"Start Training Job: {training_job}")
        response = client.create_training_job(
            TrainingJobName=training_job,
            AlgorithmSpecification=algorithm_specification,
            RoleArn=role_arn,
            InputDataConfig=input_data_config,
            OutputDataConfig=output_data_config,
            ResourceConfig=resource_config,
            StoppingCondition=stopping_condition,
        )
        return response["TrainingJobArn"]
    except Exception as error:
        logging.error(f"{error=}")
        raise error


def stop_training_job(training_job_name: str):
    """[Stop a Training Job]

    Args:
        training_job_name (str): [Unique Identifier for your Training Job]

    Raises:
        error: [Error]

    Returns:
        [type]: [description]
    """
    try:
        logging.info(f"Stop Training Job: {training_job_name}")
        response = client.stop_training_job(TrainingJobName=training_job_name)
        return response
    except Exception as error:
        logging.error(f"{error=}")
        raise error


def describe_training_job(training_job_name: str):
    """[Describe a Training Job]

    Args:
        training_job_name (str): [Unique Identifier for your Training Job]

    Raises:
        error: [Error]

    Returns:
        [type]: [description]
    """
    try:
        logging.info(f"Describe Training Job :{training_job_name}")
        response = client.describe_training_job(TrainingJobName=training_job_name)
        return response
    except Exception as error:
        logging.error(f"{error=}")
        raise error


def list_training_job():
    """[List all Training Jobs]

    Raises:
        error: [Error]

    Returns:
        [type]: [List of training jobs]
    """
    try:
        logging.info(f"List Training Jobs")
        response = client.list_training_jobs()
        return response
    except Exception as error:
        logging.error(f"{error=}")
        raise error
