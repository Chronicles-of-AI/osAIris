from typing import List
from pydantic import BaseModel


class CreateProject(BaseModel):
    title: str
    description: str
    show_instruction: bool = False
    show_skip_button: bool = True
    enable_empty_annotation: bool = True
    show_annotation_history: bool = False
    organization: int = 1
    color: str = "#FFFFFF"
    maximum_annotations: int = 1
    is_published: bool = False
    is_draft: bool = False
    sampling: str = "Sequential sampling"
    show_ground_truth_first: bool = True
    show_overlap_first: bool = True
    overlap_cohort_percentage: int = 100


class Project(BaseModel):
    project_id: int


class TransformAnnotation(BaseModel):
    input_data_uri: str
    output_data_bucket_name: str
    output_data_file_prefix: str = None
    service_provider: str
