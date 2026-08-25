from time import sleep

from airflow import DAG
from pendulum import datetime

DEPENDENCY_SWITCH_INDEX = 5


def do_autogenerate_operator(operator_id: int, **_kwargs: dict) -> None:
    print("hello, id:", str(operator_id))
    sleep(15)
    print("bye")


with DAG(
    # TODO
    dag_id="task3_step_3_3",
    start_date=datetime(2023, 1, 1),
    schedule="@daily",
    catchup=True,
    tags=["task3", "step3"],
) as dag:
    # TODO
    ...
