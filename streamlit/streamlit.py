import streamlit as st
import json
import os
from external_call import APIInterface
from PIL import Image
import pandas as pd

IP = os.environ.get("IP", "192.168.29.208")
DATA_HUB = f"http://{IP}:7000"
DOCUMENTATION = f"http://{IP}:80"
asset_name = "mObius"
page_icon_path = "/Users/arpitkjain/Desktop/Data/POC/osAIris/docs/logo.jpeg"
home_page_image = "/Users/arpitkjain/Desktop/Data/POC/osAIris/docs/logo.jpeg"
sidebar_image_path = "/Users/arpitkjain/Desktop/Data/POC/osAIris/docs/logo.jpeg"

st.set_page_config(
    page_title=asset_name,
    page_icon=Image.open(page_icon_path),
    initial_sidebar_state="auto",
)
st.image(home_page_image)
st.title(f"Welcome to {asset_name}")


def import_dataset(token, project_id, dataset_id, gcs_path, region):
    response, status_code = APIInterface.post(
        route=f"{DATA_HUB}/gcp/automl/import_dataset",
        data={
            "pipeline_id": 0,
            "project_id": project_id,
            "dataset_id": dataset_id,
            "gcs_path": gcs_path,
            "region": region,
        },
        headers={"Authorization": token},
    )
    return response


with st.beta_expander("Login"):
    with st.form("authentication"):
        st.write("Authorize User")
        username = st.text_input("User Name")
        password = st.text_input("Password", type="password")
        submitted = st.form_submit_button("Login")
        if submitted:
            with st.spinner("Working on it..."):
                response, status_code = APIInterface.post_form(
                    route=f"{DATA_HUB}/user/login",
                    data={
                        "username": username,
                        "password": password,
                    },
                )
            token = response.get("access_token")
            with open("token.json", "w+") as f:
                json.dump({"token": f"Bearer {token}"}, f)
            st.success("Done!")
            st.json({"status": "User Authenticated"})

with st.beta_expander("Step 1: Create mobius Poject"):
    token_obj = json.load(open("token.json", "r"))
    token = token_obj.get("token")
    with st.form("create_mobius_project"):
        st.subheader("Configure Project")
        pipeline_name = st.text_input("Pipeline Name")
        pipeline_description = st.text_input("Pipeline Description")
        cloud_service_provider = st.radio("Cloud Vendors", ("AWS", "GCP"))
        st.session_state["cloud_service_provider"] = cloud_service_provider.lower()
        annotation_project_name = st.text_input("Annotation Name")
        annotation_project_description = st.text_input("Annotation Description")
        use_case = st.selectbox(
            "Supported Use Cases",
            (
                "image_classification",
                "text_classification",
                "object_detection",
                "natural_entity_recognition",
            ),
        )
        submitted = st.form_submit_button("Create Project")
        if submitted:
            with st.spinner("Working on it..."):
                response, status_code = APIInterface.post(
                    route=f"{DATA_HUB}/osairis/project_flow/create",
                    data={
                        "pipeline_name": pipeline_name,
                        "pipeline_description": pipeline_description,
                        "cloud_service_provider": cloud_service_provider.lower(),
                        "annotation_project_name": annotation_project_name,
                        "annotation_project_description": annotation_project_description,
                        "use_case": use_case,
                    },
                    headers={"Authorization": token},
                )
                st.session_state["annotation_project_id"] = response.get(
                    "annotation_project_id"
                )
                st.session_state["use_case"] = use_case
            st.success("Done!")
            st.json(response)

st.sidebar.image(sidebar_image_path)
st.sidebar.title("Side Features")
st.sidebar.subheader("All Projects")
submitted = st.sidebar.button("Refresh", key="refresh_projects")
if submitted:
    with st.spinner("Working on it..."):
        response, status_code = APIInterface.get(
            route=f"{DATA_HUB}/osairis/project_flow",
            headers={"Authorization": token},
        )
    st.success("Done!")
    df = pd.DataFrame(response)
    st.dataframe(df)

st.sidebar.subheader("All Storages")
if "annotation_project_id" not in st.session_state:
    # project_id = st.sidebar.text_input(label="Annotation Project ID")
    project_id = 0
else:
    project_id = st.session_state["annotation_project_id"]
submitted = st.sidebar.button("Refresh", key="refresh_storages")
if submitted:
    response, status_code = APIInterface.get(
        route=f"{DATA_HUB}/label_studio/list_storages",
        params={"project_id": project_id},
        headers={"Authorization": token},
    )
    st.sidebar.success("Done!")
    df = pd.DataFrame(response)
    st.sidebar.dataframe(df)

st.sidebar.subheader("Operation Status")
operation_id = st.sidebar.text_input("Operation ID")
submitted = st.sidebar.button("Check", key="operation_status")
if submitted:
    response, status_code = APIInterface.get(
        route=f"{DATA_HUB}/gcp/automl/get_operation_details",
        params={"operation_id": operation_id},
        headers={"Authorization": token},
    )
    st.sidebar.success("Done!")
    st.sidebar.json(response)

st.sidebar.markdown(
    """
<large>[DOCUMENTATION](http://0.0.0.0:7000/documentation)</large>
    """,
    unsafe_allow_html=True,
)
with st.beta_expander("Step 2: Configure Annotation Task"):
    token_obj = json.load(open("token.json", "r"))
    token = token_obj.get("token")
    with st.form("configure_annotation_project"):
        st.subheader("Add Storage to Project")
        storage_title = st.text_input("Storage title")
        storage_description = st.text_input("Storage Description")
        cloud_bucket_name = st.text_input("Cloud Bucket Name")
        annotation_project_id = st.number_input("Annotation Project Id", min_value=0)
        cloud_service_provider = st.session_state.cloud_service_provider
        if cloud_service_provider == "aws":
            route = f"{DATA_HUB}/label_studio/create_s3_storage"
            data = {
                "project": annotation_project_id,
                "title": storage_title,
                "description": storage_description,
                "bucket": cloud_bucket_name,
                "region_name": "us-east-2",
                "use_blob_urls": True,
            }
        elif cloud_service_provider == "gcp":
            route = f"{DATA_HUB}/label_studio/create_gcs_storage"
            data = {
                "project": annotation_project_id,
                "title": storage_title,
                "description": storage_description,
                "bucket": cloud_bucket_name,
                "use_blob_urls": True,
            }
        submitted = st.form_submit_button("Add Storage")
        if submitted:
            with st.spinner("Working on it..."):
                response, status_code = APIInterface.post(
                    route=route,
                    data=data,
                    headers={"Authorization": token},
                )
            st.success("Done!")
            st.json(response)
    storage_id = st.number_input("Storage Id", min_value=0)
    sync_data_bool = st.button(label="Sync Data", key="sync_data")
    if sync_data_bool:
        if st.session_state.cloud_service_provider == "aws":
            route = f"{DATA_HUB}/label_studio/sync_s3_storage"
        elif st.session_state.cloud_service_provider == "gcp":
            route = f"{DATA_HUB}/label_studio/sync_gcs_storage"
        with st.spinner("Working on it..."):
            response, status_code = APIInterface.post(
                route=route,
                data={"storage_id": storage_id},
                headers={"Authorization": token},
            )
        st.success("Done!")
        st.json(response)
    st.write("[Proceed to Data Annotation](http://0.0.0.0:8080)")

with st.beta_expander("Step 3: Export/Transform Annotations (Optional)"):
    token_obj = json.load(open("token.json", "r"))
    token = token_obj.get("token")
    st.subheader("Manage Annotations")
    function = st.selectbox("Action", options=("Export", "Transform"))
    if function == "Export":
        with st.form("export_annotations"):
            st.subheader("Export Annotations")
            pipeline_id = st.number_input("Pipeline ID", min_value=0)
            project_id = st.number_input("Annotation Project Id", min_value=0)
            service_provider = st.session_state["cloud_service_provider"]
            bucket_name = st.text_input("Output Bucket Name")
            submitted = st.form_submit_button("Export Annotations")
            if submitted:
                with st.spinner("Working on it..."):
                    response, status_code = APIInterface.get(
                        route=f"{DATA_HUB}/label_studio/export_annotations",
                        params={
                            "pipeline_id": pipeline_id,
                            "project_id": project_id,
                            "service_provider": service_provider,
                            "bucket_name": bucket_name,
                        },
                        headers={"Authorization": token},
                    )
                st.success("Done!")
                st.json(response)
    else:
        with st.form("transform_annotations"):
            st.subheader("Transform Annotations")
            service_provider = st.session_state["cloud_service_provider"]
            pipeline_id = st.number_input("Pipeline ID", min_value=0)
            input_data_s3_uri = st.text_input("Exported Annotations File Path")
            output_data_s3_bucket = st.text_input("Output Data Bucket")
            output_data_s3_prefix = st.text_input("Folder Name")
            submitted = st.form_submit_button("Transform Annotations")
            if submitted:
                with st.spinner("Working on it..."):
                    response, status_code = APIInterface.post(
                        route=f"{DATA_HUB}/label_studio/transform_annotations",
                        data={
                            "pipeline_id": pipeline_id,
                            "input_data_uri": input_data_s3_uri,
                            "output_data_bucket_name": output_data_s3_bucket,
                            "output_data_file_prefix": output_data_s3_prefix,
                            "service_provider": service_provider,
                        },
                        headers={"Authorization": token},
                    )
                st.success("Done!")
                st.json(response)

with st.beta_expander("Step 4: Train Model"):
    token_obj = json.load(open("token.json", "r"))
    token = token_obj.get("token")
    cloud_service_provider = st.session_state.cloud_service_provider
    if "use_case" not in st.session_state:
        use_case = "image_classification"
    else:
        use_case = st.session_state["use_case"]
    response, status_code = APIInterface.get(
        route=f"{DATA_HUB}/osairis/services/by_cloud_and_use_case",
        params={
            "cloud_service_provider": cloud_service_provider,
            "use_case": use_case,
        },
        headers={"Authorization": token},
    )
    service_name = response.get("service_name")
    if service_name == "rekognition":
        with st.form("train_rekog_model"):
            st.subheader("Create Rekognition Model")
            pipeline_id = st.number_input("Pipeline ID", min_value=0)
            project_name = st.text_input("Project Name")
            version_name = st.text_input("Model Name")
            s3_bucket = st.text_input("Output Bucket Name")
            s3_key_prefix = st.text_input("Folder Name")
            manifest_bucket = st.text_input("Manifest Bucket Name")
            manifest_file_path = st.text_input("Manifest File Path")
            route = f"{DATA_HUB}/aws/rekog/create_project"
            data = {
                "pipeline_id": int(pipeline_id),
                "project_name": project_name,
            }
            submitted = st.form_submit_button("Create Model")
            if submitted:
                with st.spinner("Working on it..."):
                    response, status_code = APIInterface.post(
                        route=route,
                        data=data,
                        headers={"Authorization": token},
                    )
                    response, status_code = APIInterface.post(
                        route=f"{DATA_HUB}/aws/rekog/start_training",
                        data={
                            "pipeline_id": pipeline_id,
                            "project_arn": response.get("project_arn"),
                            "version_name": version_name,
                            "output_config": {
                                "S3Bucket": s3_bucket,
                                "S3KeyPrefix": s3_key_prefix,
                            },
                            "training_data": {
                                "Assets": [
                                    {
                                        "GroundTruthManifest": {
                                            "S3Object": {
                                                "Bucket": manifest_bucket,
                                                "Name": manifest_file_path,
                                            }
                                        }
                                    }
                                ]
                            },
                            "testing_data": {
                                "AutoCreate": True,
                            },
                        },
                        headers={"Authorization": token},
                    )
                st.success("Done!")
                st.json(response)
    elif service_name == "comprehend":
        if use_case == "text_classification":
            with st.form("train_comprehend_model"):
                st.subheader("Create Comprehend Model")
                pipeline_id = st.number_input("Pipeline ID", min_value=0)
                DocumentClassifierName = st.text_input("Model Name")
                DataAccessRoleArn = st.text_input("AWS Role ARN")
                s3_bucket = st.text_input("Output Bucket Name")
                manifest_file_path = st.text_input("Manifest File Path")
                mode = st.selectbox("Type of Model", {"MULTI_CLASS", "MULTI_LABEL"})
                submitted = st.form_submit_button("Create Model")
                if submitted:
                    with st.spinner("Working on it..."):
                        response, status_code = APIInterface.post(
                            route=f"{DATA_HUB}/aws/comprehend/create_document_classifier",
                            data={
                                "pipeline_id": pipeline_id,
                                "DocumentClassifierName": DocumentClassifierName,
                                "DataAccessRoleArn": DataAccessRoleArn,
                                "InputDataConfig": {
                                    "DataFormat": "AUGMENTED_MANIFEST",
                                    "AugmentedManifests": [
                                        {"S3Uri": manifest_file_path}
                                    ],
                                },
                                "OutputDataConfig": {"S3Uri": s3_bucket},
                                "LanguageCode": "en",
                                "Mode": mode,
                            },
                            headers={"Authorization": token},
                        )
                    st.success("Done!")
                    st.json(response)
        elif use_case == "natural_entity_recognition":
            with st.form("train_comprehend_ner_model"):
                st.subheader("Create Comprehend Model")
                pipeline_id = st.number_input("Pipeline ID", min_value=0)
                RecognizerName = st.text_input("Model Name")
                DataAccessRoleArn = st.text_input("AWS Role ARN")
                manifest_file_path = st.text_input("Manifest File Path")
                submitted = st.form_submit_button("Create Model")
                if submitted:
                    with st.spinner("Working on it..."):
                        response, status_code = APIInterface.post(
                            route=f"{DATA_HUB}/aws/comprehend/create_document_classifier",
                            data={
                                "pipeline_id": pipeline_id,
                                "RecognizerName": RecognizerName,
                                "DataAccessRoleArn": DataAccessRoleArn,
                                "InputDataConfig": {
                                    "DataFormat": "AUGMENTED_MANIFEST",
                                    "AugmentedManifests": [
                                        {
                                            "S3Uri": manifest_file_path,
                                        }
                                    ],
                                },
                                "LanguageCode": "en",
                            },
                            headers={"Authorization": token},
                        )
                    st.success("Done!")
                    st.json(response)
    elif service_name == "automl":
        with st.form("import_automl_dataset"):
            st.subheader("Import AutoML Dataset")
            pipeline_id = st.number_input("Pipeline ID", min_value=0)
            project_id = st.text_input("Project Name")
            dataset_name = st.text_input("Dataset Name")
            gcs_path = st.text_input("Annotation File Path")
            region = st.selectbox("Region to Train your Model in", ("us-central1"))
            mode = st.selectbox("Type of Model", ("MULTI_LABEL", "MULTI_CLASS", "N.A"))
            if mode == "MULTI_CLASS":
                multi_label = False
            else:
                multi_label = True
            if use_case == "image_classification":
                route = f"{DATA_HUB}/gcp/automl/create_image_classification_dataset"
                data = {
                    "pipeline_id": pipeline_id,
                    "project_id": project_id,
                    "display_name": dataset_name,
                    "region": region,
                    "multi_label": multi_label,
                }
            elif use_case == "text_classification":
                route = f"{DATA_HUB}/gcp/automl/create_text_classification_dataset"
                data = {
                    "pipeline_id": pipeline_id,
                    "project_id": project_id,
                    "display_name": dataset_name,
                    "region": region,
                    "multi_label": multi_label,
                }
            elif use_case == "object_detection":
                route = f"{DATA_HUB}/gcp/automl/create_object_detection_dataset"
                data = {
                    "pipeline_id": pipeline_id,
                    "project_id": project_id,
                    "display_name": dataset_name,
                    "region": region,
                }
            elif use_case == "natural_entity_recognition":
                route = f"{DATA_HUB}/gcp/automl/create_ner_dataset"
                data = {
                    "pipeline_id": pipeline_id,
                    "project_id": project_id,
                    "display_name": dataset_name,
                    "region": region,
                }
            submitted = st.form_submit_button("Import Dataset")
            if submitted:
                with st.spinner("Working on it..."):
                    response, status_code = APIInterface.post(
                        route=route,
                        data=data,
                        headers={"Authorization": token},
                    )
                    dataset_id = response.get("dataset_id")
                    final_response = import_dataset(
                        token=token,
                        project_id=project_id,
                        dataset_id=dataset_id,
                        gcs_path=gcs_path,
                        region=region,
                    )
                st.success("Done!")
                st.json(final_response)
        with st.form("train_automl_model"):
            st.subheader("Train AutoML Model")
            pipeline_id = st.number_input("Pipeline ID", min_value=0)
            project_id = st.text_input("Project Name")
            dataset_id = st.text_input("Dataset ID")
            model_name = st.text_input("Model Name")
            region = st.selectbox("Region to Train your Model in", ("us-central1"))
            data = {
                "pipeline_id": pipeline_id,
                "project_id": project_id,
                "model_display_name": model_name,
                "region": region,
                "dataset_id": dataset_id,
            }
            if use_case == "image_classification":
                route = f"{DATA_HUB}/gcp/automl/train_image_classification_model"
            elif use_case == "text_classification":
                route = f"{DATA_HUB}/gcp/automl/train_text_classification_model"
            elif use_case == "object_detection":
                route = f"{DATA_HUB}/gcp/automl/train_object_detection_model"
            elif use_case == "natural_entity_recognition":
                route = f"{DATA_HUB}/gcp/automl/train_ner_model"
            submitted = st.form_submit_button("Train Model")
            if submitted:
                with st.spinner("Working on it..."):
                    response, status_code = APIInterface.post(
                        route=route,
                        data=data,
                        headers={"Authorization": token},
                    )
                st.success("Done!")
                st.json(response)

with st.beta_expander("Step 5: Deploy Model"):
    token_obj = json.load(open("token.json", "r"))
    token = token_obj.get("token")
    cloud_service_provider = st.session_state.cloud_service_provider
    if "use_case" not in st.session_state:
        use_case = "image_classification"
    else:
        use_case = st.session_state["use_case"]
    response, status_code = APIInterface.get(
        route=f"{DATA_HUB}/osairis/services/by_cloud_and_use_case",
        params={
            "cloud_service_provider": cloud_service_provider,
            "use_case": use_case,
        },
        headers={"Authorization": token},
    )
    service_name = response.get("service_name")
    if cloud_service_provider == "aws":
        if service_name == "rekognition":
            with st.form("manage_rekognition_model"):
                st.subheader("Manage Rekognition Model")
                pipeline_id = st.number_input("Pipeline ID", min_value=0)
                model_id = st.text_input("Model ARN")
                min_inference_units = st.selectbox(
                    "Minimum Inference Units", ("1", "2", "3", "4")
                )
                manage_model = st.selectbox("Model Action", ("DEPLOY", "UN_DEPLOY"))
                if manage_model == "DEPLOY":
                    route = f"{DATA_HUB}/aws/comprehend/deploy_model"
                    data = {
                        "pipeline_id": int(pipeline_id),
                        "project_version_arn": model_id,
                        "min_inference_units": int(min_inference_units),
                    }
                elif manage_model == "UN_DEPLOY":
                    route = f"{DATA_HUB}/aws/comprehend/undeploy_model"
                    data = {
                        "pipeline_id": int(pipeline_id),
                        "project_version_arn": model_id,
                    }
                submitted = st.form_submit_button("Submit")
                if submitted:
                    with st.spinner("Working on it..."):
                        response, status_code = APIInterface.post(
                            route=route,
                            data=data,
                            headers={"Authorization": token},
                        )
                    st.success("Done!")
                    st.json(response)
        elif service_name == "comprehend":
            with st.form("manage_comprehend_model"):
                st.subheader("Manage Comprehend Model")
                pipeline_id = st.number_input("Pipeline ID", min_value=0)
                endpoint_name = st.text_input("Endpoint Name or ARN")
                model_id = st.text_input("Model ARN")
                min_inference_units = st.selectbox(
                    "Minimum Inference Units", ("1", "2", "3", "4")
                )
                manage_model = st.selectbox("Model Action", ("DEPLOY", "UN_DEPLOY"))
                if manage_model == "DEPLOY":
                    route = f"{DATA_HUB}/aws/comprehend/deploy_model"
                    data = {
                        "pipeline_id": int(pipeline_id),
                        "endpoint_name": endpoint_name,
                        "model_arn": model_id,
                        "min_inference_units": int(min_inference_units),
                    }
                elif manage_model == "UN_DEPLOY":
                    route = f"{DATA_HUB}/aws/comprehend/undeploy_model"
                    data = {
                        "pipeline_id": int(pipeline_id),
                        "endpoint_name": endpoint_name,
                    }
                submitted = st.form_submit_button("Submit")
                if submitted:
                    with st.spinner("Working on it..."):
                        response, status_code = APIInterface.post(
                            route=route,
                            data=data,
                            headers={"Authorization": token},
                        )
                    st.success("Done!")
                    st.json(response)
    elif cloud_service_provider == "gcp":
        with st.form("manage_automl_model"):
            st.subheader("Manage AutoML Model")
            pipeline_id = st.number_input("Pipeline ID", min_value=0)
            project_id = st.text_input("Project Name")
            model_id = st.text_input("Model ID")
            region = st.selectbox("Region to Train your Model in", ("us-central1"))
            manage_model = st.selectbox("Model Action", ("DEPLOY", "UN_DEPLOY"))
            data = {
                "pipeline_id": pipeline_id,
                "project_id": project_id,
                "model_id": model_id,
                "region": region,
            }
            if manage_model == "DEPLOY":
                route = f"{DATA_HUB}/gcp/automl/deploy_model"
            elif manage_model == "UN_DEPLOY":
                route = f"{DATA_HUB}/gcp/automl/undeploy_model"
            submitted = st.form_submit_button("Submit")
            if submitted:
                with st.spinner("Working on it..."):
                    response, status_code = APIInterface.post(
                        route=route,
                        data=data,
                        headers={"Authorization": token},
                    )
                st.success("Done!")
                st.json(response)
