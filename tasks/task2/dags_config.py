DATA_FILE: str = "sales_native.csv"

DAG_ABSOLUTE_PATH: str = "/opt/airflow/dags/"
OUTPUT_PATH: str = DAG_ABSOLUTE_PATH + "output/"
DATA_PATH: str = DAG_ABSOLUTE_PATH + "data/"
DATA_FILE_PATH: str = DATA_PATH + DATA_FILE

TASK2_PREFIX: str = "task2_"
TASK2_SUFFIX: str = "_revenue.csv"

OUTPUT_TASK2: str = OUTPUT_PATH + TASK2_PREFIX
