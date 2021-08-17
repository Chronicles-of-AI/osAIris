from google.cloud import storage
from core_engine import logger

client = storage.Client()
logging = logger(__name__)


def read_file_from_gcs(file_path: str, bucket_name: str):
    """[Read File from GCS]

    Args:
        file_path (str): [File path of GCS]
        bucket_name (str): [Bucket Name to dump the output in]

    Raises:
        error: [Error]

    Returns:
        [type]: [description]
    """
    try:
        logging.info(f"Read from GCS file: {file_path}")
        bucket = client.get_bucket(bucket_name)
        blob = bucket.get_blob(file_path)
        data_string = blob.download_as_string()
        return bytes(data_string)
    except Exception as error:
        logging.error(f"{error=}")
        raise error


def upload_blob_string(
    bucket_name: str, destination_file_name: str, content_type: str, file
):
    """[Upload Data into a File in GCS]

    Args:
        bucket_name (str): [Output Bucket Name]
        destination_file_name (str): [Destination File Name in GCS]
        content_type (str): [Content]
        file ([type]): [description]

    Raises:
        error: [Error]

    Returns:
        [type]: [description]
    """
    try:
        logging.info(f"Upload to GCS bucket: {bucket_name}")
        logging.info(f"{destination_file_name}")
        """Uploads a file to the bucket."""

        bucket = client.bucket(bucket_name)
        blob = bucket.blob(destination_file_name)
        blob.upload_from_string(file, content_type=content_type)

        print("Uploaded to {}.".format(destination_file_name))
        gcs_uri = "gs://" + bucket_name + "/" + destination_file_name
        return gcs_uri
    except Exception as error:
        logging.error(f"{error=}")
        raise error
