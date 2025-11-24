import requests

class ApiClient:

    def __init__(self, base_url="https://reqres.in/api"):
        self.base_url = base_url.rstrip("/")

    def get(self, path: str, **kwargs):
        url = self.base_url + path
        return requests.get(url, **kwargs)

    def post(self, path: str, json=None, **kwargs):
        url = self.base_url + path
        return requests.post(url, json=json, **kwargs)

    def put(self, path: str, json=None, **kwargs):
        url = self.base_url + path
        return requests.put(url, json=json, **kwargs)

    def patch(self, path: str, json=None, **kwargs):
        url = self.base_url + path
        return requests.patch(url, json=json, **kwargs)

    def delete(self, path: str, **kwargs):
        url = self.base_url + path
        return requests.delete(url, **kwargs)
