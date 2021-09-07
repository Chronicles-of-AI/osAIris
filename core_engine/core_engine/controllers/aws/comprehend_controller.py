from core_engine.utils.aws.comprehend_helper import (
    create_document_classifier,
    delete_document_classifier,
    describe_document_classifier,
    list_document_classifier,
    stop_training_document_classifier,
    create_entity_recognizer,
    delete_entity_recognizer,
    describe_entity_recognizer,
    list_entity_recognizer,
    stop_training_entity_recognizer,
    deploy_model,
    undeploy_model,
    get_predictions,
)
from core_engine import logger

logging = logger(__name__)


class ComprehendController:
    def create_document_classifier_controller(self, request):
        """[Creates a Document Classifier ]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [description]
        """
        try:
            logging.info(f"Create Document Classifier Controller: {request}")
            create_document_classifier_request = request.dict(exclude_none=True)
            return create_document_classifier(
                document_classifier_name=create_document_classifier_request.get(
                    "DocumentClassifierName"
                ),
                data_access_role_arn=create_document_classifier_request.get(
                    "DataAccessRoleArn"
                ),
                input_data_config=create_document_classifier_request.get(
                    "InputDataConfig"
                ),
                output_data_config=create_document_classifier_request.get(
                    "OutputDataConfig"
                ),
                language_code=create_document_classifier_request.get("LanguageCode"),
                classification_mode=create_document_classifier_request.get("Mode"),
            )
        except Exception as error:
            logging.error(f"{error=}")
            raise error

    def delete_document_classifier_controller(self, request):
        """[Deleted a Document Classifier ]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [description]
        """
        try:
            logging.info(
                f"Delete Document Classifier Controller: {request.DocumentClassifierArn}"
            )
            return delete_document_classifier(
                document_classifier_arn=request.DocumentClassifierArn
            )
        except Exception as error:
            logging.error(f"{error=}")
            raise error

    def describe_document_classifier_controller(self, request):
        """[Describes a Document Classifier ]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [description]
        """
        try:
            logging.info(
                f"Describe Document Classifier Controller: {request.DocumentClassifierArn}"
            )
            return describe_document_classifier(
                document_classifier_arn=request.DocumentClassifierArn
            )
        except Exception as error:
            logging.error(f"{error=}")
            raise error

    def stop_training_document_classifier_controller(self, request):
        """[Stops training a Document Classifier ]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [description]
        """
        try:
            logging.info(
                f"Stop Training Document Classifier Controller: {request.DocumentClassifierArn}"
            )
            return stop_training_document_classifier(
                document_classifier_arn=request.DocumentClassifierArn
            )
        except Exception as error:
            logging.error(f"{error=}")
            raise error

    def list_document_classifier_controller(self):
        """[Lists Document Classifiers ]

        Raises:
            error: [Error]

        Returns:
            [type]: [description]
        """
        try:
            logging.info(f"List Document Classifier Controller")
            return list_document_classifier()
        except Exception as error:
            logging.error(f"{error=}")
            raise error

    def create_entity_recognizer_controller(self, request):
        """[Creates a Entity Recognizer ]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [description]
        """
        try:
            logging.info(f"Create Entity Recognizer Controller: {request}")
            create_entity_recognizer_request = request.dict(exclude_none=True)
            return create_entity_recognizer(
                recognizer_name=create_entity_recognizer_request.get("RecognizerName"),
                data_access_role_arn=create_entity_recognizer_request.get(
                    "DataAccessRoleArn"
                ),
                input_data_config=create_entity_recognizer_request.get(
                    "InputDataConfig"
                ),
            )
        except Exception as error:
            logging.error(f"{error=}")
            raise error

    def delete_entity_recognizer_controller(self, request):
        """[Deleted a Entity Recognizer ]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [description]
        """
        try:
            logging.info(
                f"Delete Entity Recognizer Controller: {request.EntityRecognizerArn}"
            )
            return delete_entity_recognizer(
                entity_recognizer_arn=request.EntityRecognizerArn
            )
        except Exception as error:
            logging.error(f"{error=}")
            raise error

    def describe_entity_recognizer_controller(self, request):
        """[Describes a Entity Recognizer ]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [description]
        """
        try:
            logging.info(
                f"Describe Entity Recognizer Controller: {request.EntityRecognizerArn}"
            )
            return describe_entity_recognizer(
                entity_recognizer_arn=request.EntityRecognizerArn
            )
        except Exception as error:
            logging.error(f"{error=}")
            raise error

    def stop_training_entity_recognizer_controller(self, request):
        """[Stops training a Entity Recognizer ]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [description]
        """
        try:
            logging.info(
                f"Stop Training Entity Recognizer Controller: {request.EntityRecognizerArn}"
            )
            return stop_training_entity_recognizer(
                entity_recognizer_arn=request.EntityRecognizerArn
            )
        except Exception as error:
            logging.error(f"{error=}")
            raise error

    def list_entity_recognizer_controller(self):
        """[Lists Entity Recognizer ]

        Raises:
            error: [Error]

        Returns:
            [type]: [description]
        """
        try:
            logging.info(f"List Entity Recognizer Controller")
            return list_document_classifier()
        except Exception as error:
            logging.error(f"{error=}")
            raise error

    def deploy_model_controller(self, request):
        """[Deploys a Document Classifier ]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [description]
        """
        try:
            logging.info(f"Deploy Document Classifier Controller: {request.model_arn}")
            logging.info(f"Endpoint ARN: {request.endpoint_name}")
            return deploy_model(
                min_inference_units=request.min_inference_units,
                endpoint_name=request.endpoint_name,
                model_arn=request.model_arn,
            )
        except Exception as error:
            logging.error(f"{error=}")
            raise error

    def undeploy_model_controller(self, request):
        """[Un-Deploys a Document Classifier ]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [description]
        """
        try:
            logging.info(
                f"Undeploy Document Classifier Controller: {request.endpoint_arn}"
            )
            undeploy_model(endpoint_arn=request.endpoint_arn)
            return {"status": "Document Classifier Un-deployed"}
        except Exception as error:
            logging.error(f"{error=}")
            raise error

    def get_predictions_controller(self, endpoint_arn: str, text: str):
        """[Get Predictions from a Document Classifier ]

        Args:
            endpoint_arn (str): [End point name]
            text (str): [sample Text]

        Raises:
            error: [Error]

        Returns:
            [type]: [description]
        """
        try:
            logging.info(f"Get Predictions from: {endpoint_arn}")
            logging.info(f"{text=}")
            return get_predictions(endpoint_arn=endpoint_arn, text=text)
        except Exception as error:
            logging.error(f"{error=}")
            raise error
