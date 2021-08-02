from utils.aws.rekognition_helper import (
    train_model,
    start_model,
    stop_model,
    delete_model,
    version_description,
    get_predictions,
)


class ModelController:
    def __init__(self):
        pass

    def train_model_controller(self, request):
        request = request.dict(exclude_none=True)
        response = train_model(
            project_arn=request.get("project_arn"),
            version_name=request.get("version_name"),
            output_config=request.get("output_config"),
            training_dataset=request.get("training_data"),
            testing_dataset=request.get("testing_data"),
        )
        return {"project_version_arn": response}

    def deploy_model_controller(self, request):
        response = start_model(
            project_version_arn=request.project_version_arn,
            min_inference_units=request.min_inference_units,
        )
        return {"status": response}

    def undeploy_model_controller(self, request):
        response = stop_model(project_version_arn=request.project_version_arn)
        return {"status": response}

    def delete_model_controller(self, request):
        response = delete_model(project_version_arn=request.project_version_arn)
        return {"status": response}

    def get_evaluation_controller(self, project_arn, version_name):
        response = version_description(
            project_arn=project_arn, version_name=version_name
        )
        return {
            "evaluation_result": response.get("ProjectVersionDescriptions")[0].get(
                "EvaluationResult"
            )
        }

    def get_manifest_controller(self, project_arn, version_name):
        response = version_description(
            project_arn=project_arn, version_name=version_name
        )
        return {
            "manifest_summary": response.get("ProjectVersionDescriptions")[0].get(
                "ManifestSummary"
            )
        }

    def get_predictions_controller(
        self, project_version_arn: str, s3_uri: str, confidence_threshold: int
    ):
        s3_prefix = s3_uri.split("//")[-1]
        bucket_name = s3_prefix.split("/")[0]
        file_prefix = "/".join(s3_prefix.split("/")[1:])
        return get_predictions(
            project_version_arn=project_version_arn,
            bucket=bucket_name,
            file_prefix=file_prefix,
            min_confidence=confidence_threshold,
        )
