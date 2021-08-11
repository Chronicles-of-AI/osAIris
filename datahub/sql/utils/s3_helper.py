import boto3
import json
from datetime import datetime
from sql import logger

logging = logger(__name__)
client = boto3.client("s3")


def write_annotations_to_s3(bucket_name: str, json_data: dict, prefix: str):
    """[The function uploads the file directly to S3 bucket]

    Args:
        bucket_name (str): [S3 bucket name the file needs to be uploaded to]
        json_data (dict): [file content in json format]
        prefix (str): [file prefix on S3 bucket]

    Raises:
        error: [Error raised by BOTO3 client]

    Returns:
        [str]: [S3 URI of the file uploaded]
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
    """[This function is used to read a file from S3 bucket]

    Args:
        input_data_s3_uri (str): [S3 URI of the file to be read]

    Raises:
        error: [Error raised by BOTO3 client]

    Returns:
        [dict]: [annotation data read from the S3 file]
    """
    try:
        bucket_name = input_data_s3_uri.split("//")[-1].split("/")[0]
        file_name = "/".join(input_data_s3_uri.split("//")[-1].split("/")[1:])
        response = client.get_object(Bucket=bucket_name, Key=file_name)
        annotations_data = json.loads(response["Body"].read().decode("UTF-8"))
        return annotations_data
    except Exception as error:
        raise error
