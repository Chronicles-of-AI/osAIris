from commons.external_call import APIInterface
from sql import config, logger
from sql.crud.data_monitoring_crud import CRUDDataMonitoring
from sql.crud.project_flow_crud import CRUDProjectFlow
from sql.crud.services_crud import CRUDServices
from datetime import datetime

logging = logger(__name__)


class DataMonitoringController:
    def __init__(self):
        self.CRUDDataMonitoring = CRUDDataMonitoring()
        self.CRUDProjectFlow = CRUDProjectFlow()
        self.CRUDServices = CRUDServices()
        self.label_studio_config = config.get("label_studio").get("endpoint")
        self.label_studio_token = config.get("label_studio").get("token")
        self.header = {"Authorization": f"Token {self.label_studio_token}"}
        self.create_label_studio_task_url = self.label_studio_config.get("create_task")

    def get_task_id(self, request):
        response, status_code = APIInterface.post(
            route=self.create_label_studio_task_url,
            data=request,
            headers=self.header,
        )
        task_id = response.get("id")
        return task_id

    def create_data_monitoring_crud_request(self, request, task_id, inferred_results):
        crud_request = {
            "model_uri": request.get("model_uri"),
            "data": request.get("data"),
            "feedback": request.get("feedback"),
            "inferred_value": inferred_results,
            "ground_truth": request.get("ground_truth"),
            "annotation_task_id": task_id,
            "created_at": datetime.now(),
        }
        return crud_request

    def create_image_classification_record_controller(self, request):
        try:
            logging.info(
                "executing create_image_classification_record_controller function"
            )
            create_image_classification_record_request = request.dict(exclude_none=True)

            project_flow_record = self.CRUDProjectFlow.read_by_model_id(
                model_id=create_image_classification_record_request.get("model_uri")
            )
            create_label_studio_task_request = {
                "data": {"image": request.data},
                "is_labeled": False,
                "project": project_flow_record.get("annotation_project_id"),
            }
            task_id = self.get_task_id(request=create_label_studio_task_request)
            creat_annotation_url = (
                f"{self.create_label_studio_task_url}/{task_id}/annotations/"
            )
            create_annotation_request = {
                "result": [
                    {
                        "value": {
                            "choices": [
                                create_image_classification_record_request.get(
                                    "inferred_value"
                                )
                            ]
                        },
                        "from_name": "choice",
                        "to_name": "image",
                        "type": "choices",
                    }
                ],
                "ground_truth": True,
            }
            _, status_code = APIInterface.post(
                route=creat_annotation_url,
                data=create_annotation_request,
                headers=self.header,
            )
            if status_code == 200:
                crud_request = self.create_data_monitoring_crud_request(
                    request=create_image_classification_record_request,
                    task_id=task_id,
                    inferred_results=create_annotation_request,
                )
                self.CRUDDataMonitoring.create(**crud_request)
                return {"success": "yo"}
            else:
                raise Exception({"status": "Data creation failed"})
        except Exception as error:
            logging.error(
                f"Error in create_inferred_data_record_controller function: {error}"
            )
            raise error

    def create_text_classification_record_controller(self, request):
        try:
            logging.info(
                "executing create_text_classification_record_controller function"
            )
            create_text_classification_record_request = request.dict(exclude_none=True)

            project_flow_record = self.CRUDProjectFlow.read_by_model_id(
                model_id=create_text_classification_record_request.get("model_uri")
            )
            create_label_studio_task_request = {
                "data": {"text": request.data},
                "is_labeled": False,
                "project": project_flow_record.get("annotation_project_id"),
            }
            task_id = self.get_task_id(request=create_label_studio_task_request)
            creat_annotation_url = (
                f"{self.create_label_studio_task_url}/{task_id}/annotations/"
            )
            create_annotation_request = {
                "result": [
                    {
                        "value": {
                            "choices": [
                                create_text_classification_record_request.get(
                                    "inferred_value"
                                )
                            ]
                        },
                        "from_name": "sentiment",
                        "to_name": "text",
                        "type": "choices",
                    }
                ],
                "ground_truth": True,
            }
            _, status_code = APIInterface.post(
                route=creat_annotation_url,
                data=create_annotation_request,
                headers=self.header,
            )
            if status_code == 200:
                crud_request = self.create_data_monitoring_crud_request(
                    request=create_text_classification_record_request,
                    task_id=task_id,
                    inferred_results=create_annotation_request,
                )
                self.CRUDDataMonitoring.create(**crud_request)
                return {"success": "yo"}
            else:
                raise Exception({"status": "Data creation failed"})
        except Exception as error:
            logging.error(
                f"Error in create_inferred_data_record_controller function: {error}"
            )
            raise error

    def create_object_detection_record_controller(self, request):
        try:
            logging.info("executing create_object_detection_record_controller function")
            create_object_detection_record_request = request.dict(exclude_none=True)

            project_flow_record = self.CRUDProjectFlow.read_by_model_id(
                model_id=create_object_detection_record_request.get("model_uri")
            )
            create_label_studio_task_request = {
                "data": {"image": request.inferred_value},
                "is_labeled": False,
                "project": project_flow_record.get("annotation_project_id"),
            }
            task_id = self.get_task_id(request=create_label_studio_task_request)
            creat_annotation_url = (
                f"{self.create_label_studio_task_url}/{task_id}/annotations/"
            )
            final_result = [
                result_data.update(
                    {
                        "type": "labels",
                        "to_name": "text",
                        "from_name": "label",
                    }
                )
                for result_data in request.inferred_value
            ]
            create_annotation_request = {
                "result": final_result,
                "ground_truth": True,
            }
            _, status_code = APIInterface.post(
                route=creat_annotation_url,
                data=create_annotation_request,
                headers=self.header,
            )
            if status_code == 200:
                crud_request = self.create_data_monitoring_crud_request(
                    request=create_object_detection_record_request,
                    task_id=task_id,
                    inferred_results=create_annotation_request,
                )
                self.CRUDDataMonitoring.create(**crud_request)
                return {"success": "yo"}
            else:
                raise Exception({"status": "Data creation failed"})
        except Exception as error:
            logging.error(
                f"Error in create_inferred_data_record_controller function: {error}"
            )
            raise error

    def create_ner_record_controller(self, request):
        try:
            logging.info("executing create_object_detection_record_controller function")
            create_ner_record_request = request.dict(exclude_none=True)

            project_flow_record = self.CRUDProjectFlow.read_by_model_id(
                model_id=create_ner_record_request.get("model_uri")
            )
            create_label_studio_task_request = {
                "data": {"text": request.data},
                "is_labeled": False,
                "project": project_flow_record.get("annotation_project_id"),
            }
            task_id = self.get_task_id(request=create_label_studio_task_request)
            creat_annotation_url = (
                f"{self.create_label_studio_task_url}/{task_id}/annotations/"
            )
            final_result = [
                result_data.update(
                    {
                        "type": "labels",
                        "to_name": "text",
                        "from_name": "label",
                    }
                )
                for result_data in request.inferred_value
            ]
            create_annotation_request = {
                "result": final_result,
                "ground_truth": True,
            }
            _, status_code = APIInterface.post(
                route=creat_annotation_url,
                data=create_annotation_request,
                headers=self.header,
            )
            if status_code == 200:
                crud_request = self.create_data_monitoring_crud_request(
                    request=create_ner_record_request,
                    task_id=task_id,
                    inferred_results=create_annotation_request,
                )
                self.CRUDDataMonitoring.create(**crud_request)
                return {"success": "yo"}
            else:
                raise Exception({"status": "Data creation failed"})
        except Exception as error:
            logging.error(
                f"Error in create_inferred_data_record_controller function: {error}"
            )
            raise error

    def update_inferred_data_record_controller(self, request):
        try:
            logging.info("executing create_inferred_data_record_controller function")
            update_inferred_data_record_request = request.dict(exclude_none=True)
            update_inferred_data_record_url = self.label_studio_config.get(
                "create_task"
            )
            response, status_code = APIInterface.post(
                route=update_inferred_data_record_url,
                data=update_inferred_data_record_request,
            )
            self.CRUDDataMonitoring.update(
                annotation_task_id=request.annotation_task_id,
                ground_truth=request.ground_truth,
            )
            return {"success": "yo"}
        except Exception as error:
            logging.error(
                f"Error in create_inferred_data_record_controller function: {error}"
            )
            raise error
