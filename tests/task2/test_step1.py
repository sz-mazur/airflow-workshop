import pytest
from airflow.models import DagBag

from tests.helper.connection import HTTP_STATUS_OK, get_response_from_api
from tests.task2 import config


@pytest.mark.airflow_required
def test_dag_loaded() -> None:
    dags = DagBag().dags.values()
    for dag in dags:
        assert len(dag.tasks) > 0
        assert dag is not None


@pytest.mark.airflow_required
def test_exist_task2_dag() -> None:
    dag_status = get_response_from_api(config.DAG_URI, True).status_code
    assert HTTP_STATUS_OK == dag_status


@pytest.mark.airflow_required
def test_settings_dag() -> None:
    dag_response = get_response_from_api(config.DAG_URI + "/details", True).json()
    output = {
        "dag_id": dag_response["dag_id"],
        "start_date": dag_response["start_date"],
        "schedule": dag_response["schedule_interval"]["value"],
        "tags": dag_response["tags"],
    }
    assert config.EXCEPTED_SETTINGS == output


@pytest.mark.airflow_required
def test_task2_operators_type() -> None:
    task_mean_response = get_response_from_api(config.MEAN_TASK_URI, True).json()
    task_max_response = get_response_from_api(config.MAX_TASK_URI, True).json()

    assert "PythonOperator" == task_mean_response["operator_name"]
    assert "templates_dict" in task_mean_response["template_fields"]

    assert "PythonOperator" == task_max_response["operator_name"]
    assert "templates_dict" in task_max_response["template_fields"]


@pytest.mark.airflow_required
def test_tasks_dependency() -> None:
    task_mean_response = get_response_from_api(config.MEAN_TASK_URI, True).json()["downstream_task_ids"]
    task_max_response = get_response_from_api(config.MAX_TASK_URI, True).json()["downstream_task_ids"]

    assert "max_revenue" not in task_mean_response
    assert "mean_revenue" not in task_max_response
