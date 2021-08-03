from google.cloud import automl

# TODO(developer): Uncomment and set the following variables
# project_id = "YOUR_PROJECT_ID"

client = automl.AutoMlClient()


def get_dataset_description(project_id: str, region: str, dataset_id: str):
    dataset_full_id = client.dataset_path(project_id, region, dataset_id)
    dataset = client.get_dataset(name=dataset_full_id)

    dataset_dict = {
        "dataset_name": dataset.name,
        "dataset_id": dataset.name.split("/")[-1],
        "display_name": dataset.display_name,
    }
    return {"dataset_description": dataset_dict}


def list_datasets(project_id: str, region: str):
    project_location = f"projects/{project_id}/locations/{region}"
    request = automl.ListDatasetsRequest(parent=project_location, filter="")
    response = client.list_datasets(request=request)

    all_datasets = []
    for dataset in response:
        dataset_dict = {
            "dataset_name": dataset.name,
            "dataset_id": dataset.name.split("/")[-1],
            "display_name": dataset.display_name,
        }
        all_datasets.append(dataset_dict)
    return {"all_datasets": all_datasets}


def delete_datasets(project_id: str, region: str, dataset_id: str):
    dataset_full_id = client.dataset_path(project_id, region, dataset_id)
    response = client.delete_dataset(name=dataset_full_id)
    return {
        "status": "Deleting",
        "operation_id": response.operation.name,
        "project_id": project_id,
        "region": region,
        "dataset_id": dataset_id,
    }
