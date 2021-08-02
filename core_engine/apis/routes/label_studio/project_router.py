from fastapi import APIRouter
from apis.schemas.requests.label_studio.project_request import (
    TransformAnnotation,
)
from apis.schemas.response.label_studio.project_response import (
    TransformAnnotationResponse,
)
from controllers.label_studio.label_studio_controller import ProjectController

project_router = APIRouter()


@project_router.post(
    "/label_studio/transform_annotations", response_model=TransformAnnotationResponse
)
def transform_annotations(transform_annotation_request: TransformAnnotation):
    response = ProjectController().transform_annotations_controller(
        transform_annotation_request
    )
    return TransformAnnotationResponse(**response)
