import pytest

from tests.helper.connection import get_response_from_api
from tests.task2 import config


@pytest.mark.airflow_required
def test_file_sensor_type() -> None:
    file_sensor_response = get_response_from_api(config.WAITING_FOR_TASK_URI, True).json()["operator_name"]

    assert "FileSensor" == file_sensor_response


@pytest.mark.airflow_required
def test_file_sensor_id() -> None:
    file_sensor_response = get_response_from_api(config.WAITING_FOR_TASK_URI, True).json()["task_id"]

    assert "waiting_for_data" == file_sensor_response


@pytest.mark.airflow_required
def test_file_sensor_field() -> None:
    file_sensor_response = get_response_from_api(config.WAITING_FOR_TASK_URI, True).json()["template_fields"]

    assert "filepath" in file_sensor_response


@pytest.mark.airflow_required
def test_file_sensor_dependency() -> None:
    file_sensor_response = get_response_from_api(config.WAITING_FOR_TASK_URI, True).json()["downstream_task_ids"]

    assert "max_revenue" in file_sensor_response
    assert "mean_revenue" in file_sensor_response
