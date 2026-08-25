import pandas as pd
from airflow import DAG


# Support functions
def save_df_to_file(df: pd.DataFrame, file_name: str) -> None:
    # TODO
    ...


def join_and_calculate_df(df_max: pd.DataFrame, df_mean: pd.DataFrame, key: str) -> pd.DataFrame:
    # TODO
    ...


# Functions for PythonOperator
def calculate_revenue(separator: str, group_function: str, file_path: str, **_kwargs: dict) -> None:
    # TODO
    ...


def calculate_difference(mean_revenue_path: str, max_revenue_path: str, **_kwargs: dict) -> None:
    # TODO
    ...


def delete_file(file_path: str) -> None:
    # TODO
    ...


# TODO
DAG_ID = ...
START_DATE = ...
SCHEDULE = ...
TAGS = ...

with DAG(
    # DAG config
    dag_id=DAG_ID,
    start_date=START_DATE,
    schedule=SCHEDULE,
    tags=TAGS,
) as dag:
    # First Operator
    # TODO
    ...

    # Second Operator
    # TODO
    ...

    # Third Operator
    # TODO
    ...

    # Clear operator
    # TODO
    ...

    # Finisher Operator
    # TODO
    ...

    # File Sensor
    # TODO
    ...

    # Dependencies
    # TODO
    ...
