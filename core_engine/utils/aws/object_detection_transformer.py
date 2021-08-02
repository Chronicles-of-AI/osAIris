import datetime


def aws_object_detection_transformation(json_data: dict):
    all_annotations = []
    annotation_labels = {}
    for object in json_data:
        cloud_uri = object.get("data").get("image")
        annotations = object.get("annotations")[0]
        results = annotations.get("result")
        user_annotations = []
        objects = []
        class_map = {}
        for result in results:
            values = result.get("value")
            image_width = result.get("original_width")
            image_height = result.get("original_height")
            top = values.get("x")
            left = values.get("y")
            width = values.get("width")
            height = values.get("height")
            label = values.get("rectanglelabels")[0]
            if label in annotation_labels:
                pass
            else:
                annotation_labels[label] = len(annotation_labels)
            annot_dict = {
                "class_id": annotation_labels.get(label),
                "top": top,
                "left": left,
                "width": width,
                "height": height,
            }
            user_annotations.append(annot_dict)
            objects.append({"confidence": 1})
            class_map.update({str(annotation_labels.get(label)): label})
        final_sample_annot = {
            "source-ref": cloud_uri,
            "bounding-box": {
                "image_size": [
                    {"width": image_width, "height": image_height, "depth": 3}
                ],
                "annotations": user_annotations,
            },
            "bounding-box-metadat": {
                "objects": objects,
                "class-map": class_map,
                "type": "groundtruth/object-detection",
                "human-annotated": "yes",
                "creation-date": "T".join(str(datetime.datetime.today()).split(" ")),
                "job-name": "bounding-box-job",
            },
        }
        all_annotations.append(final_sample_annot)
    return all_annotations