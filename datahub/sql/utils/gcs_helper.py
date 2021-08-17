import logging
from google.cloud import storage
from sql import logger

storage_client = storage.Client()

logging = logger(__name__)


def upload_blob_string(
    bucket_name: str, file: bytes, destination_file_name: str, content_type: str
):
    """[The function uploads the file directly to GCS bucket]

    Args:
        bucket_name (str): [GCS bucket name]
        file (bytes): [File to be uploaded to cloud bucket]
        destination_file_name (str): [File name of GCS bucket]
        content_type (str): [Type of file]

    Raises:
        error: [Error in file upload]

    Returns:
        [str]: [GCS URI for uploaded file]
    """
    try:
        logging.info("Upload to GCS bucket")
        """Uploads a file to the bucket."""
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(destination_file_name)
        blob.upload_from_string(file, content_type=content_type)
        gcs_uri = "gs://" + bucket_name + "/" + destination_file_name
        return gcs_uri
    except Exception as error:
        logging.error(f"Error in uplaoding file to GCS bucket : {error}")
        raise error
