import pandas as pd
import os
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.sensors.filesystem import FileSensor
from pendulum import datetime

from tasks.task2.workflow_finished_operator import WorkflowFinishedOperator
from tasks.task2.dags_config import DATA_FILE_PATH, OUTPUT_TASK2, TASK2_SUFFIX


MEAN_FILE_PATH: str = OUTPUT_TASK2 + 'mean' + TASK2_SUFFIX
MAX_FILE_PATH: str = OUTPUT_TASK2 + 'max' + TASK2_SUFFIX
DIFF_FILE_PATH: str = OUTPUT_TASK2 + 'difference' + TASK2_SUFFIX

# Support functions
def save_df_to_file(df: pd.DataFrame, file_name: str) -> None:
    df.to_csv(file_name, index=False)


def join_and_calculate_df(df_max: pd.DataFrame, df_mean: pd.DataFrame, key: str) -> pd.DataFrame:
    df = df_max.merge(df_mean, on=key)
    df["difference"] = df["max_revenue"] - df["mean_revenue"]
    return df

# Functions for PythonOperator
def calculate_revenue(separator: str, group_function: str, file_path: str, **_kwargs: dict) -> None:
    df = pd.read_csv(file_path, sep=separator)
    result = (
        df.groupby("orderMethodType")["revenue"]
        .agg(group_function)
        .reset_index()
        .rename(columns={"revenue": f"{group_function}_revenue"})
    )
    if group_function == "mean":
        save_df_to_file(result, MEAN_FILE_PATH)
    elif group_function == "max":
        save_df_to_file(result, MAX_FILE_PATH)
    else:
        raise ValueError(f"Unsupported group function: {group_function}")


def calculate_difference(mean_revenue_path: str, max_revenue_path: str, **_kwargs: dict) -> None:
    df_mean_revenue = pd.read_csv(mean_revenue_path)
    df_max_revenue = pd.read_csv(max_revenue_path)
    result = join_and_calculate_df(df_max_revenue, df_mean_revenue, key="orderMethodType")
    save_df_to_file(result, DIFF_FILE_PATH)


def delete_file(file_path: str) -> None:
    os.remove(file_path)


DAG_ID = "task2_sales_dag"
START_DATE = datetime(2023, 1, 1)
SCHEDULE = "@once"
TAGS = ["task2"]

with DAG(
    # DAG config
    dag_id=DAG_ID,
    start_date=START_DATE,
    schedule=SCHEDULE,
    tags=TAGS,
) as dag:
    # First Operator
    mean_revenue = PythonOperator(
        task_id="mean_revenue",
        python_callable=calculate_revenue,
        op_kwargs={
            "separator": ",",
            "group_function": "mean",
            "file_path": DATA_FILE_PATH
        }
    )
    # Second Operator
    max_revenue = PythonOperator(
        task_id="max_revenue",
        python_callable=calculate_revenue,
        op_kwargs={
            "separator": ",",
            "group_function": "max",
            "file_path": DATA_FILE_PATH
        }
    )

    # Third Operator
    diff_revenue = PythonOperator(
        task_id="diff_revenue",
        python_callable=calculate_difference,
        trigger_rule="none_failed",
        op_kwargs={
            "mean_revenue_path": MEAN_FILE_PATH,
            "max_revenue_path": MAX_FILE_PATH
        }

    )

    # Clear operator
    delete_source_file = PythonOperator(
        task_id="delete_source_file",
        python_callable=delete_file,
        trigger_rule="none_failed",
        op_kwargs={
            "file_path": DATA_FILE_PATH
        }
    )

    # Finisher Operator
    workflow_finished_operator = WorkflowFinishedOperator(
        task_id="workflow_finished_operator",
        filenames=[
            "{{ params.diff_file }}",
            "{{ params.max_file }}",
            "{{ params.mean_file }}",
        ],
        params={
            "diff_file": "task2_difference_revenue",
            "max_file": "task2_max_revenue",
            "mean_file": "task2_mean_revenue",
        },
    )

    # File Sensor
    waiting_for_data = FileSensor(
        task_id="waiting_for_data",
        filepath=DATA_FILE_PATH,
        fs_conn_id="fs_default",
    )

    # Dependencies
    waiting_for_data >> (mean_revenue, max_revenue) >> diff_revenue >> (delete_source_file, workflow_finished_operator)
