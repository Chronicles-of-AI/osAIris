import json
import pandas as pd
from datetime import datetime
from core_engine import logger
from core_engine.utils.gcp.gcs_helper import upload_blob_string

logging = logger(__name__)


def gcp_ner_helper(annotations: list, threshold: float, request):
    try:
        total_annotations = len(annotations)
        train_samples = []
        test_samples = []
        validate_samples = []

        train_numbers = int(total_annotations * threshold)
        test_numbers = train_numbers + int(total_annotations * ((1 - threshold) / 2))

        validate_numbers = test_numbers + int(total_annotations * ((1 - threshold) / 2))
        for index, annot in enumerate(annotations):
            if 0 < index <= train_numbers:
                train_samples.append(annot)
            elif train_numbers < index <= test_numbers:
                test_samples.append(annot)
            elif test_numbers < index <= validate_numbers:
                validate_samples.append(annot)

        with open("ner_train.jsonl", "w") as annot_train:
            for annot in train_samples:
                json.dump(annot, annot_train)
                annot_train.write("\n")
        train_gcs_uri = upload_blob_string(
            bucket_name=request.output_data_bucket_name,
            destination_file_name=f"{request.output_data_file_prefix}/annotations_train_{str(int(datetime.now().timestamp())*10000)}.jsonl",
            content_type="application/json",
            file=annot_train,
        )
        with open("ner_test.jsonl", "w") as annot_test:
            for annot in test_samples:
                json.dump(annot, annot_test)
                annot_test.write("\n")
        test_gcs_uri = upload_blob_string(
            bucket_name=request.output_data_bucket_name,
            destination_file_name=f"{request.output_data_file_prefix}/annotations_test_{str(int(datetime.now().timestamp())*10000)}.jsonl",
            content_type="application/json",
            file=annot_test,
        )
        with open("ner_validation.jsonl", "w") as annot_validation:
            for annot in validate_samples:
                json.dump(annot, annot_validation)
                annot_validation.write("\n")
        validate_gcs_uri = upload_blob_string(
            bucket_name=request.output_data_bucket_name,
            destination_file_name=f"{request.output_data_file_prefix}/annotations_validate_{str(int(datetime.now().timestamp())*10000)}.jsonl",
            content_type="application/json",
            file=annot_validation,
        )
        all_annotations = [
            ["TRAIN", train_gcs_uri],
            ["TEST", test_gcs_uri],
            ["VALIDATION", validate_gcs_uri],
        ]
        return all_annotations
    except Exception as error:
        logging.error(f"{error=}")
        raise error


def gcp_ner_transformation(json_data: dict, request):
    """[NER Transformation from Label Studio to AutoML format]

    Args:
        json_data (dict): [Annotations]

    Raises:
        error: [Error]

    Returns:
        [list]: [List of Annotations]
    """
    try:
        logging.info(f"NER Transformer: {json_data}")
        all_annotations = []
        for obj in json_data:
            annotations_for_sent = []
            text = obj.get("data").get("text")
            annotations = obj.get("annotations")[0]
            results = annotations.get("result")
            for result in results:
                label = result.get("value").get("labels")[0]
                endOffset = result.get("value").get("end")
                startOffset = result.get("value").get("start")
                current_annot = {
                    "text_extraction": {
                        "text_segment": {
                            "end_offset": endOffset,
                            "start_offset": startOffset,
                        }
                    },
                    "display_name": label,
                }
                annotations_for_sent.append(current_annot)
            final_annot = {
                "annotations": annotations_for_sent,
                "text_snippet": {"content": text},
            }
            all_annotations.append(final_annot)
        annotations_ref = gcp_ner_helper(
            annotations=all_annotations, threshold=0.8, request=request
        )
        annotations_df = pd.DataFrame(annotations_ref)
        return annotations_df
    except Exception as error:
        logging.error(f"{error=}")
        raise error
