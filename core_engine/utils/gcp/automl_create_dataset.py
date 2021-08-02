from google.cloud import automl

client = automl.AutoMlClient()


def create_dataset(dataset, project_location: str):
    response = client.create_dataset(parent=project_location, dataset=dataset)

    created_dataset = response.result()

    # Display the dataset information
    print("Dataset name: {}".format(created_dataset.name))
    print("Dataset id: {}".format(created_dataset.name.split("/")[-1]))

    dataset_info = {
        "dataset_name": created_dataset.name,
        "dataset_id": created_dataset.name.split("/")[-1],
    }
    return dataset_info


def create_text_classification_dataset(
    project_id: str, display_name: str, region: str, multi_label: bool = False
):
    project_location = f"projects/{project_id}/locations/{region}"
    # us-central1
    if not multi_label:
        metadata = automl.TextClassificationDatasetMetadata(
            classification_type=automl.ClassificationType.MULTICLASS
        )
    else:
        metadata = automl.TextClassificationDatasetMetadata(
            classification_type=automl.ClassificationType.MULTILABEL
        )
    dataset = automl.Dataset(
        display_name=display_name,
        text_classification_dataset_metadata=metadata,
    )
    dataset_response = create_dataset(
        dataset=dataset, project_location=project_location
    )
    return dataset_response


def create_ner_dataset(project_id: str, display_name: str, region: str):
    project_location = f"projects/{project_id}/locations/{region}"
    metadata = automl.TextExtractionDatasetMetadata()
    dataset = automl.Dataset(
        display_name=display_name, text_extraction_dataset_metadata=metadata
    )
    dataset_response = create_dataset(
        dataset=dataset, project_location=project_location
    )
    return dataset_response


def create_image_classification_dataset(
    project_id: str, display_name: str, region: str, multi_label: bool = False
):
    project_location = f"projects/{project_id}/locations/{region}"
    if not multi_label:
        metadata = automl.ImageClassificationDatasetMetadata(
            classification_type=automl.ClassificationType.MULTICLASS
        )
    else:
        metadata = automl.ImageClassificationDatasetMetadata(
            classification_type=automl.ClassificationType.MULTILABEL
        )
    dataset = automl.Dataset(
        display_name=display_name,
        image_classification_dataset_metadata=metadata,
    )
    dataset_response = create_dataset(
        dataset=dataset, project_location=project_location
    )
    return dataset_response


def create_object_detection_dataset(project_id: str, display_name: str, region: str):
    project_location = f"projects/{project_id}/locations/{region}"
    metadata = automl.ImageObjectDetectionDatasetMetadata()
    dataset = automl.Dataset(
        display_name=display_name, image_object_detection_dataset_metadata=metadata
    )
    dataset_response = create_dataset(
        dataset=dataset, project_location=project_location
    )
    return dataset_response
