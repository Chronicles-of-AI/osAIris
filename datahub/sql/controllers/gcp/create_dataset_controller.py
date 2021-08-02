from commons.external_call import APIInterface
from sql import config
from sql.crud.dataset_crud import CRUDDataset
from datetime import datetime


class CreateDatasetController:
    def __init__(self):
        self.gcp_config = config.get("core_engine").get("gcp")
        self.CRUDDataset = CRUDDataset()

    def create_text_classification_dataset_controller(self, request):
        uuid = str(int(datetime.now().timestamp()) * 10000)
        create_dataset_url = (
            self.gcp_config.get("automl")
            .get("text")
            .get("create_classification_dataset")
        )
        create_dataset_request = request.dict(exclude_none=True)
        response, status_code = APIInterface.post(
            route=create_dataset_url, data=create_dataset_request
        )
        print(f"{response=}")
        if status_code == 200:
            crud_request = {
                "dataset_id": response.get("dataset_id"),
                "alias_name": create_dataset_request.get("display_name"),
                "UUID": uuid,
                "status": "Created",
                "problem_type": "text_classification",
            }
            print(f"{crud_request=}")
            self.CRUDDataset.create(**crud_request)
            return {
                "dataset_name": create_dataset_request.get("display_name"),
                "dataset_id": response.get("dataset_id"),
            }
        else:
            # TODO: error
            pass
            return {"status": "create dataset failed"}

    def create_ner_dataset_controller(self, request):
        uuid = str(int(datetime.now().timestamp()) * 10000)
        create_dataset_url = (
            self.gcp_config.get("automl").get("text").get("create_ner_dataset")
        )
        create_dataset_request = request.dict(exclude_none=True)
        response, status_code = APIInterface.post(
            route=create_dataset_url, data=create_dataset_request
        )
        if status_code == 200:
            crud_request = {
                "dataset_id": response.get("dataset_id"),
                "alias_name": create_dataset_request.get("display_name"),
                "UUID": uuid,
                "status": "Created",
                "problem_type": "text_ner",
            }
            self.CRUDDataset.create(**crud_request)
            return {
                "dataset_name": create_dataset_request.get("display_name"),
                "dataset_id": response.get("dataset_id"),
            }
        else:
            # TODO: error
            pass
            return {"status": "create dataset failed"}

    def create_image_classification_dataset_controller(self, request):
        uuid = str(int(datetime.now().timestamp()) * 10000)
        create_dataset_url = (
            self.gcp_config.get("automl")
            .get("image")
            .get("create_image_classification_dataset")
        )
        create_dataset_request = request.dict(exclude_none=True)
        response, status_code = APIInterface.post(
            route=create_dataset_url, data=create_dataset_request
        )
        if status_code == 200:
            crud_request = {
                "dataset_id": response.get("dataset_id"),
                "alias_name": create_dataset_request.get("display_name"),
                "UUID": uuid,
                "status": "Created",
                "problem_type": "image_classification",
            }
            self.CRUDDataset.create(**crud_request)
            return {
                "dataset_name": create_dataset_request.get("display_name"),
                "dataset_id": response.get("dataset_id"),
            }
        else:
            # TODO: error
            pass
            return {"status": "create dataset failed"}

    def create_object_detection_dataset_controller(self, request):
        uuid = str(int(datetime.now().timestamp()) * 10000)
        create_dataset_url = (
            self.gcp_config.get("automl")
            .get("image")
            .get("create_object_detection_dataset")
        )
        create_dataset_request = request.dict(exclude_none=True)
        response, status_code = APIInterface.post(
            route=create_dataset_url, data=create_dataset_request
        )
        if status_code == 200:
            crud_request = {
                "dataset_id": response.get("dataset_id"),
                "alias_name": create_dataset_request.get("display_name"),
                "UUID": uuid,
                "status": "Created",
                "problem_type": "object_detection",
            }
            self.CRUDDataset.create(**crud_request)
            return {
                "dataset_name": create_dataset_request.get("display_name"),
                "dataset_id": response.get("dataset_id"),
            }
        else:
            # TODO: error
            pass
            return {"status": "create dataset failed"}
