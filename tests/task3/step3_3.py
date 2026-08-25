import pytest

from tests.helper.connection import HTTP_STATUS_OK, get_response_from_api
from tests.task3 import config


@pytest.mark.airflow_required
def test_exist_dag_step_3_3() -> None:
    dag_status = get_response_from_api(config.DAG_URI_3_3, True).status_code
    assert HTTP_STATUS_OK == dag_status


@pytest.mark.airflow_required
def test_settings_dag_step_3_3() -> None:
    dag_response = get_response_from_api(config.DAG_URI_3_3 + "/details", True).json()

    assert config.DAG_NAME_STEP3_3 == dag_response["dag_id"]
    assert config.SCHEDULE == dag_response["schedule_interval"]["value"]
    assert config.TAGS_STEP3 == dag_response["tags"]


@pytest.mark.airflow_required
def test_max_active_tasks_dag_step_3_3() -> None:
    dag_response = get_response_from_api(config.DAG_URI_3_3 + "/details", True).json()
    assert config.MAX_ACTIVE_TASKS == dag_response["max_active_tasks"]


@pytest.mark.airflow_required
def test_max_active_runs_dag_step_3_3() -> None:
    dag_response = get_response_from_api(config.DAG_URI_3_3 + "/details", True).json()
    assert config.MAX_ACTIVE_RUNS == dag_response["max_active_runs"]


@pytest.mark.airflow_required
def test_task_dependency_step_3_3() -> None:
    depends_on_past = True

    for i in range(10):
        if i == config.SWITCH_DEPENDENCY_AT_INDEX:
            depends_on_past = False
        response = get_response_from_api(config.DAG_URI_3_3 + "/tasks/auto_generated_" + str(i), True).json()
        assert depends_on_past == response["depends_on_past"]
