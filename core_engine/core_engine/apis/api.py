from fastapi import FastAPI
from core_engine.apis.routes.aws.project_router import project_router
from core_engine.apis.routes.aws.model_router import model_router
from core_engine.apis.routes.aws.sagemaker_router import sagemaker_router
from core_engine.apis.routes.aws.comprehend_router import comprehend_router
from core_engine.apis.routes.label_studio.project_router import (
    project_router as label_studio_project_router,
)
from core_engine.apis.routes.gcp.create_dataset_router import create_dataset_router
from core_engine.apis.routes.gcp.import_dataset_router import import_dataset_router
from core_engine.apis.routes.gcp.manage_model_router import manage_model_router
from core_engine.apis.routes.gcp.model_predictions_router import get_predictions_router
from core_engine.apis.routes.gcp.train_model_router import train_model_router
from core_engine.apis.routes.gcp.manage_dataset_router import manage_dataset_router
from core_engine.apis.routes.gcp.operations_router import operations_router


app = FastAPI()
app.include_router(project_router, tags=["aws rekognition"])
app.include_router(model_router, tags=["aws rekognition"])
app.include_router(sagemaker_router, tags=["aws sagemaker"])
app.include_router(comprehend_router, tags=["aws comprehend"])
app.include_router(label_studio_project_router, tags=["label studio"])
app.include_router(create_dataset_router, tags=["gcp automl dataset"])
app.include_router(import_dataset_router, tags=["gcp automl dataset"])
app.include_router(manage_dataset_router, tags=["gcp automl dataset"])
app.include_router(train_model_router, tags=["gcp automl model"])
app.include_router(manage_model_router, tags=["gcp automl model"])
app.include_router(get_predictions_router, tags=["gcp automl model"])
app.include_router(operations_router, tags=["gcp automl operations"])


@app.get("/")
def ping():
    """[ping func provides a health check]

    Returns:
        [dict]: [success response for health check]
    """
    return {"response": "ping to datahub successful"}
