from google.cloud import storage

storage_client = storage.Client()


def upload_blob_string(
    bucket_name: str, file: bytes, destination_file_name: str, content_type: str
):
    """Uploads a file to the bucket."""
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_file_name)
    blob.upload_from_string(file, content_type=content_type)

    print("Uploaded to {}.".format(destination_file_name))
    gcs_uri = "gs://" + bucket_name + "/" + destination_file_name
    return gcs_uri
