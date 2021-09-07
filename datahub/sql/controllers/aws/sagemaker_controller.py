from datetime import datetime
from commons.external_call import APIInterface
from sql import config, logger
from sql.crud.model_crud import CRUDModel
from sql.crud.project_flow_crud import CRUDProjectFlow

logging = logger(__name__)


class SagemakerController:
    def __init__(self):
        self.CRUDModel = CRUDModel()
        self.CRUDProjectFlow = CRUDProjectFlow()
        self.core_aws_model_config = (
            config.get("core_engine").get("aws").get("sagemaker_router")
        )

    def start_training_job_controller(self, request):
        """[Controller function to start training job for AWS Sagemaker project]

        Args:
            request ([dict]): [AWS Sagemaker Start Training job request]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [dict]: [AWS Sagemaker Start Training job response]
        """
        try:
            logging.info("executing start_training_job_controller function")
            uuid = str(int(datetime.now().timestamp()))
            start_training_request = request.dict(exclude_none=True)
            start_training_url = self.core_aws_model_config.get("start_training_job")
            response, status_code = APIInterface.post(
                route=start_training_url, data=start_training_request
            )
            if status_code == 200:
                crud_request = {
                    "pipeline_id": start_training_request.get("pipeline_id"),
                    "model_id": response.get("training_job_arn"),
                    "dataset_id": start_training_request.get("InputDataConfig"),
                    "artifacts": start_training_request.get("OutputDataConfig"),
                    "alias_name": start_training_request.get("TrainingJobName"),
                    "auto_trigger": False,
                    "UUID": uuid,
                    "status": "Running",
                    "created": datetime.now(),
                }
                self.CRUDModel.create(**crud_request)
                project_flow_crud_request = {
                    "pipeline_id": start_training_request.get("pipeline_id"),
                    "updated_at": datetime.now(),
                    "model_id": response.get("training_job_arn"),
                    "functional_stage_id": response.get("training_job_arn"),
                    "current_stage": "SAGEMAKER_TRAINING_STARTED",
                }
                self.CRUDProjectFlow.update(**project_flow_crud_request)
                response.update({"status": "training started"})
                return response
            else:
                raise Exception({"status": "training failed"})
        except Exception as error:
            logging.error(f"Error in start_training_job_controller function: {error}")
            raise error

    def stop_training_job_controller(self, request):
        """[Controller function to stop training job for AWS Sagemaker project]

        Args:
            request ([dict]): [AWS Sagemaker Stop Training job request]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [dict]: [AWS Sagemaker Training job status]
        """
        try:
            logging.info("executing stop_training_job_controller function")
            stop_training_request = request.dict(exclude_none=True)
            stop_training_url = self.core_aws_model_config.get("stop_training_job")
            response, status_code = APIInterface.post(
                route=stop_training_url, data=stop_training_request
            )
            if status_code == 200:
                crud_request = {
                    "alias_name": request.TrainingJobName,
                    "status": "Stopped",
                    "updated": datetime.now(),
                }
                self.CRUDModel.update_by_alias_name(crud_request)
                project_flow_crud_request = {
                    "pipeline_id": stop_training_request.get("pipeline_id"),
                    "updated_at": datetime.now(),
                    "current_stage": "SAGEMAKER_TRAINING_STOPPED",
                }
                self.CRUDProjectFlow.update(**project_flow_crud_request)
                return {"status": "training stopped"}
            else:
                raise Exception({"status": "training failed"})
        except Exception as error:
            logging.error(f"Error in stop_training_job_controller function: {error}")
            raise error

    def describe_training_job_controller(self, request):
        """[Controller function to describe training job for AWS Sagemaker project]

        Args:
            request ([dict]): [AWS Sagemaker Describe Training job request]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [dict]: [AWS Sagemaker Training job details]
        """
        try:
            logging.info("executing describe_training_job_controller function")
            describe_training_request = request.dict(exclude_none=True)
            describe_training_url = self.core_aws_model_config.get(
                "describe_training_job"
            )
            response, status_code = APIInterface.post(
                route=describe_training_url, data=describe_training_request
            )
            return response
        except Exception as error:
            logging.error(
                f"Error in describe_training_job_controller function: {error}"
            )
            raise error

    def list_training_job_controller(self):
        """[Controller function to list training job for AWS Sagemaker project]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [dict]: [List of AWS Sagemaker Training jobs]
        """
        try:
            logging.info("executing list_training_job_controller function")
            list_training_url = self.core_aws_model_config.get("list_training_job")
            response, status_code = APIInterface.get(route=list_training_url)
            return response
        except Exception as error:
            logging.error(f"Error in list_training_job_controller function: {error}")
            raise error
