import pendulum
from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator
from pendulum.datetime import DateTime

# Parameter getting from Airflow
try_number_count = "{{ task_instance.try_number }}"
date_value = "{{ ds }}"


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
    dag_id="task3_step_1_2",
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
After changing the start_date to a static date 4 days in the past and unpausing the DAG, 
airflow immediately schedules 4 DAG Runs for 23.08, 24.08, 25.08 and 26.08.
This is called "catchup" - airflow creates DAG Runs for the intervals 
between the start_date and the current date that have not been executed yet.
The {{ ds }} variable in each DAG Run represents the logical date of that particular run, 
not the actual date and time when the task is executed.
"""
