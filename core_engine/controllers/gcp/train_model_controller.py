from utils.gcp.automl_train import (
    train_text_classification_model,
    train_ner_model,
    train_image_classification_model,
    train_image_classification_edge_model,
    train_object_detection_model,
    train_object_detection_edge_model,
)


class TrainModelController:
    def __init__(self):
        pass

    def train_text_classification_model_controller(self, request):
        return train_text_classification_model(
            project_id=request.project_id,
            dataset_id=request.dataset_id,
            model_display_name=request.model_display_name,
            region=request.region,
        )

    def train_ner_model_controller(self, request):
        return train_ner_model(
            project_id=request.project_id,
            dataset_id=request.dataset_id,
            model_display_name=request.model_display_name,
            region=request.region,
        )

    def train_image_classification_model_controller(self, request):
        return train_image_classification_model(
            project_id=request.project_id,
            dataset_id=request.dataset_id,
            model_display_name=request.model_display_name,
            region=request.region,
        )

    def train_image_classification_edge_model_controller(self, request):
        return train_image_classification_edge_model(
            project_id=request.project_id,
            dataset_id=request.dataset_id,
            model_display_name=request.model_display_name,
            region=request.region,
            model_type=request.model_type,
        )

    def train_object_detection_model_controller(self, request):
        return train_object_detection_model(
            project_id=request.project_id,
            dataset_id=request.dataset_id,
            model_display_name=request.model_display_name,
            region=request.region,
        )

    def train_object_detection_edge_model_controller(self, request):
        return train_object_detection_edge_model(
            project_id=request.project_id,
            dataset_id=request.dataset_id,
            model_display_name=request.model_display_name,
            region=request.region,
            model_type=request.model_type,
        )
