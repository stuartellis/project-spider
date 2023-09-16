from dataclasses import dataclass
from typing import List

import pytest
import requests

from project_spider.gitlab_api_service import GitLabAPIService
from project_spider.request_utils import get_session

class APIRequestError(ValueError):
    pass


@dataclass(frozen=True)
class GitLabUser:
    id: int
    email: str
    first_name: str
    last_name: str
    avatar: str


class GitLabDataGenerator(object):
    all_users: List[GitLabUser] = []

    def __init__(self, api_service):
        self.api_service = api_service
        for user in api_service.get_all_users():
            self.all_users.append(GitLabUser(**user))

    def get_total_users(self):
        return len(self.all_users)

_api_service = GitLabAPIService(get_session())
_generator = GitLabDataGenerator(_api_service)

@pytest.fixture
def a_dummy_api_service():
    return _api_service


@pytest.fixture
def a_dummy_generator():
    return _generator


def test_request_a_url_without_timeout_successfully():
    response = requests.get('https://postman-echo.com/status/200')
    assert response.status_code == 200


def test_request_a_url_with_infinite_timeout():
    response = requests.get('https://postman-echo.com/delay/10', timeout=None)
    assert response.status_code == 200


def test_request_a_url_with_a_long_timeout_successfully():
    response = requests.get('https://postman-echo.com/status/200', timeout=5)
    assert response.status_code == 200


def test_request_a_url_with_a_very_short_timeout_and_fails():
    with pytest.raises(requests.exceptions.Timeout):
        requests.get('https://postman-echo.com/status/200', timeout=0.001)


def test_get_a_url_with_response_status_500(a_dummy_api_service):
    endpoint_url = "https://postman-echo.com/status/500"

    with pytest.raises(requests.exceptions.RetryError):
        a_dummy_api_service.request_session.get(endpoint_url, timeout=2)


def test_get_all_users_successfully(a_dummy_generator):
    assert a_dummy_generator.get_total_users() == 6
