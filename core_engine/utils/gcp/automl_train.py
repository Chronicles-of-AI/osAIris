from google.cloud import automl

# Sample variable values
# project_id = "us-gcp-ame-con-be2-npd-1"
# dataset_id = "TCN8344915572575698944"
# display_name = "decision_caller_api_model_v1"

client = automl.AutoMlClient()


def train_text_classification_model(
    project_id: str, dataset_id: str, model_display_name: str, region: str
):
    project_location = f"projects/{project_id}/locations/{region}"
    metadata = automl.TextClassificationModelMetadata()
    model = automl.Model(
        display_name=model_display_name,
        dataset_id=dataset_id,
        text_classification_model_metadata=metadata,
    )
    response = client.create_model(parent=project_location, model=model)

    return {
        "operation_id": response.operation.name,
        "dataset_id": dataset_id,
        "status": "Training Started",
        "project_id": project_id,
        "region": region,
    }


def train_ner_model(
    project_id: str, dataset_id: str, model_display_name: str, region: str
):
    # A resource that represents Google Cloud Platform location.
    project_location = f"projects/{project_id}/locations/{region}"
    # Leave model unset to use the default base model provided by Google
    metadata = automl.TextExtractionModelMetadata()
    model = automl.Model(
        display_name=model_display_name,
        dataset_id=dataset_id,
        text_extraction_model_metadata=metadata,
    )

    # Create a model with the model metadata in the region.
    response = client.create_model(parent=project_location, model=model)
    return {
        "operation_id": response.operation.name,
        "dataset_id": dataset_id,
        "status": "Training Started",
        "project_id": project_id,
        "region": region,
    }


def train_image_classification_model(
    project_id: str, dataset_id: str, model_display_name: str, region: str
):
    project_location = f"projects/{project_id}/locations/{region}"
    metadata = automl.ImageClassificationModelMetadata(
        train_budget_milli_node_hours=24000
    )
    model = automl.Model(
        display_name=model_display_name,
        dataset_id=dataset_id,
        image_classification_model_metadata=metadata,
    )

    # Create a model with the model metadata in the region.
    response = client.create_model(parent=project_location, model=model)
    return {
        "operation_id": response.operation.name,
        "dataset_id": dataset_id,
        "status": "Training Started",
        "project_id": project_id,
        "region": region,
    }


def train_image_classification_edge_model(
    project_id: str,
    dataset_id: str,
    model_display_name: str,
    region: str,
    model_type: str = "mobile-versatile-1",
):
    project_location = f"projects/{project_id}/locations/{region}"
    metadata = automl.ImageClassificationModelMetadata(
        train_budget_milli_node_hours=24000, model_type=model_type
    )
    model = automl.Model(
        display_name=model_display_name,
        dataset_id=dataset_id,
        image_classification_model_metadata=metadata,
    )

    # Create a model with the model metadata in the region.
    response = client.create_model(parent=project_location, model=model)
    return {
        "operation_id": response.operation.name,
        "dataset_id": dataset_id,
        "status": "Training Started",
        "project_id": project_id,
        "region": region,
    }


def train_object_detection_model(
    project_id: str, dataset_id: str, model_display_name: str, region: str
):
    project_location = f"projects/{project_id}/locations/{region}"
    metadata = automl.ImageClassificationModelMetadata(
        train_budget_milli_node_hours=24000
    )
    model = automl.Model(
        display_name=model_display_name,
        dataset_id=dataset_id,
        image_classification_model_metadata=metadata,
    )

    # Create a model with the model metadata in the region.
    response = client.create_model(parent=project_location, model=model)
    return {
        "operation_id": response.operation.name,
        "dataset_id": dataset_id,
        "status": "Training Started",
        "project_id": project_id,
        "region": region,
    }


def train_object_detection_edge_model(
    project_id: str,
    dataset_id: str,
    model_display_name: str,
    region: str,
    model_type: str = "mobile-versatile-1",
):
    project_location = f"projects/{project_id}/locations/{region}"
    metadata = automl.ImageClassificationModelMetadata(
        train_budget_milli_node_hours=24000, model_type=model_type
    )
    model = automl.Model(
        display_name=model_display_name,
        dataset_id=dataset_id,
        image_classification_model_metadata=metadata,
    )

    # Create a model with the model metadata in the region.
    response = client.create_model(parent=project_location, model=model)
    return {
        "operation_id": response.operation.name,
        "dataset_id": dataset_id,
        "status": "Training Started",
        "project_id": project_id,
        "region": region,
    }
