from utils.aws.sagemaker_helper import (
    start_training_job,
    stop_training_job,
    describe_training_job,
    list_training_job,
)


class SagemakerController:
    def start_training_job_controller(self, request):
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

    def stop_training_job_controller(self, request):
        stop_training_request = request.dict(exclude_none=True)
        return stop_training_job(
            training_job_name=stop_training_request.get("TrainingJobName")
        )

    def describe_training_job_controller(self, request):
        describe_training_request = request.dict(exclude_none=True)
        return describe_training_job(
            training_job_name=describe_training_request.get("TrainingJobName")
        )

    def list_training_job_controller(self):
        return list_training_job()
