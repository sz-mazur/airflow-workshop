from airflow import DAG
from airflow.operators.python import PythonOperator
from pendulum import datetime

# Parameter getting from Airflow
name = "{{ dag_run.conf['name'] }}"
try_number_count = "{{ task_instance.try_number }}"


# Functions for PythonOperator
def hello(text: str) -> None:
    print("Hello", text)


def try_number(num: int) -> None:
    print("You have run this task", str(num), "times")


# A DAG represents a workflow, a collection of tasks
with DAG(
    dag_id="example_dag",
    start_date=datetime(2022, 1, 1),
    schedule="@hourly",
    tags=["task1"],
) as dag:
    # Tasks are represented as operators
    hello_task = PythonOperator(
        task_id="hello",
        python_callable=hello,
        op_kwargs={"text": name},
    )

    number = PythonOperator(
        task_id="try_number",
        python_callable=try_number,
        op_kwargs={"num": try_number_count},
    )
