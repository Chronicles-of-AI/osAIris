from utils.aws.comprehend_helper import (
    create_document_classifier,
    delete_document_classifier,
    describe_document_classifier,
    list_document_classifier,
    stop_training_document_classifier,
    deploy_document_classifier,
    undeploy_document_classifier,
    get_predictions,
)


class ComprehendController:
    def create_document_classifier_controller(self, request):
        create_document_classifier_request = request.dict(exclude_none=True)
        return create_document_classifier(
            document_classifier_name=create_document_classifier_request.get(
                "DocumentClassifierName"
            ),
            data_access_role_arn=create_document_classifier_request.get(
                "DataAccessRoleArn"
            ),
            input_data_config=create_document_classifier_request.get("InputDataConfig"),
            output_data_config=create_document_classifier_request.get(
                "OutputDataConfig"
            ),
            language_code=create_document_classifier_request.get("LanguageCode"),
            classification_mode=create_document_classifier_request.get("Mode"),
        )

    def delete_document_classifier_controller(self, request):
        return delete_document_classifier(
            document_classifier_arn=request.DocumentClassifierArn
        )

    def describe_document_classifier_controller(self, request):
        return describe_document_classifier(
            document_classifier_arn=request.DocumentClassifierArn
        )

    def stop_training_document_classifier_controller(self, request):
        return stop_training_document_classifier(
            document_classifier_arn=request.DocumentClassifierArn
        )

    def list_document_classifier_controller(self):
        return list_document_classifier()

    def deploy_document_classifier_controller(self, request):
        return deploy_document_classifier(
            min_inference_units=request.min_inference_units,
            endpoint_name=request.endpoint_name,
            model_arn=request.model_arn,
        )

    def undeploy_document_classifier_controller(self, request):
        undeploy_document_classifier(endpoint_arn=request.endpoint_arn)
        return {"status": "Document Classifier Un-deployed"}

    def get_predictions_controller(self, endpoint_arn: str, text: str):
        return get_predictions(endpoint_arn=endpoint_arn, text=text)
