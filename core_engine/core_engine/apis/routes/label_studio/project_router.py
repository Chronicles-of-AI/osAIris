from fastapi import APIRouter
from core_engine.apis.schemas.requests.label_studio.project_request import (
    TransformAnnotation,
)
from core_engine.apis.schemas.response.label_studio.project_response import (
    TransformAnnotationResponse,
)
from core_engine.controllers.label_studio.label_studio_controller import (
    ProjectController,
)
from core_engine import logger

logging = logger(__name__)

project_router = APIRouter()


@project_router.post(
    "/label_studio/transform_annotations", response_model=TransformAnnotationResponse
)
def transform_annotations(transform_annotation_request: TransformAnnotation):
    """[Transform Annotations Router]

    Args:
        transform_annotation_request (TransformAnnotation): [Based on Input Schema]

    Raises:
        error: [Error]

    Returns:
        [type]: [description]
    """
    try:
        logging.info(f"Transform Annotations Router: {transform_annotation_request}")
        response = ProjectController().transform_annotations_controller(
            transform_annotation_request
        )
        return TransformAnnotationResponse(**response)
    except Exception as error:
        logging.error(f"{error=}")
        raise error
