from google.cloud import automl
from core_engine import logger

client = automl.AutoMlClient()
logging = logger(__name__)


def model_deployment(project_id: str, model_id: str, region: str):
    """[Deploy Model in AutoML GCP]

    Args:
        project_id (str): [Unique Identifier for your Project]
        model_id (str): [Unique Identifier for your Model]
        region (str): [Region]

    Raises:
        error: [Error]

    Returns:
        [dict]: [Status]
    """
    try:
        logging.info(f"Model Deployment for project id: {project_id}")
        logging.info(f"{model_id=}")
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
    except Exception as error:
        logging.error(f"{error=}")
        raise error


def model_undeployment(project_id: str, model_id: str, region: str):
    """[Un-Deploy Model in AutoML GCP]

    Args:
        project_id (str): [Unique Identifier for your Project]
        model_id (str): [Unique Identifier for your Model]
        region (str): [Region]

    Raises:
        error: [Error]

    Returns:
        [dict]: [Status]
    """
    try:
        logging.info(f"Model Un-Deployment for project id: {project_id}")
        logging.info(f"{model_id=}")
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
    except Exception as error:
        logging.error(f"{error=}")
        raise error


def get_model_description(project_id: str, model_id: str, region: str):
    """[Model Description in AutoML GCP]

    Args:
        project_id (str): [Unique Identifier for your Project]
        model_id (str): [Unique Identifier for your Model]
        region (str): [Region]

    Raises:
        error: [Error]

    Returns:
        [dict]: [Status]
    """
    try:
        logging.info(f"Model Description for project id: {project_id}")
        logging.info(f"{model_id=}")
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
    except Exception as error:
        logging.error(f"{error=}")
        raise error


def delete_model(project_id: str, model_id: str, region: str):
    """[Delete Model in AutoML GCP]

    Args:
        project_id (str): [Unique Identifier for your Project]
        model_id (str): [Unique Identifier for your Model]
        region (str): [Region]

    Raises:
        error: [Error]

    Returns:
        [dict]: [Status]
    """
    try:
        logging.info(f"Delete Model for project id: {project_id}")
        logging.info(f"{model_id=}")
        model_full_id = client.model_path(project_id, region, model_id)
        response = client.delete_model(name=model_full_id)
        return {
            "model_id": model_id,
            "operation_id": response.operation.name,
            "status": "Model Deleting",
            "project_id": project_id,
            "region": region,
        }
    except Exception as error:
        logging.error(f"{error=}")
        raise error


def model_evaluation_helper(iterator):
    metrics = {}
    for metric in iterator:
        if metric.confidence_threshold >= 0.9:
            recall = metric.recall
            precision = metric.precision
            f1Score = metric.f1Score
            metrics.update(
                {
                    "recall": recall,
                    "precision": precision,
                    "f1_score": f1Score,
                }
            )
            break
    return metrics


def get_model_evaluation(project_id: str, model_id: str, region: str):
    """[Model Evaluation in AutoML GCP]

    Args:
        project_id (str): [Unique Identifier for your Project]
        model_id (str): [Unique Identifier for your Model]
        region (str): [Region]

    Raises:
        error: [Error]

    Returns:
        [dict]: [Status]
    """
    try:
        logging.info(f"Evaluate Model for project id: {project_id}")
        logging.info(f"{model_id=}")
        model_full_id = client.model_path(project_id, region, model_id)
        for evaluation in client.list_model_evaluations(parent=model_full_id):
            response = client.get_model_evaluation(name=evaluation.name)
            if response.display_name == "":
                if response.classification_evaluation_metrics:
                    metrics = model_evaluation_helper(
                        iterator=response.classification_evaluation_metrics.confidence_metrics_entry
                    )
                elif response.image_object_detection_evaluation_metrics:
                    metrics = model_evaluation_helper(
                        iterator=response.image_object_detection_evaluation_metrics.bounding_box_metrics_entries
                    )
                elif response.text_extraction_evaluation_metrics:
                    metrics = model_evaluation_helper(
                        iterator=response.text_extraction_evaluation_metrics.confidence_metrics_entries
                    )
                else:
                    metrics = {"recall": 0.0, "precision": 0.0, "f1_score": 0.0}
                break
        return {
            "model_id": model_id,
            "metrics": metrics,
            "project_id": project_id,
            "region": region,
        }
    except Exception as error:
        logging.error(f"{error=}")
        raise error
