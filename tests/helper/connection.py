import json
from typing import Optional

import requests

from config import config

HTTP_STATUS_OK = 200
HTTP_STATUS_UNAUTHORIZED = 401


def get_response_from_url(url: str, login: bool = False) -> requests.Response:
    if login:
        return requests.get(url=url, auth=config.AUTH)
    return requests.get(url=url)


def get_response_from_ui(endpoint: str = "", login: bool = False) -> requests.Response:
    return get_response_from_url(config.URL_AIRFLOW_UI + endpoint, login)


def get_response_from_api(endpoint: str = "", login: bool = False) -> requests.Response:
    return get_response_from_ui(config.API_PATH + endpoint, login)


def post_to_api(
    endpoint: str = "",
    headers: Optional[dict[str, str]] = None,
    data: Optional[dict[str, dict]] = None,
) -> requests.Response:
    if data is None:
        data = dict()
    if headers is None:
        headers = dict()
    return requests.post(
        url=config.URL_AIRFLOW_API + endpoint,
        data=json.dumps(data),
        headers=headers,
        auth=config.AUTH,
    )
