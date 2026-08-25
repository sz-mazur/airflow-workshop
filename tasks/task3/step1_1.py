from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator

# Parameter getting from Airflow
try_number_count = "{{ task_instance.try_number }}"
date_value = ...


# Functions for PythonOperator
def hello(text: str) -> None:
    print("Hello", text)


def try_number(num: int) -> None:
    print("You have run this task", str(num), "times")


def date_info(date_val: str) -> None:
    print("You run this task at", str(date_val))


# TODO
START_DATE = ...
SCHEDULE = ...

# A DAG represents a workflow, a collection of tasks
with DAG(
    dag_id="task3_step_1_1",
    start_date=START_DATE,
    schedule=SCHEDULE,
    tags=["task3", "step1"],
) as dag:
    # Tasks are represented as operators
    EmptyOperator(
        task_id="hello_word",
    )

    number = PythonOperator(
        task_id="try_number",
        python_callable=try_number,
        op_kwargs={"num": try_number_count},
    )

    date = PythonOperator(
        task_id="date",
        python_callable=date_info,
        op_kwargs={"date_val": date_value},
    )

"""
What happens when we start DAG?
# TODO
...
"""
