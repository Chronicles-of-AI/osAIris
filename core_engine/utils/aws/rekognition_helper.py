import boto3

client = boto3.client("rekognition")


def create_project(project_name):

    # Create a project
    print("Creating project:" + project_name)
    response = client.create_project(ProjectName=project_name)
    print("project ARN: " + response["ProjectArn"])
    print("Done...")
    return response["ProjectArn"]


def delete_project(project_arn):

    # Delete a project
    print("Deleting project:" + project_arn)
    response = client.delete_project(ProjectArn=project_arn)
    print("Status: " + response["Status"])
    print("Done...")
    return response["Status"]


def get_all_projects():
    return client.describe_projects()


def version_description(project_arn: str, version_name: str = None):
    # Get the completion status
    if version_name:
        describe_response = client.describe_project_versions(
            ProjectArn=project_arn, VersionNames=[version_name]
        )
    else:
        describe_response = client.describe_project_versions(ProjectArn=project_arn)
    return describe_response


def train_model(
    project_arn, version_name, output_config, training_dataset, testing_dataset
):
    print("Training Started: " + version_name)

    try:
        response = client.create_project_version(
            ProjectArn=project_arn,
            VersionName=version_name,
            OutputConfig=output_config,
            TrainingData=training_dataset,
            TestingData=testing_dataset,
        )
        return response["ProjectVersionArn"]
    except Exception as e:
        print(e)


def start_model(project_version_arn, min_inference_units):
    try:
        # Start the model
        print("Starting model: " + project_version_arn)
        response = client.start_project_version(
            ProjectVersionArn=project_version_arn, MinInferenceUnits=min_inference_units
        )
        return response["Status"]
    except Exception as e:
        print(e)


def stop_model(project_version_arn):
    print("Stopping model:" + project_version_arn)

    # Stop the model
    try:
        response = client.stop_project_version(ProjectVersionArn=project_version_arn)
        return response["Status"]
    except Exception as e:
        print(e)


def delete_model(project_version_arn):
    try:
        response = client.delete_project_version(ProjectVersionArn=project_version_arn)
        return response["Status"]
    except Exception as e:
        print(e)


def get_predictions(
    project_version_arn: str, bucket: str, file_prefix: str, min_confidence: int
):
    response = client.detect_custom_labels(
        Image={"S3Object": {"Bucket": bucket, "Name": file_prefix}},
        MinConfidence=min_confidence,
        ProjectVersionArn=project_version_arn,
    )

    return response.get("CustomLabels", None)
