from google.cloud import storage

client = storage.Client()


def read_file_from_gcs(file_path: str, bucket_name: str):
    bucket = client.get_bucket(bucket_name)
    blob = bucket.get_blob(file_path)
    data_string = blob.download_as_string()
    return bytes(data_string)


def upload_blob_string(
    bucket_name: str, destination_file_name: str, content_type: str, file
):
    """Uploads a file to the bucket."""

    bucket = client.bucket(bucket_name)
    blob = bucket.blob(destination_file_name)
    blob.upload_from_string(file, content_type=content_type)

    print("Uploaded to {}.".format(destination_file_name))
    gcs_uri = "gs://" + bucket_name + "/" + destination_file_name
    return gcs_uri
