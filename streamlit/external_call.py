import requests
import json


class APIInterface:
    @staticmethod
    def post(route, data=None, headers=None):
        url = route
        print(f"url = {url}, data = {data}")
        response = requests.post(url, json=data, headers=headers)
        if response.status_code >= 400:
            raise Exception(
                f"Call to {route} failed with {response.status_code} and response {response.text}"
            )
        return json.loads(response.text), response.status_code

    def post_form(route, data=None, headers=None):
        url = route
        print(f"url = {url}, data = {data}")
        response = requests.post(url, data=data, headers=headers)
        if response.status_code >= 400:
            raise Exception(
                f"Call to {route} failed with {response.status_code} and response {response.text}"
            )
        return json.loads(response.text), response.status_code

    @staticmethod
    def get(route, params=None, headers=None):
        url = route
        print(f"url = {url}, params = {params}")
        response = requests.get(url, params=params, headers=headers)
        if response.status_code >= 400:
            raise Exception(
                f"Call to {route} failed with {response.status_code} and response {response.text}"
            )
        return json.loads(response.text), response.status_code

    @staticmethod
    def put(route, data=None, headers=None):
        url = route
        print(f"url = {url}, data = {data}")
        response = requests.put(url, json=data, headers=headers)
        if response.status_code >= 400:
            raise Exception(
                f"Call to {route} failed with {response.status_code} and response {response.text}"
            )
        return json.loads(response.text), response.status_code

    @staticmethod
    def delete(route, headers=None):
        url = route
        print(f"url = {url}")
        response = requests.delete(url, headers=headers)
        if response.status_code >= 400:
            raise Exception(
                f"Call to {route} failed with {response.status_code} and response {response.text}"
            )
        return response.status_code
