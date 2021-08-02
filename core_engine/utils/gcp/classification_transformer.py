import pandas as pd


def gcp_image_classification_transformation(json_data: dict):
    all_annotations = []
    for obj in json_data:
        cloud_uri = obj.get("data").get("image")
        annotations = obj.get("annotations")[0]
        results = annotations.get("result")
        class_name = results[0].get("value").get("choices")[0]
        all_annotations.append([cloud_uri, class_name])
    annotations_df = pd.DataFrame(all_annotations)
    return annotations_df


def gcp_text_classification_transformation(json_data: dict):
    all_annotations = []
    for obj in json_data:
        text = obj.get("data").get("text")
        annotations = obj.get("annotations")[0]
        results = annotations.get("result")
        class_name = results[0].get("value").get("choices")[0]
        all_annotations.append([text, class_name])
    annotations_df = pd.DataFrame(all_annotations)
    return annotations_df
