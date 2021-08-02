from google.cloud import automl

client = automl.AutoMlClient()

# Sample variables for reference
# dataset_id = "datasetId=TCN2488828682110500864"
# project_id = "us-gcp-ame-con-be2-npd-1"


def list_models(project_id: str, region: str, dataset_id: str = None):
    """List models."""
    project_location = f"projects/{project_id}/locations/{region}"
    request = automl.ListModelsRequest(
        parent=project_location, filter=f"datasetId={dataset_id}"
    )
    response = client.list_models(request=request)

    all_models = []
    for model in response:
        # Display the model information.
        if model.deployment_state == automl.Model.DeploymentState.DEPLOYED:
            deployment_state = "deployed"
        else:
            deployment_state = "undeployed"

        model_meta_data = {
            "model_id": model.name.split("/")[-1],
            "model_display_name": model.display_name,
            "model_deployment_state": deployment_state,
            "model_name": model.name,
        }
        all_models.append(model_meta_data)
    return {"models": all_models}
