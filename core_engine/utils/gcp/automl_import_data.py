from google.cloud import automl

client = automl.AutoMlClient()

# Sample variable values
# project_id = "us-gcp-ame-con-be2-npd-1"
# dataset_id = "TCN8344915572575698944"
# path = "gs://test_bucket_automl_nl/decision_caller_api_maps.csv"


def import_training_data(project_id: str, dataset_id: str, gcs_path: str, region: str):
    dataset_full_id = client.dataset_path(project_id, region, dataset_id)
    input_uris = gcs_path.split(",")
    gcs_source = automl.GcsSource(input_uris=input_uris)
    input_config = automl.InputConfig(gcs_source=gcs_source)
    response = client.import_data(name=dataset_full_id, input_config=input_config)
    return {
        "operation_id": response.operation.name,
        "project_id": project_id,
        "region": region,
        "status": "Import In-Progress",
        "dataset_id": dataset_id,
    }
