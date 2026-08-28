import pendulum
from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator
from pendulum import DateTime

# Parameter getting from Airflow
try_number_count: str = "{{ task_instance.try_number }}"
date_value: str = "{{ ds }}"


# Functions for PythonOperator
def hello(text: str) -> None:
    print("Hello", text)


def try_number(num: int) -> None:
    print("You have run this task", str(num), "times")


def date_info(date_val: str) -> None:
    print("You run this task at", str(date_val))


START_DATE: DateTime = pendulum.datetime(2026, 8, 23)
SCHEDULE: str = "@daily"


# A DAG represents a workflow, a collection of tasks
with DAG(
    dag_id="task3_step_1_3",
    start_date=START_DATE,
    schedule=SCHEDULE,
    tags=["task3", "step1"],
    catchup=False,
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
With setting catchup=False only one DAG Run is scheduled for the current data interval, from 26.08 to 27.08, 
airflow skips all missed intervals and schedules only the latest available interval.
...
"""
