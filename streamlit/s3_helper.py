from attr import dataclass
import boto3
from datetime import datetime

s3 = boto3.client("s3")


def upload_file_obj(file_data: bytes):
    print(type(file_data))
    file_id = str(int(datetime.now().timestamp()))
    bucket_name = "mlops-label-studio-datasource"
    s3.put_object(
        ACL="private",
        Body=file_data,
        Bucket=bucket_name,
        Key=f"test_images/{file_id}.jpg",
    )
    return f"s3://{bucket_name}/test_images/{file_id}.jpg"
