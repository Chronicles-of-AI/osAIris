import boto3
import json
from datetime import datetime
from sql import logger

logging = logger(__name__)
client = boto3.client("s3")


def write_annotations_to_s3(bucket_name: str, json_data: dict, prefix: str):
    """[summary]

    Args:
        bucket_name (str): [description]
        json_data (dict): [description]
        prefix (str): [description]

    Raises:
        error: [description]

    Returns:
        [type]: [description]
    """
    try:
        file_name = f"{prefix}/annotations_{str(datetime.now().timestamp())}.json"
        response = client.put_object(
            ACL="private",
            Body=bytes(json.dumps(json_data).encode("UTF-8")),
            Bucket=bucket_name,
            Key=file_name,
        )
        return f"s3://{bucket_name}/{file_name}"
    except Exception as error:
        raise error


def read_annotations_from_s3(input_data_s3_uri: str):
    """[summary]

    Args:
        input_data_s3_uri (str): [description]

    Raises:
        error: [description]

    Returns:
        [type]: [description]
    """
    try:
        bucket_name = input_data_s3_uri.split("//")[-1].split("/")[0]
        file_name = "/".join(input_data_s3_uri.split("//")[-1].split("/")[1:])
        response = client.get_object(Bucket=bucket_name, Key=file_name)
        annotations_data = json.loads(response["Body"].read().decode("UTF-8"))
        return annotations_data
    except Exception as error:
        raise error
