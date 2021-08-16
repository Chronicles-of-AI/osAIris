from core_engine.utils.aws.sagemaker_helper import (
    start_training_job,
    stop_training_job,
    describe_training_job,
    list_training_job,
)
from core_engine import logger

logging = logger(__name__)


class SagemakerController:
    def start_training_job_controller(self, request):
        """[Start a Training Job in AWS Sagemaker]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [Unique Identifier of your Training Job]
        """
        try:
            logging.info(f"Start Training Job Controller: {request}")
            start_training_request = request.dict(exclude_none=True)
            response = start_training_job(
                training_job=start_training_request.get("TrainingJobName"),
                algorithm_specification=start_training_request.get(
                    "AlgorithmSpecification"
                ),
                role_arn=start_training_request.get("RoleArn"),
                input_data_config=start_training_request.get("InputDataConfig"),
                output_data_config=start_training_request.get("OutputDataConfig"),
                resource_config=start_training_request.get("ResourceConfig"),
                stopping_condition=start_training_request.get("StoppingCondition"),
            )
            return {"training_job_arn": response}
        except Exception as error:
            logging.error(f"{error=}")
            raise error

    def stop_training_job_controller(self, request):
        """[Stop a Training Job in AWS Sagemaker]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [description]
        """
        try:
            logging.info(f"Stop Training Job Controller: {request}")
            stop_training_request = request.dict(exclude_none=True)
            return stop_training_job(
                training_job_name=stop_training_request.get("TrainingJobName")
            )
        except Exception as error:
            logging.error(f"{error=}")
            raise error

    def describe_training_job_controller(self, request):
        """[Describe a Training Job in AWS Sagemaker]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [description]
        """
        try:
            logging.info(f"Describe Training Job Controller: {request}")
            describe_training_request = request.dict(exclude_none=True)
            return describe_training_job(
                training_job_name=describe_training_request.get("TrainingJobName")
            )
        except Exception as error:
            logging.error(f"{error=}")
            raise error

    def list_training_job_controller(self):
        """[List Training Jobs in AWS Sagemaker]

        Raises:
            error: [Error]

        Returns:
            [type]: [List of Training Jobs]
        """
        try:
            logging.info(f"List Training Job Controller")
            return list_training_job()
        except Exception as error:
            logging.error(f"{error=}")
            raise error
