import streamlit as st
from external_call import APIInterface
from s3_helper import upload_file_obj
import os
import json

IP = os.environ.get("IP", "192.168.1.100")
st.title("osAIris")
DATA_HUB = f"http://{IP}:7000"
token_obj = json.load(open("token.json", "r"))
token = token_obj.get("token")
st.header("AI Engineering")
with st.form("create_rekognition_project"):
    st.write("Create Rekognition Project")
    project_name = st.text_input("Project Name")
    submitted = st.form_submit_button("Create Rekognition Project")
    if submitted:
        with st.spinner("Working on it..."):
            response, status_code = APIInterface.post(
                route=f"{DATA_HUB}/aws/rekog/create_project",
                data={"project_name": project_name},
                headers={"Authorization": token},
            )
        st.success("Done!")
        st.json(response)

with st.form("start_training"):
    st.write("Start Training")
    project_arn = st.text_input("Project ARN")
    version_name = st.text_input("Model Alias")
    st.text("Output Bucket Config")
    s3_bucket = st.text_input("S3 Bucket Name")
    s3_key_prefix = st.text_input("S3 Folder Path")
    st.text("Annotation Config")
    manifest_bucket = st.text_input("Manifest S3 Bucket Name")
    manifest_file_path = st.text_input("Manifest File Path")
    submitted = st.form_submit_button("Start Training")
    if submitted:
        with st.spinner("Working on it..."):
            response, status_code = APIInterface.post(
                route=f"{DATA_HUB}/aws/rekog/start_training",
                data={
                    "project_arn": project_arn,
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

with st.form("get_project_description"):
    st.write("Get Project Description")
    project_arn = st.text_input("Project ARN")
    submitted = st.form_submit_button("Get Description")
    if submitted:
        with st.spinner("Working on it..."):
            response, status_code = APIInterface.get(
                route=f"{DATA_HUB}/aws/rekog/get_project_description",
                params={"project_arn": project_arn},
                headers={"Authorization": token},
            )
        st.success("Done!")
        st.json(response)

with st.form("deploy_model"):
    st.write("Deploy")
    project_version_arn = st.text_input("Project Version ARN")
    min_inference_units = st.text_input("Minimum Inference Units")
    submitted = st.form_submit_button("Deploy")
    if submitted:
        with st.spinner("Working on it..."):
            response, status_code = APIInterface.post(
                route=f"{DATA_HUB}/aws/rekog/deploy_model",
                data={
                    "project_version_arn": project_version_arn,
                    "min_inference_units": int(min_inference_units),
                },
                headers={"Authorization": token},
            )
        st.success("Done!")
        st.json(response)

with st.form("un_deploy_model"):
    st.write("Un-Deploy")
    project_version_arn = st.text_input("Project Version ARN")
    submitted = st.form_submit_button("Un-Deploy")
    if submitted:
        with st.spinner("Working on it..."):
            response, status_code = APIInterface.post(
                route=f"{DATA_HUB}/aws/rekog/undeploy_model",
                data={
                    "project_version_arn": project_version_arn,
                },
                headers={"Authorization": token},
            )
        st.success("Done!")
        st.json(response)

with st.form("get_predictions"):
    st.write("Get Predictions")
    uploaded_file = st.file_uploader("Select a file")
    project_version_arn = st.text_input("Project Version ARN")
    submitted = st.form_submit_button("Predict")
    if submitted:
        with st.spinner("Working on it..."):
            bytes_data = uploaded_file.getvalue()
            s3_uri = upload_file_obj(file_data=bytes_data)
            print(f"{s3_uri=}")
            response, status_code = APIInterface.get(
                route=f"{DATA_HUB}/aws/rekog/get_predictions",
                params={
                    "project_version_arn": project_version_arn,
                    "s3_uri": s3_uri,
                },
                headers={"Authorization": token},
            )
        st.success("Done!")
        st.json(response)
