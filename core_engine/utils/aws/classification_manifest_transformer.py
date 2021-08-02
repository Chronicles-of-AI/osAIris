import datetime


def aws_image_classification_transformation(json_data: dict):
    try:
        all_annotations = []
        for obj in json_data:
            cloud_uri = obj.get("data").get("image")
            annotations = obj.get("annotations")[0]
            results = annotations.get("result")
            class_name = results[0].get("value").get("choices")[0]
            final_sample_annot = {
                "source-ref": cloud_uri,
                "image_classification": 1,
                "image_classification-metadata": {
                    "confidence": 1,
                    "class-name": class_name,
                    "type": "groundtruth/image-classification",
                    "human-annotated": "yes",
                    "creation-date": "T".join(
                        str(datetime.datetime.today()).split(" ")
                    ),
                    "job-name": "labeling-job/image_classification",
                },
            }
            all_annotations.append(final_sample_annot)
        return all_annotations
    except Exception as e:
        print(e)


def aws_text_classification_transformation(json_data: dict):
    all_annotations = []
    for obj in json_data:
        text = obj.get("data").get("text")
        annotations = obj.get("annotations")[0]
        results = annotations.get("result")
        class_name = results[0].get("value").get("choices")[0]
        final_sample_annot = {
            "source": text,
            "text_classification": 1,
            "text_classification-metadata": {
                "confidence": 1,
                "class-name": class_name,
                "type": "groundtruth/text-classification",
                "human-annotated": "yes",
                "creation-date": "T".join(str(datetime.datetime.today()).split(" ")),
                "job-name": "labeling-job/text_classification",
            },
        }
        all_annotations.append(final_sample_annot)
    return all_annotations