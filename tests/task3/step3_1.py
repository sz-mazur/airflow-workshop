import pytest

from tests.helper.connection import HTTP_STATUS_OK, get_response_from_api
from tests.task3 import config


@pytest.mark.airflow_required
def test_exist_dag_step_3_1() -> None:
    dag_status = get_response_from_api(config.DAG_URI_3_1, True).status_code
    assert HTTP_STATUS_OK == dag_status


@pytest.mark.airflow_required
def test_settings_dag_step_3_1() -> None:
    dag_response = get_response_from_api(config.DAG_URI_3_1 + "/details", True).json()

    assert config.DAG_NAME_STEP3_1 == dag_response["dag_id"]
    assert config.SCHEDULE == dag_response["schedule_interval"]["value"]
    assert config.TAGS_STEP3 == dag_response["tags"]


@pytest.mark.airflow_required
def test_max_active_dag_step_3_1() -> None:
    dag_response = get_response_from_api(config.DAG_URI_3_1 + "/details", True).json()
    assert config.MAX_ACTIVE_TASKS == dag_response["max_active_tasks"]
