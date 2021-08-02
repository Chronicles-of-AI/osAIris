from google.cloud import automl
from utils.gcp.gcs_helper import read_file_from_gcs

prediction_client = automl.PredictionServiceClient()


def text_model_prediction(project_id: str, model_id: str, content: str, region: str):
    model_full_id = automl.AutoMlClient.model_path(project_id, region, model_id)

    text_snippet = automl.TextSnippet(content=content, mime_type="text/plain")
    payload = automl.ExamplePayload(text_snippet=text_snippet)

    response = prediction_client.predict(name=model_full_id, payload=payload)
    response_dict = {}
    for result in response.payload:
        response_dict.update({result.display_name: result.classification.score})
    return response_dict


def image_model_prediction(project_id: str, model_id: str, region: str, gcs_uri: str):
    bucket_name = gcs_uri.split("//")[-1].split("/")[0]
    file_path = "/".join(gcs_uri.split("//")[-1].split("/")[1:])

    model_full_id = automl.AutoMlClient.model_path(project_id, region, model_id)
    file_bytes = read_file_from_gcs(file_path=file_path, bucket_name=bucket_name)
    image = automl.Image(image_bytes=file_bytes)
    payload = automl.ExamplePayload(image=image)
    params = {"score_threshold": "0.8"}

    request = automl.PredictRequest(name=model_full_id, payload=payload, params=params)
    response = prediction_client.predict(request=request)
    response_dict = {}
    for result in response.payload:
        response_dict.update({result.display_name: result.classification.score})
    return response_dict
