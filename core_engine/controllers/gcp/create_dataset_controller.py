from utils.gcp.automl_create_dataset import (
    create_text_classification_dataset,
    create_ner_dataset,
    create_image_classification_dataset,
    create_object_detection_dataset,
)


class CreateDatasetController:
    def __init__(self):
        pass

    def create_text_classification_dataset_controller(self, request):
        return create_text_classification_dataset(
            project_id=request.project_id,
            display_name=request.display_name,
            region=request.region,
            multi_label=request.multi_label,
        )

    def create_ner_dataset_controller(self, request):
        return create_ner_dataset(
            project_id=request.project_id,
            display_name=request.display_name,
        )

    def create_image_classification_dataset_controller(self, request):
        return create_image_classification_dataset(
            project_id=request.project_id,
            display_name=request.display_name,
            region=request.region,
            multi_label=request.multi_label,
        )

    def create_object_detection_dataset_controller(self, request):
        return create_object_detection_dataset(
            project_id=request.project_id,
            display_name=request.display_name,
            region=request.region,
        )
