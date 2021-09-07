import datetime
from core_engine import logger

logging = logger(__name__)


def aws_ner_transformation(json_data: dict):
    """[Converting Label Studio Annotations to AWS Manifest file needs]

    Args:
        json_data (dict): [All annotations]

    Raises:
        e: [Error]

    Returns:
        [list]: [All Annotations]
    """
    try:
        logging.info(f"AWS NER Transformation for JSON: {json_data}")
        all_annotations = []
        for obj in json_data:
            confidence_scores = []
            annot_entities = []
            labels = []
            text = obj.get("data").get("ner")
            annotations = obj.get("annotations")[0]
            results = annotations.get("result")
            for result in results:
                label = result.get("value").get("labels")[0]
                endOffset = result.get("value").get("end")
                startOffset = result.get("value").get("start")
                current_annot = {
                    "endOffset": endOffset,
                    "startOffset": startOffset,
                    "label": label,
                }
                current_label = {"label": label}
                conf_label = {"confidence": 1}

                annot_entities.append(current_annot)
                labels.append(current_label)
                confidence_scores.append(conf_label)

            final_sample_annot = {
                "source": text,
                "named_entity_recognition": {
                    "annotations": {"entities": annot_entities, "labels": labels}
                },
                "named_entity_recognition-metadata": {
                    "entities": confidence_scores,
                    "type": "groundtruth/text-span",
                    "human-annotated": "yes",
                    "creation-date": "T".join(
                        str(datetime.datetime.today()).split(" ")
                    ),
                    "job-name": "labeling-job/named_entity_recognition",
                },
            }
            all_annotations.append(final_sample_annot)
        return all_annotations
    except Exception as e:
        logging.error(e)
        raise e
