from commons.external_call import APIInterface
from sql import config, logger
from sql.crud.model_crud import CRUDModel
from sql.crud.deployment_crud import CRUDDeployment
from sql.crud.project_flow_crud import CRUDProjectFlow
from sql.crud.model_monitoring_crud import CRUDModelMonitoring
from datetime import datetime

logging = logger(__name__)


class ComprehendController:
    def __init__(self):
        self.CRUDModel = CRUDModel()
        self.CRUDDeployment = CRUDDeployment()
        self.CRUDProjectFlow = CRUDProjectFlow()
        self.CRUDModelMonitoring = CRUDModelMonitoring()
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
                    "pipeline_id": create_document_classifier_request.get(
                        "pipeline_id"
                    ),
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

    def create_entity_recognizer_controller(self, request):
        """[Controller function to create a new entity recognizer using AWS Comprehend]

        Args:
            request ([dict]): [Create entity recognizer request]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [str]: [entity_recognizer_arn]
            [str]: [status]
        """
        try:
            logging.info("executing create_entity_recognizer_controller function")
            uuid = str(int(datetime.now().timestamp()))
            create_entity_recognizer_request = request.dict(exclude_none=True)
            create_entity_recognizer_url = self.core_aws_comprehend_config.get(
                "create_entity_recognizer"
            )
            response, status_code = APIInterface.post(
                route=create_entity_recognizer_url,
                data=create_entity_recognizer_request,
            )
            if status_code == 200:
                crud_request = {
                    "pipeline_id": create_entity_recognizer_request.get("pipeline_id"),
                    "model_id": response.get("entity_recognizer_arn"),
                    "dataset_id": create_entity_recognizer_request.get(
                        "InputDataConfig"
                    ),
                    "artifacts": create_entity_recognizer_request.get(
                        "OutputDataConfig"
                    ),
                    "alias_name": create_entity_recognizer_request.get(
                        "RecognizerName"
                    ),
                    "auto_trigger": False,
                    "UUID": uuid,
                    "status": "Running",
                    "created": datetime.now(),
                }
                self.CRUDModel.create(**crud_request)
                project_flow_crud_request = {
                    "pipeline_id": create_entity_recognizer_request.get("pipeline_id"),
                    "updated_at": datetime.now(),
                    "functional_stage_id": response.get("entity_recognizer_arn"),
                    "current_stage": "TRAINING",
                }
                self.CRUDProjectFlow.update(**project_flow_crud_request)
                return {
                    "entity_recognizer_arn": response.get("entity_recognizer_arn"),
                    "status": "training started",
                }
            else:
                raise Exception({"status": "training failed"})
        except Exception as error:
            logging.error(
                f"Error in create_entity_recognizer_controller function: {error}"
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

    def delete_entity_recognizer_controller(self, request):
        """[Controller function to delete a entity_recognizer using AWS Comprehend]

        Args:
            request ([dict]): [Delete entity_recognizer request]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [str]: [status]
        """
        try:
            logging.info("executing delete_entity_recognizer_controller function")
            delete_entity_recognizer_request = request.dict(exclude_none=True)
            delete_entity_recognizer_url = self.core_aws_comprehend_config.get(
                "delete_entity_recognizer"
            )
            response, status_code = APIInterface.post(
                route=delete_entity_recognizer_url,
                data=delete_entity_recognizer_request,
            )
            if status_code == 200:
                crud_request = {
                    "model_id": request.DocumentClassifierArn,
                    "status": "Deleted",
                    "updated": datetime.now(),
                }
                self.CRUDModel.update(crud_request)
                return {"status": "recognizer deleted"}
            else:
                raise Exception({"status": "deletion failed"})
        except Exception as error:
            logging.error(
                f"Error in delete_entity_recognizer_controller function: {error}"
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
            crud_request = {
                "model_id": request.DocumentClassifierArn,
                "status": response.get("Status"),
                "updated": datetime.now(),
            }
            self.CRUDModel.update(crud_request)
            evaluation_metrics = (
                response.get("DocumentClassifierProperties")
                .get("ClassifierMetadata")
                .get("EvaluationMetrics")
            )
            f1_score = evaluation_metrics.get("F1Score")
            precision = evaluation_metrics.get("Precision")
            recall = evaluation_metrics.get("Recall")
            status = response.get("DocumentClassifierProperties").get("Status")
            if status == "TRAINED":
                create_model_monitoring_request = {
                    "model_uri": request.DocumentClassifierArn,
                    "model_f1_score": f1_score,
                    "model_recall": recall,
                    "model_precision": precision,
                    "model_drift_threshold": "0.8",
                    "created_at": datetime.now(),
                    "updated_at": datetime.now(),
                }
                if (
                    len(
                        self.CRUDModelMonitoring.read(
                            model_uri=request.DocumentClassifierArn
                        )
                    )
                    == 0
                ):
                    project_flow_crud_request = {
                        "pipeline_id": request.pipeline_id,
                        "updated_at": datetime.now(),
                        "current_stage": "TRAINED",
                    }
                    self.CRUDProjectFlow.update(**project_flow_crud_request)
                    self.CRUDModelMonitoring.create(**create_model_monitoring_request)
            return response
        except Exception as error:
            logging.error(
                f"Error in describe_document_classifier_controller function: {error}"
            )
            raise error

    def describe_document_classifier_status_controller(self, request):
        """[Controller function to describe a document classifier status using AWS Comprehend]

        Args:
            request ([dict]): [Describe document classifier request]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [dict]: [Document Classifier description returned from core engine]
        """
        try:
            logging.info(
                "executing describe_document_classifier_status_controller function"
            )
            describe_document_classifier_request = request.dict(exclude_none=True)
            describe_document_classifier_url = self.core_aws_comprehend_config.get(
                "describe_document_classifier"
            )
            response, status_code = APIInterface.post(
                route=describe_document_classifier_url,
                data=describe_document_classifier_request,
            )
            document_classifier_status = response.get(
                "DocumentClassifierProperties"
            ).get("Status")
            return {"model_status": document_classifier_status}
        except Exception as error:
            logging.error(
                f"Error in describe_document_classifier_status_controller function: {error}"
            )
            raise error

    def describe_entity_recognizer_controller(self, request):
        """[Controller function to describe a entity recognizer using AWS Comprehend]

        Args:
            request ([dict]): [Describe entity recognizer request]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [dict]: [entity recognizer description returned from core engine]
        """
        try:
            logging.info("executing describe_entity_recognizer_controller function")
            describe_entity_recognizer_request = request.dict(exclude_none=True)
            describe_entity_recognizer_url = self.core_aws_comprehend_config.get(
                "describe_entity_recognizer"
            )
            response, status_code = APIInterface.post(
                route=describe_entity_recognizer_url,
                data=describe_entity_recognizer_request,
            )
            crud_request = {
                "model_id": request.EntityRecognizerArn,
                "status": response.get("Status"),
                "updated": datetime.now(),
            }
            self.CRUDModel.update(crud_request)
            evaluation_metrics = (
                response.get("EntityRecognizerProperties")
                .get("RecognizerMetadata")
                .get("EvaluationMetrics")
            )
            f1_score = evaluation_metrics.get("F1Score")
            precision = evaluation_metrics.get("Precision")
            recall = evaluation_metrics.get("Recall")
            status = response.get("EntityRecognizerProperties").get("Status")
            if status == "TRAINED":
                create_model_monitoring_request = {
                    "model_uri": request.EntityRecognizerArn,
                    "model_f1_score": f1_score,
                    "model_recall": recall,
                    "model_precision": precision,
                    "model_drift_threshold": "0.8",
                    "created_at": datetime.now(),
                    "updated_at": datetime.now(),
                }
                if (
                    len(
                        self.CRUDModelMonitoring.read(
                            model_uri=request.EntityRecognizerArn
                        )
                    )
                    == 0
                ):
                    project_flow_crud_request = {
                        "pipeline_id": request.pipeline_id,
                        "updated_at": datetime.now(),
                        "current_stage": "TRAINED",
                    }
                    self.CRUDProjectFlow.update(**project_flow_crud_request)
                    self.CRUDModelMonitoring.create(**create_model_monitoring_request)
            return response
        except Exception as error:
            logging.error(
                f"Error in describe_entity_recognizer_controller function: {error}"
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

    def stop_training_entity_recognizer_controller(self, request):
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
                "executing stop_training_entity_recognizer_controller function"
            )
            stop_training_entity_recognizer_request = request.dict(exclude_none=True)
            stop_training_entity_recognizer_url = self.core_aws_comprehend_config.get(
                "stop_training_entity_recognizer"
            )
            response, status_code = APIInterface.post(
                route=stop_training_entity_recognizer_url,
                data=stop_training_entity_recognizer_request,
            )
            if status_code == 200:
                crud_request = {
                    "model_id": request.EntityRecognizerArn,
                    "status": "Stopped",
                    "updated": datetime.now(),
                }
                self.CRUDModel.update(crud_request)
                project_flow_crud_request = {
                    "pipeline_id": stop_training_entity_recognizer_request.get(
                        "pipeline_id"
                    ),
                    "updated_at": datetime.now(),
                    "functional_stage_id": request.EntityRecognizerArn,
                    "current_stage": "TRAINING_STOPPED",
                }
                self.CRUDProjectFlow.update(**project_flow_crud_request)
                return {"status": "training stopped"}
            else:
                raise Exception({"status": "training failed"})
        except Exception as error:
            logging.error(
                f"Error in stop_training_entity_recognizer_controller function: {error}"
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

    def list_entity_recognizer_controller(self):
        """[Controller function to list all the entity recognizers on AWS Comprehend]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [dict]: [List of all the entity recognizers on AWS Comprehend]
        """
        try:
            logging.info("executing list_entity_recognizer_controller function")
            list_entity_recognizer_url = self.core_aws_comprehend_config.get(
                "list_entity_recognizer"
            )
            response, status_code = APIInterface.get(
                route=list_entity_recognizer_url,
            )
            return response
        except Exception as error:
            logging.error(
                f"Error in list_entity_recognizer_controller function: {error}"
            )
            raise error

    def deploy_model_controller(self, request):
        """[Controller function to deploy a document classifier]

        Args:
            request ([dict]): [Deploy document classifier request]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [dict]: [Details of the deployed document classifier model]
        """
        try:
            logging.info("executing deploy_model_controller function")
            uuid = str(int(datetime.now().timestamp()))
            deploy_model_request = request.dict(exclude_none=True)
            deploy_model_url = self.core_aws_comprehend_config.get("deploy_model")
            response, status_code = APIInterface.post(
                route=deploy_model_url,
                data=deploy_model_request,
            )
            if status_code == 200:
                deployment_crud_request = {
                    "pipeline_id": deploy_model_request.get("pipeline_id"),
                    "UUID": uuid,
                    "model_id": request.model_arn,
                    "deployment_endpoint": response.get("endpoint_arn"),
                    "created": datetime.now(),
                    "status": "Deployed",
                }
                self.CRUDDeployment.create(**deployment_crud_request)
                project_flow_crud_request = {
                    "pipeline_id": deploy_model_request.get("pipeline_id"),
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
            logging.error(f"Error in deploy_model_controller function: {error}")
            raise error

    def undeploy_model_controller(self, request):
        """[Controller function to undeploy a document classifier]

        Args:
            request ([dict]): [Un-Deploy document classifier request]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [dict]: [Details of the undeployed document classifier model]
        """
        try:
            logging.info("executing undeploy_model_controller function")
            undeploy_model_request = request.dict(exclude_none=True)
            undeploy_model_url = self.core_aws_comprehend_config.get("undeploy_model")
            response, status_code = APIInterface.post(
                route=undeploy_model_url,
                data=undeploy_model_request,
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
                    "pipeline_id": undeploy_model_request.get("pipeline_id"),
                    "updated_at": datetime.now(),
                    "current_stage": "MODEL_UNDEPLOYED",
                }
                self.CRUDProjectFlow.update(**project_flow_crud_request)
                return {"status": "model undeployed successfully"}
            else:
                raise Exception({"status": "model undeployment failed"})
        except Exception as error:
            logging.error(f"Error in undeploy_model_controller function: {error}")
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
