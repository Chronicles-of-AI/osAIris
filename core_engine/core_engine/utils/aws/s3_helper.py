import boto3
import json
from datetime import datetime
from core_engine import logger

client = boto3.client("s3")
logging = logger(__name__)


def write_annotations_to_s3(bucket_name: str, byte_data: bytes, prefix: str):
    """[Write data to a file in S3]

    Args:
        bucket_name (str): [Output Bucket Name]
        byte_data (bytes): [Data]
        prefix (str): [File Name for S3]

    Raises:
        error: [Error]

    Returns:
        [type]: [S3 file path]
    """
    try:
        logging.info(f"Upload Annotations to S3: {bucket_name}, {prefix}")
        file_name = f"{prefix}/annotations_{str(int(datetime.now().timestamp())*10000)}.manifest"
        response = client.put_object(
            ACL="private",
            Body=byte_data,
            Bucket=bucket_name,
            Key=file_name,
        )
        return f"s3://{bucket_name}/{file_name}"
    except Exception as error:
        logging.error(f"{error=}")
        raise error


def read_annotations_from_s3(input_data_s3_uri: str):
    """[Read a file from S3]

    Args:
        input_data_s3_uri (str): [Input Data path from S3]

    Raises:
        error: [Error]

    Returns:
        [type]: [Annotations]
    """
    try:
        logging.info(f"Read Annotations from S3: {input_data_s3_uri}")
        bucket_name = input_data_s3_uri.split("//")[-1].split("/")[0]
        file_name = "/".join(input_data_s3_uri.split("//")[-1].split("/")[1:])
        response = client.get_object(Bucket=bucket_name, Key=file_name)
        annotations_data = json.loads(response["Body"].read().decode("UTF-8"))
        return annotations_data
    except Exception as error:
        logging.error(f"{error=}")
        raise error
