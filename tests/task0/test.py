import pytest

from tests.helper.connection import (
    HTTP_STATUS_OK,
    HTTP_STATUS_UNAUTHORIZED,
    get_response_from_api,
    get_response_from_ui,
)


@pytest.mark.airflow_required
def test_server_connection() -> None:
    assert HTTP_STATUS_OK == get_response_from_ui().status_code


@pytest.mark.airflow_required
def test_server_healthy() -> None:
    response = get_response_from_api("health").json()
    assert "healthy" == response["metadatabase"]["status"] and "healthy" == response["scheduler"]["status"]


@pytest.mark.airflow_required
def test_airflow_version() -> None:
    response = get_response_from_api("version").json()
    assert "2.5.0" == response["version"]


@pytest.mark.airflow_required
def test_fail_authentication() -> None:
    response = get_response_from_api("dags").status_code
    assert HTTP_STATUS_UNAUTHORIZED == response


@pytest.mark.airflow_required
def test_correct_authentication() -> None:
    response = get_response_from_api("dags", True).status_code
    assert HTTP_STATUS_OK == response


@pytest.mark.airflow_required
def test_empty_dags_list() -> None:
    response = get_response_from_api("dags", True).json()
    assert 0 == response["total_entries"]
