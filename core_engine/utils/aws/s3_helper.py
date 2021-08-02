import boto3
import json
from datetime import datetime

client = boto3.client("s3")


def write_annotations_to_s3(bucket_name: str, byte_data: bytes, prefix: str):
    file_name = (
        f"{prefix}/annotations_{str(int(datetime.now().timestamp())*10000)}.manifest"
    )
    response = client.put_object(
        ACL="private",
        Body=byte_data,
        Bucket=bucket_name,
        Key=file_name,
    )
    return f"s3://{bucket_name}/{file_name}"


def read_annotations_from_s3(input_data_s3_uri: str):
    bucket_name = input_data_s3_uri.split("//")[-1].split("/")[0]
    file_name = "/".join(input_data_s3_uri.split("//")[-1].split("/")[1:])
    response = client.get_object(Bucket=bucket_name, Key=file_name)
    annotations_data = json.loads(response["Body"].read().decode("UTF-8"))
    return annotations_data
