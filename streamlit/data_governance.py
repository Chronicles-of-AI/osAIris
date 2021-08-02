from fastapi import params
import streamlit as st
from external_call import APIInterface
import os
import json

IP = os.environ.get("IP", "192.168.1.100")
st.title("SynapSe")
DATA_HUB = f"http://{IP}:7000"
token = None
st.header("Authentication")
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
                    # "grant_type": None,
                    # "client_id": None,
                    # "client_secret": None,
                },
            )
        # st.success("Done!")
        # st.json(response)
        token = response.get("access_token")
        with open("token.json", "w+") as f:
            json.dump({"token": f"Bearer {token}"}, f)
        st.json({"status": "User Authenticated"})
st.header("Data Governance")
with st.form("create_annotation_project"):
    token_obj = json.load(open("token.json", "r"))
    token = token_obj.get("token")
    st.write("Create Annotation Project")
    annotation_project_name = st.text_input("Project Name")
    project_description = st.text_input("Project Description")
    submitted = st.form_submit_button("Create Project")
    if submitted:
        with st.spinner("Working on it..."):
            response, status_code = APIInterface.post(
                route=f"{DATA_HUB}/label_studio/create_project",
                data={
                    "title": annotation_project_name,
                    "description": project_description,
                },
                headers={"Authorization": token},
            )
        st.success("Done!")
        st.json(response)

with st.form("attach_storage"):
    token_obj = json.load(open("token.json", "r"))
    token = token_obj.get("token")
    st.write("Attach Storage")
    project_id = st.text_input("Project Id")
    storage_name = st.text_input("Storage Name")
    bucket_name = st.text_input("Bucket Name")
    submitted = st.form_submit_button("Attach Storage")
    if submitted:
        with st.spinner("Working on it..."):
            response, status_code = APIInterface.post(
                route=f"{DATA_HUB}/label_studio/create_s3_storage",
                data={
                    "project": project_id,
                    "title": storage_name,
                    "bucket": bucket_name,
                    "description": storage_name,
                    "region_name": "us-east-2",
                },
                headers={"Authorization": token},
            )
        st.success("Done!")
        st.json(response)

with st.form("sync_storage"):
    token_obj = json.load(open("token.json", "r"))
    token = token_obj.get("token")
    st.write("Sync Storage")
    storage_id = st.text_input("Storage Id")
    submitted = st.form_submit_button("Sync Storage")
    if submitted:
        with st.spinner("Working on it..."):
            response, status_code = APIInterface.post(
                route=f"{DATA_HUB}/label_studio/sync_s3_storage",
                data={"storage_id": storage_id},
                headers={"Authorization": token},
            )
        st.success("Done!")
        st.json(response)

with st.form("export_annotations"):
    token_obj = json.load(open("token.json", "r"))
    token = token_obj.get("token")
    st.write("Export Annotations")
    project_id = st.text_input("Project Id")
    service_provider = st.radio("Service Provider", ("aws", "gcp"))
    bucket_name = st.text_input("Bucket Name")
    submitted = st.form_submit_button("Export Annotations")
    if submitted:
        with st.spinner("Working on it..."):
            response, status_code = APIInterface.get(
                route=f"{DATA_HUB}/label_studio/export_annotations",
                params={
                    "project_id": project_id,
                    "service_provider": service_provider,
                    "bucket_name": bucket_name,
                },
                headers={"Authorization": token},
            )
        st.success("Done!")
        st.json(response)

with st.form("transform_annotations"):
    token_obj = json.load(open("token.json", "r"))
    token = token_obj.get("token")
    st.write("Transform Annotations")
    service_provider = st.radio("Service Provider", ("aws", "gcp"))
    input_data_s3_uri = st.text_input("Input Data S3 URI")
    output_data_s3_bucket = st.text_input("Output Data S3 Bucket")
    output_data_s3_prefix = st.text_input("Output Data S3 Prefix")
    submitted = st.form_submit_button("Transform Annotations")
    if submitted:
        with st.spinner("Working on it..."):
            response, status_code = APIInterface.post(
                route=f"{DATA_HUB}/label_studio/transform_annotations",
                data={
                    "input_data_uri": input_data_s3_uri,
                    "output_data_bucket_name": output_data_s3_bucket,
                    "output_data_file_prefix": output_data_s3_prefix,
                    "service_provider": service_provider,
                },
                headers={"Authorization": token},
            )
        st.success("Done!")
        st.json(response)
