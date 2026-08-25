from typing import cast

import pytest
from pendulum import parser
from pendulum.datetime import DateTime

from tests.helper.connection import HTTP_STATUS_OK, get_response_from_api
from tests.task3 import config


@pytest.mark.airflow_required
def test_exist_dag_step_1_2() -> None:
    dag_status = get_response_from_api(config.DAG_URI_1_2, True).status_code
    assert HTTP_STATUS_OK == dag_status


@pytest.mark.airflow_required
def test_settings_dag_step_1_2() -> None:
    dag_response = get_response_from_api(config.DAG_URI_1_2 + "/details", True).json()

    assert config.DAG_NAME_STEP1_2 == dag_response["dag_id"]
    assert config.SCHEDULE == dag_response["schedule_interval"]["value"]
    assert config.TAGS_STEP1 == dag_response["tags"]


@pytest.mark.airflow_required
def test_data_dag_step_1_2() -> None:
    dag_response = get_response_from_api(config.DAG_URI_1_2 + "/details", True).json()
    dag_datatime = cast(DateTime, parser.parse(dag_response["start_date"]))

    assert config.START_4_DAY_BEFORE.date() == dag_datatime.date()
