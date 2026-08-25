import argparse
import os
import shutil


def deploy_dags(task_nr: int) -> None:
    task_dir = os.path.join("tasks", f"task{task_nr}")
    if not os.path.exists(task_dir):
        print(f"Error: Task {task_nr} does not exist")
        return

    destination_dags_dir: str = os.path.join("airflow_local", "dags")
    destination_task_dir: str = os.path.join(destination_dags_dir, "tasks", f"task{task_nr}")
    destination_data_dir: str = os.path.join(destination_dags_dir, "data")

    os.makedirs(destination_task_dir, exist_ok=True)
    os.makedirs(destination_data_dir, exist_ok=True)

    for file_name in os.listdir(task_dir):
        if file_name.endswith(".py") and file_name != "__init__.py":
            shutil.copy2(os.path.join(task_dir, file_name), destination_task_dir)

    for file_name in os.listdir(task_dir):
        if file_name.endswith(".csv"):
            shutil.copy2(os.path.join(task_dir, file_name), destination_data_dir)

    print(f"DAGs and data files deployed successfully for task {task_nr}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Deploy DAGs and data files for a specific task.")
    parser.add_argument("task_number", type=int, help="The number of the task to deploy DAGs for")
    args = parser.parse_args()

    deploy_dags(args.task_number)
