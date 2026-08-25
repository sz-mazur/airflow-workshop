import pandas as pd
import pytest
from pandas._testing import assert_frame_equal

import tasks.task2.task2_sales_dag as dag
import tests.task2.config as conf
from tests.helper.connection import get_response_from_api


@pytest.mark.airflow_required
def test_diff_revenue_operator_type() -> None:
    response_diff_revenue_operator = get_response_from_api(conf.DIFF_TASK_URI, True).json()

    assert "PythonOperator" == response_diff_revenue_operator["operator_name"]
    assert "templates_dict" in response_diff_revenue_operator["template_fields"]


@pytest.mark.airflow_required
def test_diff_revenue_operator_dependency() -> None:
    task_mean_response = get_response_from_api(conf.MEAN_TASK_URI, True).json()["downstream_task_ids"]
    task_max_response = get_response_from_api(conf.MAX_TASK_URI, True).json()["downstream_task_ids"]

    assert "diff_revenue" in task_mean_response
    assert "diff_revenue" in task_max_response


@pytest.mark.airflow_required
def test_delete_task_type() -> None:
    delete_task_response = get_response_from_api(conf.DELETE_TASK_URI, True).json()

    assert "PythonOperator" == delete_task_response["operator_name"]


@pytest.mark.airflow_required
def test_delete_task_dependency() -> None:
    diff_task_response = get_response_from_api(conf.DIFF_TASK_URI, True).json()["downstream_task_ids"]

    assert "delete_source_file" in diff_task_response


@pytest.mark.airflow_required
def test_trigger_rule_in_delete_operator() -> None:
    trigger_rule_response = get_response_from_api(conf.DELETE_TASK_URI, True).json()["trigger_rule"]

    assert "none_failed" == trigger_rule_response


def test_join_and_calculate_df_function() -> None:
    df_1 = pd.DataFrame(
        [
            dict(orderMethodType="A", mean_revenue=1),
            dict(orderMethodType="B", mean_revenue=2),
        ]
    )
    df_2 = pd.DataFrame(
        [
            dict(orderMethodType="B", max_revenue=1),
            dict(orderMethodType="A", max_revenue=2),
        ]
    )

    df_excepted = pd.DataFrame(
        [
            dict(orderMethodType="A", mean_revenue=1, max_revenue=2, difference=1),
            dict(orderMethodType="B", mean_revenue=2, max_revenue=1, difference=-1),
        ]
    )

    df_result = dag.join_and_calculate_df(df_1, df_2, "orderMethodType")

    assert_frame_equal(df_excepted, df_result)
