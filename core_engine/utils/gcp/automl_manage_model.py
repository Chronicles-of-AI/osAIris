from google.cloud import automl

client = automl.AutoMlClient()


def model_deployment(project_id: str, model_id: str, region: str):
    # Get the full path of the model.
    model_full_id = client.model_path(project_id, region, model_id)
    response = client.deploy_model(name=model_full_id)
    return {
        "model_id": model_id,
        "operation_id": response.operation.name,
        "status": "Deployment Started",
        "project_id": project_id,
        "region": region,
    }


def model_undeployment(project_id: str, model_id: str, region: str):
    # Get the full path of the model.
    model_full_id = client.model_path(project_id, region, model_id)
    response = client.undeploy_model(name=model_full_id)
    return {
        "model_id": model_id,
        "operation_id": response.operation.name,
        "status": "Undeployment Started",
        "project_id": project_id,
        "region": region,
    }


def get_model_description(project_id: str, model_id: str, region: str):
    model_full_id = client.model_path(project_id, region, model_id)
    model = client.get_model(name=model_full_id)

    # Retrieve deployment state.
    if model.deployment_state == automl.Model.DeploymentState.DEPLOYED:
        deployment_state = "deployed"
    else:
        deployment_state = "undeployed"

    # Display the model information.
    model_data = {
        "model_name": model.name,
        "model_id": model.name.split("/")[-1],
        "model_display_name": model.display_name,
        "model_deplyment_state": deployment_state,
    }
    return {"model_description": model_data}


def delete_model(project_id: str, model_id: str, region: str):
    model_full_id = client.model_path(project_id, region, model_id)
    response = client.delete_model(name=model_full_id)
    return {
        "model_id": model_id,
        "operation_id": response.operation.name,
        "status": "Model Deleting",
        "project_id": project_id,
        "region": region,
    }
