from google.cloud import automl


def evaluate_model(
    project_id: str, region: str, model_id: str, evlauation_filter: str = ""
):
    client = automl.AutoMlClient()
    model_full_id = client.model_path(project_id, region, model_id)
    return client.list_model_evaluations(parent=model_full_id, filter=evlauation_filter)
