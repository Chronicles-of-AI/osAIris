from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from sql.apis.routes.aws.project_router import project_router
from sql.apis.routes.aws.model_router import model_router
from sql.apis.routes.aws.sagemaker_router import sagemaker_router
from sql.apis.routes.aws.comprehend_router import comprehend_router
from sql.apis.routes.label_studio.project_router import (
    project_router as label_studio_project_router,
)
from sql.apis.routes.label_studio.storage_router import storage_router
from sql.apis.routes.gcp.create_dataset_router import create_dataset_router
from sql.apis.routes.gcp.import_dataset_router import import_dataset_router
from sql.apis.routes.gcp.train_model_router import train_model_router
from sql.apis.routes.gcp.manage_model_router import manage_model_router
from sql.apis.routes.gcp.model_predictions_router import get_predictions_router
from sql.apis.routes.gcp.manage_dataset_router import manage_dataset_router
from sql.apis.routes.gcp.operations_router import operations_router
from sql.apis.routes.user_management.user_router import user_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="osAIris",
    version="0.2 - Beta",
    description="MLOps made simple",
    redoc_url="/documentation",
)
origins = [
    "http://localhost:8081",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(user_router, tags=["authentication"])
app.include_router(project_router, tags=["aws rekognition"])
app.include_router(model_router, tags=["aws rekognition"])
app.include_router(sagemaker_router, tags=["aws sagemaker"])
app.include_router(comprehend_router, tags=["aws comprehend"])
app.include_router(label_studio_project_router, tags=["label studio"])
app.include_router(storage_router, tags=["label studio"])
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


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="osAIris",
        version="0.2 - Beta",
        description="MLOps made simple",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://github.com/Chronicles-of-AI/osAIris/blob/ce6e33adf3bc0a9ca6e2e1cc16a49c16a983a798/docs/logo.jpeg?raw=true"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi
