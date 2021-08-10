from fastapi import APIRouter, Depends, HTTPException, status
from sql.apis.schemas.requests.label_studio.project_request import (
    CreateProject,
    Project,
    TransformAnnotation,
)
from sql.controllers.label_studio.label_studio_controller import ProjectController
from sql.apis.schemas.responses.label_studio.project_response import (
    CreateProjectResponse,
    ProjectResponse,
    ExportAnnotationResponse,
    TransformAnnotationResponse,
)
from fastapi.security import OAuth2PasswordBearer
from commons.auth import decodeJWT

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")
project_router = APIRouter()


@project_router.post(
    "/label_studio/create_project", response_model=CreateProjectResponse
)
def create_project(
    create_project_request: CreateProject, token: str = Depends(oauth2_scheme)
):
    try:
        if decodeJWT(token=token):
            response = ProjectController().create_project_controller(
                create_project_request
            )
            # return CreateProjectResponse(**response)
            return response
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        raise error


@project_router.delete("/label_studio/delete_project", response_model=ProjectResponse)
def delete_project(
    delete_project_request: Project, token: str = Depends(oauth2_scheme)
):
    if decodeJWT(token=token):
        response = ProjectController().delete_project_controller(delete_project_request)
        return ProjectResponse(**response)
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid access token",
            headers={"WWW-Authenticate": "Bearer"},
        )


@project_router.get(
    "/label_studio/export_annotations", response_model=ExportAnnotationResponse
)
def export_annotations(
    project_id: int,
    service_provider: str,
    bucket_name: str,
    token: str = Depends(oauth2_scheme),
):
    if decodeJWT(token=token):
        response = ProjectController().export_annotations_controller(
            project_id=project_id,
            service_provider=service_provider,
            bucket_name=bucket_name,
        )
        return ExportAnnotationResponse(**response)
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid access token",
            headers={"WWW-Authenticate": "Bearer"},
        )


@project_router.post(
    "/label_studio/transform_annotations", response_model=TransformAnnotationResponse
)
def transform_annotations(
    transform_annotation_request: TransformAnnotation,
    token: str = Depends(oauth2_scheme),
):
    if decodeJWT(token=token):
        response = ProjectController().transform_annotations_controller(
            transform_annotation_request
        )
        return TransformAnnotationResponse(**response)
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid access token",
            headers={"WWW-Authenticate": "Bearer"},
        )
