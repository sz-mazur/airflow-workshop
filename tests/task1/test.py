import time

import pytest

from tests.helper.connection import HTTP_STATUS_OK, get_response_from_api, post_to_api
from tests.task1 import config


@pytest.mark.airflow_required
def test_exist_example_dag() -> None:
    response = get_response_from_api("dags/example_dag", True).status_code
    assert HTTP_STATUS_OK == response


@pytest.mark.airflow_required
def test_tasks_example_dag() -> None:
    response = get_response_from_api("dags/example_dag/tasks", True)
    tasks_count = response.json()["total_entries"]
    assert HTTP_STATUS_OK == response.status_code
    assert config.TASK_COUNT == tasks_count


@pytest.mark.airflow_required
def test_run_example_dag() -> None:
    data = {
        "conf": {"name": "Test"},
    }
    headers = {"Content-type": "application/json"}
    response_post = post_to_api("dags/example_dag/dagRuns", headers, data).json()
    run_id = response_post["dag_run_id"]
    response_post_state = response_post["state"]
    time.sleep(30)
    response_get = get_response_from_api("dags/example_dag/dagRuns/" + run_id, True).json()
    response_get_state = response_get["state"]
    assert "queued" == response_post_state
    assert "success" == response_get_state
