import pytest
import requests

from project_spider.request_utils import get_session

def test_session_a_successful_url_and_success():
    s = get_session()
    response = s.get("https://postman-echo.com/status/200")
    assert response.status_code == 200


def test_session_a_non_existing_url_n_times_and_fails(caplog):
    s = get_session()
    with pytest.raises(requests.exceptions.ConnectionError):
        s.get("http://this-url-does-not-exist.bar")

    assert "Retry(total=0, connect=None, read=None, redirect=None, status=None)" in caplog.records[2].message
    assert "Retry(total=1, connect=None, read=None, redirect=None, status=None)" in caplog.records[1].message
    assert "Retry(total=2, connect=None, read=None, redirect=None, status=None)" in caplog.records[0].message
