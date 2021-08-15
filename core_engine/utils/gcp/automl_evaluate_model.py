from google.cloud import automl
from core_engine import logger

logging = logger(__name__)


def evaluate_model(
    project_id: str, region: str, model_id: str, evlauation_filter: str = ""
):
    """[Evalaute Model Summary]

    Args:
        project_id (str): [Unique Identifier for your Project]
        region (str): [Region]
        model_id (str): [Unique Identifier for your Model]
        evlauation_filter (str, optional): [description]. Defaults to "".

    Raises:
        error: [Error]

    Returns:
        [type]: [description]
    """
    try:
        logging.info(f"Evaluate Model: {project_id}")
        logging.info(f"{model_id=}")
        client = automl.AutoMlClient()
        model_full_id = client.model_path(project_id, region, model_id)
        return client.list_model_evaluations(
            parent=model_full_id, filter=evlauation_filter
        )
    except Exception as error:
        logging.error(f"{error=}")
        raise error
