import pytest

from tests.helper.connection import get_response_from_api
from tests.task2 import config


@pytest.mark.airflow_required
def test_custom_operator_dependency() -> None:
    diff_task_response = get_response_from_api(config.DIFF_TASK_URI, True).json()["downstream_task_ids"]

    assert "workflow_finished_operator" in diff_task_response


@pytest.mark.airflow_required
def test_custom_operator_empty_dependency() -> None:
    workflow_finished_response = get_response_from_api(config.WORKFLOW_FINISHED_TASK_URI, True).json()[
        "downstream_task_ids"
    ]
    assert 0 == len(workflow_finished_response)
