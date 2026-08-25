from pendulum import datetime, now
from pendulum.datetime import DateTime

from tests.helper import quiz_helper

DAG_NAME_STEP1_1: str = "task3_step_1_1"
DAG_NAME_STEP1_2: str = "task3_step_1_2"
DAG_NAME_STEP1_3: str = "task3_step_1_3"
DAG_NAME_STEP3_1: str = "task3_step_3_1"
DAG_NAME_STEP3_2: str = "task3_step_3_2"
DAG_NAME_STEP3_3: str = "task3_step_3_3"

DAG_URI_1_1: str = "dags/" + DAG_NAME_STEP1_1
DAG_URI_1_2: str = "dags/" + DAG_NAME_STEP1_2
DAG_URI_1_3: str = "dags/" + DAG_NAME_STEP1_3
DAG_URI_3_1: str = "dags/" + DAG_NAME_STEP3_1
DAG_URI_3_2: str = "dags/" + DAG_NAME_STEP3_2
DAG_URI_3_3: str = "dags/" + DAG_NAME_STEP3_3

SCHEDULE: str = "@daily"
TAGS_STEP1: list[dict[str, str]] = [{"name": "task3"}, {"name": "step1"}]
TAGS_STEP3: list[dict[str, str]] = [{"name": "task3"}, {"name": "step3"}]

START_NOW: DateTime = now()
START_4_DAY_BEFORE: DateTime = START_NOW.subtract(days=4)
CATCHUP: bool = False

DATA_TIME01: DateTime = datetime(2023, 1, 1)
DATA_TIME02: DateTime = datetime(2023, 2, 2, 2, tz="Europe/Warsaw")
DATA_TIME03: DateTime = datetime(2022, 9, 17, 11, 45, tz="Asia/Tokyo")
DATA_TIME04: DateTime = datetime(2020, 3, 3, 10, 26)
DATA_TIME05: DateTime = datetime(2019, 10, 31, 9, 59, tz="Pacific/Honolulu")
DATA_TIME06: DateTime = datetime(2022, 9, 19, 0, 24)
DATA_TIME07: DateTime = datetime(2019, 10, 31, 1, 3)

QUIZ_1_QUESTION_1_ANSWER_HASH: dict[str, int] = quiz_helper.generate_hash_ds_answers(DATA_TIME01, "0 0 * * *")
QUIZ_1_QUESTION_2_ANSWER_HASH: dict[str, int] = quiz_helper.generate_hash_ts_answers(DATA_TIME02, "15 4 * * *")
QUIZ_1_QUESTION_3_ANSWER_HASH: dict[str, int] = quiz_helper.generate_hash_ts_answers(DATA_TIME03, "*/25 * * * *")
QUIZ_1_QUESTION_4_ANSWER_HASH: dict[str, int] = quiz_helper.generate_hash_ds_answers(DATA_TIME04, "10 11 5 6 *")
QUIZ_1_QUESTION_5_ANSWER_HASH: dict[str, int] = quiz_helper.generate_hash_ts_answers(DATA_TIME05, "0 10 * */3 *")

MAX_ACTIVE_TASKS = 2
MAX_ACTIVE_RUNS = 2
SWITCH_DEPENDENCY_AT_INDEX = 5
