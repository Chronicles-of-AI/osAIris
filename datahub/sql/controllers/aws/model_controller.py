from sql.crud.model_crud import CRUDModel
from sql.crud.deployment_crud import CRUDDeployment
from sql import config, logger
from commons.external_call import APIInterface
from datetime import datetime

logging = logger(__name__)


class ModelController:
    def __init__(self):
        self.CRUDModel = CRUDModel()
        self.CRUDDeployment = CRUDDeployment()
        self.core_aws_model_config = (
            config.get("core_engine").get("aws").get("model_router")
        )

    def train_model_controller(self, request):
        """[Controller function to train a AWS Rekognition model]

        Args:
            request ([dict]): [AWS Rekognition training request]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [str]: [training status]
        """
        try:
            logging.info("executing train_model_controller function")
            uuid = str(int(datetime.now().timestamp()))
            start_training_request = request.dict(exclude_none=True)
            start_training_url = self.core_aws_model_config.get("start_training")
            response, status_code = APIInterface.post(
                route=start_training_url, data=start_training_request
            )
            if status_code == 200:
                crud_request = {
                    "model_id": response.get("project_version_arn"),
                    "dataset_id": start_training_request.get("training_data"),
                    "artifacts": start_training_request.get("output_config"),
                    "alias_name": start_training_request.get("version_name"),
                    "auto_trigger": False,
                    "UUID": uuid,
                    "status": "Running",
                    "created": datetime.now(),
                }
                self.CRUDModel.create(**crud_request)
                return {"status": "training started"}
            else:
                raise Exception({"status": "training failed"})
        except Exception as error:
            logging.error(f"Error in train_model_controller function: {error}")
            raise error

    def deploy_model_controller(self, request):
        """[Controller function to deploy a AWS Rekognition model]

        Args:
            request ([dict]): [AWS Rekognition model request]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [str]: [deployment status]
        """
        try:
            logging.info("executing deploy_model_controller function")
            uuid = str(int(datetime.now().timestamp()))
            deploy_model_request = dict(request)
            deploy_model_url = self.core_aws_model_config.get("deploy_model")
            response, status_code = APIInterface.post(
                route=deploy_model_url, data=deploy_model_request
            )
            deployment_crud_request = {
                "UUID": uuid,
                "model_id": request.project_version_arn,
                "created": datetime.now(),
                "status": response.get("status"),
            }
            if status_code == 200:
                self.CRUDDeployment.create(**deployment_crud_request)
                return {"status": "model deployed successfully"}
            else:
                raise Exception({"status": "model deployment failed"})
        except Exception as error:
            logging.error(f"Error in deploy_model_controller function: {error}")
            raise error

    def undeploy_model_controller(self, request):
        """[Controller function to un-deploy a AWS Rekognition model]

        Args:
            request ([dict]): [AWS Rekognition model request]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [str]: [un-deployment status]
        """
        try:
            logging.info("executing undeploy_model_controller function")
            undeploy_model_request = dict(request)
            deploy_model_url = self.core_aws_model_config.get("undeploy_model")
            response, status_code = APIInterface.post(
                route=deploy_model_url, data=undeploy_model_request
            )
            undeployment_crud_request = {
                "model_id": request.project_version_arn,
                "updated": datetime.now(),
                "status": response.get("status"),
            }
            if status_code == 200:
                self.CRUDDeployment.update(undeployment_crud_request)
                return {"status": "model undeployed successfully"}
            else:
                raise Exception({"status": "model undeployment failed"})
        except Exception as error:
            logging.error(f"Error in undeploy_model_controller function: {error}")
            raise error

    def delete_model_controller(self, request):
        """[Controller function to delete a AWS Rekognition model]

        Args:
            request ([dict]): [AWS Rekognition model request]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [str]: [model delete status]
        """
        try:
            logging.info("executing delete_model_controller function")
            delete_model_request = dict(request)
            delete_model_url = self.core_aws_model_config.get("delete_model")
            response, status_code = APIInterface.post(
                route=delete_model_url, data=delete_model_request
            )
            delete_model_crud_request = {
                "model_id": request.project_version_arn,
                "status": response.get("status"),
                "updated": datetime.now(),
            }
            if status_code == 200:
                self.CRUDModel.update(delete_model_crud_request)
                return {"status": "model deleted successfully"}
            else:
                raise Exception({"status": "model deletion failed"})
        except Exception as error:
            logging.error(f"Error in delete_model_controller function: {error}")
            raise error

    def get_evaluation_controller(self, project_arn, version_name):
        """[Controller function to get model evaluation for a AWS Rekognition model]

        Args:
            project_arn ([str]): [Unique identifier for the model project]
            version_name ([str]): [Unique identifier for the model version]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [str]: [model evaluation response]
        """
        try:
            logging.info("executing get_evaluation_controller function")
            get_evaluation_url = self.core_aws_model_config.get("get_model_evaluation")
            response, status_code = APIInterface.get(
                route=get_evaluation_url,
                params={"project_arn": project_arn, "version_name": version_name},
            )
            if status_code == 200:
                return response
            else:
                raise Exception({"status": "Error in getting model evaluation"})
        except Exception as error:
            logging.error(f"Error in get_evaluation_controller function: {error}")
            raise error

    def get_manifest_controller(self, project_arn, version_name):
        """[Controller function to get manifest file for an AWS Rekognition model]

        Args:
            project_arn ([str]): [Unique identifier for the model project]
            version_name ([str]): [Unique identifier for the model version]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [str]: [model manifest file information]
        """
        try:
            logging.info("executing get_manifest_controller function")
            get_manifest_url = self.core_aws_model_config.get("get_model_manifest")
            response, status_code = APIInterface.get(
                route=get_manifest_url,
                params={"project_arn": project_arn, "version_name": version_name},
            )
            if status_code == 200:
                return response
            else:
                raise Exception({"status": "Error in getting model manifest"})
        except Exception as error:
            logging.error(f"Error in get_manifest_controller function: {error}")
            raise error

    def get_predictions_controller(
        self, project_version_arn: str, s3_uri: str, confidence_threshold: int
    ):
        """[Controller function to get predictions on the deployed AWS Rekognition model]

        Args:
            project_version_arn (str): [Unique identifier for deployed model]
            s3_uri (str): [S3 URI to test on the deployed model]
            confidence_threshold (int): [Threshold value for the predicted confidence score]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [dict]: [prediction results]
        """
        try:
            logging.info("executing get_predictions_controller function")
            get_predictions_url = self.core_aws_model_config.get("get_predictions")
            response, status_code = APIInterface.get(
                route=get_predictions_url,
                params={
                    "project_version_arn": project_version_arn,
                    "s3_uri": s3_uri,
                    "confidence_threshold": confidence_threshold,
                },
            )
            return response
        except Exception as error:
            logging.error(f"Error in get_predictions_controller function: {error}")
            raise error
