from time import sleep

from airflow import DAG
from airflow.operators.python import PythonOperator
from pendulum import datetime


def do_autogenerate_operator(operator_id: int, **_kwargs: dict) -> None:
    print("hello, id:", str(operator_id))
    sleep(15)
    print("bye")


with DAG(
    # TODO
    dag_id="task3_step_3_1",
    start_date=datetime(2023, 1, 1),
    schedule="@daily",
    catchup=True,
    tags=["task3", "step3"],
) as dag:
    for i in range(16):
        PythonOperator(
            task_id="auto_generated_" + str(i),
            python_callable=do_autogenerate_operator,
            op_kwargs={"operator_id": i},
        )
