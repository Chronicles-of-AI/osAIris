import boto3

client = boto3.client("sagemaker")


def start_training_job(
    training_job,
    algorithm_specification,
    role_arn,
    input_data_config,
    output_data_config,
    resource_config,
    stopping_condition,
):
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


def stop_training_job(training_job_name: str):
    response = client.stop_training_job(TrainingJobName=training_job_name)
    return response


def describe_training_job(training_job_name: str):
    response = client.describe_training_job(TrainingJobName=training_job_name)
    return response


def list_training_job():
    response = client.list_training_jobs()
    return response
