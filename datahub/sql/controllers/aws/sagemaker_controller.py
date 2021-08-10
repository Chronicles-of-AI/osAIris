from datetime import datetime
from commons.external_call import APIInterface
from sql import config
from sql.crud.model_crud import CRUDModel


class SagemakerController:
    def __init__(self):
        self.CRUDModel = CRUDModel()
        self.core_aws_model_config = (
            config.get("core_engine").get("aws").get("sagemaker_router")
        )

    def start_training_job_controller(self, request):
        """[summary]

        Args:
            request ([type]): [description]

        Raises:
            error: [description]

        Returns:
            [type]: [description]
        """
        try:
            uuid = str(int(datetime.now().timestamp()))
            start_training_request = request.dict(exclude_none=True)
            start_training_url = self.core_aws_model_config.get("start_training_job")
            response, status_code = APIInterface.post(
                route=start_training_url, data=start_training_request
            )
            if status_code == 200:
                crud_request = {
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
                response.update({"status": "training started"})
                return response
            else:
                # TODO: error
                pass
                return {"status": "training failed"}
        except Exception as error:
            raise error

    def stop_training_job_controller(self, request):
        """[summary]

        Args:
            request ([type]): [description]

        Raises:
            error: [description]

        Returns:
            [type]: [description]
        """
        try:
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
                return {"status": "training stopped"}
            else:
                # TODO: error
                pass
                return {"status": "training failed"}
        except Exception as error:
            raise error

    def describe_training_job_controller(self, request):
        """[summary]

        Args:
            request ([type]): [description]

        Raises:
            error: [description]

        Returns:
            [type]: [description]
        """
        try:
            describe_training_request = request.dict(exclude_none=True)
            describe_training_url = self.core_aws_model_config.get(
                "describe_training_job"
            )
            response, status_code = APIInterface.post(
                route=describe_training_url, data=describe_training_request
            )
            return response
        except Exception as error:
            raise error

    def list_training_job_controller(self):
        """[summary]

        Raises:
            error: [description]

        Returns:
            [type]: [description]
        """
        try:
            list_training_url = self.core_aws_model_config.get("list_training_job")
            response, status_code = APIInterface.get(route=list_training_url)
            return response
        except Exception as error:
            raise error
