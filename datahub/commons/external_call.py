import requests
import json
from sql import logger

logging = logger(__name__)


class APIInterface:
    @staticmethod
    def post(route, data=None, headers=None):
        try:
            url = route
            logging.info("POST request sent")
            logging.debug(f"url = {url}, data = {data}")
            response = requests.post(url, json=data, headers=headers)
            if response.status_code >= 400:
                raise Exception(
                    f"Call to {route} failed with {response.status_code} and response {response.text}"
                )
            return json.loads(response.text), response.status_code
        except Exception as error:
            logging.error(f"Error in POST API request: {error}")

    @staticmethod
    def get(route, params=None, headers=None):
        try:
            url = route
            logging.info("GET request sent")
            logging.debug(f"url = {url}, params = {params}")
            response = requests.get(url, params=params, headers=headers)
            if response.status_code >= 400:
                raise Exception(
                    f"Call to {route} failed with {response.status_code} and response {response.text}"
                )
            return json.loads(response.text), response.status_code
        except Exception as error:
            logging.error(f"Error in GET API request: {error}")

    @staticmethod
    def put(route, data=None, headers=None):
        try:
            url = route
            logging.info("PUT request sent")
            logging.debug(f"url = {url}, data = {data}")
            response = requests.put(url, json=data, headers=headers)
            if response.status_code >= 400:
                raise Exception(
                    f"Call to {route} failed with {response.status_code} and response {response.text}"
                )
            return json.loads(response.text), response.status_code
        except Exception as error:
            logging.error(f"Error in PUT API request: {error}")

    @staticmethod
    def delete(route, headers=None):
        try:
            url = route
            logging.info("DELETE request sent")
            logging.debug(f"url = {url}")
            response = requests.delete(url, headers=headers)
            if response.status_code >= 400:
                raise Exception(
                    f"Call to {route} failed with {response.status_code} and response {response.text}"
                )
            return response.status_code
        except Exception as error:
            logging.error(f"Error in DELETE API request: {error}")
