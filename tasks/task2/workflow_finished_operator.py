from typing import List

from airflow.models.baseoperator import BaseOperator

from tasks.task2.dags_config import OUTPUT_PATH


class WorkflowFinishedOperator(BaseOperator):
    template_fields = ("filenames",)

    def __init__(self, filenames: List[str], **kwargs):
        super().__init__(**kwargs)
        self.filenames = filenames

    def execute(self, context):
        for filename in self.filenames:
            file_path = f"{OUTPUT_PATH}{filename}.csv"

            with open(file_path, "r") as file:
                print(f"Content of the {filename} file\n" + file.read())
