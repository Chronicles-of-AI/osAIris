from commons.external_call import APIInterface
from sql import config, logger
from sql.crud.model_crud import CRUDModel
from sql.crud.deployment_crud import CRUDDeployment
from sql.crud.project_flow_crud import CRUDProjectFlow
from datetime import datetime

logging = logger(__name__)


class ComprehendController:
    def __init__(self):
        self.CRUDModel = CRUDModel()
        self.CRUDDeployment = CRUDDeployment()
        self.CRUDProjectFlow = CRUDProjectFlow()
        self.core_aws_comprehend_config = (
            config.get("core_engine").get("aws").get("comprehend_router")
        )

    def create_document_classifier_controller(self, request):
        """[Controller function to create a new document classifier using AWS Comprehend]

        Args:
            request ([dict]): [Create document classifier request]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [str]: [document_classifier_arn]
            [str]: [status]
        """
        try:
            logging.info("executing create_document_classifier_controller function")
            uuid = str(int(datetime.now().timestamp()))
            create_document_classifier_request = request.dict(exclude_none=True)
            create_document_classifier_url = self.core_aws_comprehend_config.get(
                "create_document_classifier"
            )
            response, status_code = APIInterface.post(
                route=create_document_classifier_url,
                data=create_document_classifier_request,
            )
            if status_code == 200:
                crud_request = {
                    "model_id": response.get("document_classifier_arn"),
                    "dataset_id": create_document_classifier_request.get(
                        "InputDataConfig"
                    ),
                    "artifacts": create_document_classifier_request.get(
                        "OutputDataConfig"
                    ),
                    "alias_name": create_document_classifier_request.get(
                        "DocumentClassifierName"
                    ),
                    "auto_trigger": False,
                    "UUID": uuid,
                    "status": "Running",
                    "created": datetime.now(),
                }
                self.CRUDModel.create(**crud_request)
                project_flow_crud_request = {
                    "pipeline_id": create_document_classifier_request.get(
                        "pipeline_id"
                    ),
                    "updated_at": datetime.now(),
                    "functional_stage_id": response.get("document_classifier_arn"),
                    "current_stage": "TRAINING",
                }
                self.CRUDProjectFlow.update(**project_flow_crud_request)
                return {
                    "document_classifier_arn": response.get("document_classifier_arn"),
                    "status": "training started",
                }
            else:
                raise Exception({"status": "training failed"})
        except Exception as error:
            logging.error(
                f"Error in create_document_classifier_controller function: {error}"
            )
            raise error

    def delete_document_classifier_controller(self, request):
        """[Controller function to delete a document classifier using AWS Comprehend]

        Args:
            request ([dict]): [Delete document classifier request]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [str]: [status]
        """
        try:
            logging.info("executing delete_document_classifier_controller function")
            delete_document_classifier_request = request.dict(exclude_none=True)
            delete_document_classifier_url = self.core_aws_comprehend_config.get(
                "delete_document_classifier"
            )
            response, status_code = APIInterface.post(
                route=delete_document_classifier_url,
                data=delete_document_classifier_request,
            )
            if status_code == 200:
                crud_request = {
                    "model_id": request.DocumentClassifierArn,
                    "status": "Deleted",
                    "updated": datetime.now(),
                }
                self.CRUDModel.update(crud_request)
                return {"status": "classifier deleted"}
            else:
                raise Exception({"status": "deletion failed"})
        except Exception as error:
            logging.error(
                f"Error in delete_document_classifier_controller function: {error}"
            )
            raise error

    def describe_document_classifier_controller(self, request):
        """[Controller function to describe a document classifier using AWS Comprehend]

        Args:
            request ([dict]): [Describe document classifier request]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [dict]: [Document Classifier description returned from core engine]
        """
        try:
            logging.info("executing describe_document_classifier_controller function")
            describe_document_classifier_request = request.dict(exclude_none=True)
            describe_document_classifier_url = self.core_aws_comprehend_config.get(
                "describe_document_classifier"
            )
            response, status_code = APIInterface.post(
                route=describe_document_classifier_url,
                data=describe_document_classifier_request,
            )
            return response
        except Exception as error:
            logging.error(
                f"Error in describe_document_classifier_controller function: {error}"
            )
            raise error

    def stop_training_document_classifier_controller(self, request):
        """[Controller function to stop a training job on AWS Comprehend]

        Args:
            request ([dict]): [Stop training request]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [str]: [Status of training job]
        """
        try:
            logging.info(
                "executing stop_training_document_classifier_controller function"
            )
            stop_training_document_classifier_request = request.dict(exclude_none=True)
            stop_training_document_classifier_url = self.core_aws_comprehend_config.get(
                "stop_training_document_classifier"
            )
            response, status_code = APIInterface.post(
                route=stop_training_document_classifier_url,
                data=stop_training_document_classifier_request,
            )
            if status_code == 200:
                crud_request = {
                    "model_id": request.DocumentClassifierArn,
                    "status": "Stopped",
                    "updated": datetime.now(),
                }
                self.CRUDModel.update(crud_request)
                project_flow_crud_request = {
                    "pipeline_id": stop_training_document_classifier_request.get(
                        "pipeline_id"
                    ),
                    "updated_at": datetime.now(),
                    "functional_stage_id": request.DocumentClassifierArn,
                    "current_stage": "TRAINING_STOPPED",
                }
                self.CRUDProjectFlow.update(**project_flow_crud_request)
                return {"status": "training stopped"}
            else:
                raise Exception({"status": "training failed"})
        except Exception as error:
            logging.error(
                f"Error in stop_training_document_classifier_controller function: {error}"
            )
            raise error

    def list_document_classifier_controller(self):
        """[Controller function to list all the document classifiers on AWS Comprehend]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [dict]: [List of all the document classifier on AWS Comprehend]
        """
        try:
            logging.info("executing list_document_classifier_controller function")
            list_document_classifier_url = self.core_aws_comprehend_config.get(
                "list_document_classifier"
            )
            response, status_code = APIInterface.get(
                route=list_document_classifier_url,
            )
            return response
        except Exception as error:
            logging.error(
                f"Error in list_document_classifier_controller function: {error}"
            )
            raise error

    def deploy_document_classifier_controller(self, request):
        """[Controller function to deploy a document classifier]

        Args:
            request ([dict]): [Deploy document classifier request]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [dict]: [Details of the deployed document classifier model]
        """
        try:
            logging.info("executing deploy_document_classifier_controller function")
            uuid = str(int(datetime.now().timestamp()))
            deploy_document_classifier_request = request.dict(exclude_none=True)
            deploy_document_classifier_url = self.core_aws_comprehend_config.get(
                "deploy_document_classifier"
            )
            response, status_code = APIInterface.post(
                route=deploy_document_classifier_url,
                data=deploy_document_classifier_request,
            )
            if status_code == 200:
                deployment_crud_request = {
                    "UUID": uuid,
                    "model_id": request.model_arn,
                    "deployment_endpoint": response.get("endpoint_arn"),
                    "created": datetime.now(),
                    "status": "Deployed",
                }
                self.CRUDDeployment.create(**deployment_crud_request)
                project_flow_crud_request = {
                    "pipeline_id": deploy_document_classifier_request.get(
                        "pipeline_id"
                    ),
                    "updated_at": datetime.now(),
                    "model_id": request.model_arn,
                    "functional_stage_id": request.model_arn,
                    "current_stage": "MODEL_DEPLOYED",
                }
                self.CRUDProjectFlow.update(**project_flow_crud_request)
                response.update({"status": "model deployed successfully"})
                return response
            else:
                raise Exception({"status": "model deployment failed"})
        except Exception as error:
            logging.error(
                f"Error in deploy_document_classifier_controller function: {error}"
            )
            raise error

    def undeploy_document_classifier_controller(self, request):
        """[Controller function to undeploy a document classifier]

        Args:
            request ([dict]): [Un-Deploy document classifier request]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [dict]: [Details of the undeployed document classifier model]
        """
        try:
            logging.info("executing undeploy_document_classifier_controller function")
            undeploy_document_classifier_request = request.dict(exclude_none=True)
            undeploy_document_classifier_url = self.core_aws_comprehend_config.get(
                "undeploy_document_classifier"
            )
            response, status_code = APIInterface.post(
                route=undeploy_document_classifier_url,
                data=undeploy_document_classifier_request,
            )
            if status_code == 200:
                undeployment_crud_request = {
                    "deployment_endpoint": request.endpoint_arn,
                    "updated": datetime.now(),
                    "status": "UnDeployed",
                }
                self.CRUDDeployment.update_by_endpoint(
                    deployment_request=undeployment_crud_request
                )
                project_flow_crud_request = {
                    "pipeline_id": undeploy_document_classifier_request.get(
                        "pipeline_id"
                    ),
                    "updated_at": datetime.now(),
                    "current_stage": "MODEL_UNDEPLOYED",
                }
                self.CRUDProjectFlow.update(**project_flow_crud_request)
                return {"status": "model undeployed successfully"}
            else:
                raise Exception({"status": "model undeployment failed"})
        except Exception as error:
            logging.error(
                f"Error in undeploy_document_classifier_controller function: {error}"
            )
            raise error

    def get_predictions_controller(self, endpoint_arn: str, text: str):
        """[Controller function to get predictions from trained document classifier]

        Args:
            endpoint_arn (str): [endpoint of the trained document classifier]
            text (str): [text to be classified]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [dict]: [predictions from the trained model]
        """
        try:
            logging.info("executing get_predictions_controller function")
            get_predictions_url = self.core_aws_comprehend_config.get("get_predictions")
            response, status_code = APIInterface.get(
                route=get_predictions_url,
                params={"endpoint_arn": endpoint_arn, "text": text},
            )
            return response
        except Exception as error:
            logging.error(f"Error in get_predictions_controller function: {error}")
            raise error
