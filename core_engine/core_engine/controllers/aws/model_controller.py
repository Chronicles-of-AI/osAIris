from core_engine.utils.aws.rekognition_helper import (
    train_model,
    start_model,
    stop_model,
    delete_model,
    version_description,
    get_predictions,
)
from core_engine import logger

logging = logger(__name__)


class ModelController:
    def __init__(self):
        pass

    def train_model_controller(self, request):
        """[Train a Model in AWS]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [description]
        """
        try:
            logging.info(f"Train Model Controller: {request}")
            request = request.dict(exclude_none=True)
            response = train_model(
                project_arn=request.get("project_arn"),
                version_name=request.get("version_name"),
                output_config=request.get("output_config"),
                training_dataset=request.get("training_data"),
                testing_dataset=request.get("testing_data"),
            )
            return {"project_version_arn": response}
        except Exception as error:
            logging.error(f"{error=}")
            raise error

    def deploy_model_controller(self, request):
        """[Deploy a Model in AWS]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [description]
        """
        try:
            logging.info(f"Deploy Model Controller: {request}")
            response = start_model(
                project_version_arn=request.project_version_arn,
                min_inference_units=request.min_inference_units,
            )
            return {"status": response}
        except Exception as error:
            logging.error(f"{error=}")
            raise error

    def undeploy_model_controller(self, request):
        """[Un-Deploy a Model in AWS]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [description]
        """
        try:
            logging.info(f"Undeploy Model Controller: {request}")
            response = stop_model(project_version_arn=request.project_version_arn)
            return {"status": response}
        except Exception as error:
            logging.error(f"{error=}")
            raise error

    def delete_model_controller(self, request):
        """[Delete a Model in AWS]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [description]
        """
        try:
            logging.info(f"Delete Model Controller: {request}")
            response = delete_model(project_version_arn=request.project_version_arn)
            return {"status": response}
        except Exception as error:
            logging.error(f"{error=}")
            raise error

    def get_evaluation_controller(self, project_arn, version_name):
        """[Evluate a Model in AWS]

        Args:
            project_arn ([type]): [Unique Identifier for a project in AWS]
            version_name ([type]): [Version Name for AWS Console]

        Raises:
            error: [Error]

        Returns:
            [type]: [description]
        """
        try:
            logging.info(f"Evaluate Model Controller: {project_arn}")
            response = version_description(
                project_arn=project_arn, version_name=version_name
            )
            return {
                "evaluation_result": response.get("ProjectVersionDescriptions")[0].get(
                    "EvaluationResult"
                )
            }
        except Exception as error:
            logging.error(f"{error=}")
            raise error

    def get_manifest_controller(self, project_arn, version_name):
        """[Get Manifest of a Model in AWS]

        Args:
            project_arn ([type]): [Unique Identifier for a project in AWS]
            version_name ([type]): [Version Name for AWS Console]

        Raises:
            error: [Error]

        Returns:
            [type]: [Manifest File paths]
        """
        try:
            logging.info(f"Get Manifest Model Controller: {project_arn}")
            response = version_description(
                project_arn=project_arn, version_name=version_name
            )
            return {
                "manifest_Train a Model in AWS": response.get(
                    "ProjectVersionDescriptions"
                )[0].get("ManifestTrain a Model in AWS")
            }
        except Exception as error:
            logging.error(f"{error=}")
            raise error

    def get_predictions_controller(
        self, project_version_arn: str, s3_uri: str, confidence_threshold: int
    ):
        """[Get prediction from a Model in AWS]

        Args:
            project_version_arn (str): [Unique Identifier of a Project Version]
            s3_uri (str): [Path of Input Data]
            confidence_threshold (int): [Confidence Threshold]

        Raises:
            error: [Error]

        Returns:
            [type]: [predictions]
        """
        try:
            logging.info(f"Get Model Prediction Controller: {project_version_arn}")
            s3_prefix = s3_uri.split("//")[-1]
            bucket_name = s3_prefix.split("/")[0]
            file_prefix = "/".join(s3_prefix.split("/")[1:])
            return get_predictions(
                project_version_arn=project_version_arn,
                bucket=bucket_name,
                file_prefix=file_prefix,
                min_confidence=confidence_threshold,
            )
        except Exception as error:
            logging.error(f"{error=}")
            raise error
