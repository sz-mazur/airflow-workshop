from typing import Any

DAG_NAME: str = "task2_sales_dag"

EXCEPTED_SETTINGS: dict[str, Any] = {
    "dag_id": DAG_NAME,
    "start_date": "2023-01-01T00:00:00+00:00",
    "schedule": "@once",
    "tags": [{"name": "task2"}],
}
DAG_URI: str = "dags/" + EXCEPTED_SETTINGS["dag_id"]
MEAN_TASK_URI: str = DAG_URI + "/tasks/mean_revenue"
MAX_TASK_URI: str = DAG_URI + "/tasks/max_revenue"
DIFF_TASK_URI: str = DAG_URI + "/tasks/diff_revenue"
DELETE_TASK_URI: str = DAG_URI + "/tasks/delete_source_file"
WAITING_FOR_TASK_URI: str = DAG_URI + "/tasks/waiting_for_data"
WORKFLOW_FINISHED_TASK_URI: str = DAG_URI + "/tasks/workflow_finished_operator"
