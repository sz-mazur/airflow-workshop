from tasks.task3.step2_1 import (
    question01,
    question02,
    question03,
    question04,
    question05,
)
from tests.task3 import config


def test_correctness_question_1() -> None:
    answer = question01()
    assert answer == config.QUIZ_1_QUESTION_1_ANSWER_HASH


def test_correctness_question_2() -> None:
    answer = question02()
    assert answer == config.QUIZ_1_QUESTION_2_ANSWER_HASH


def test_correctness_question_3() -> None:
    answer = question03()
    assert answer == config.QUIZ_1_QUESTION_3_ANSWER_HASH


def test_correctness_question_4() -> None:
    answer = question04()
    assert answer == config.QUIZ_1_QUESTION_4_ANSWER_HASH


def test_correctness_question_5() -> None:
    answer = question05()
    assert answer == config.QUIZ_1_QUESTION_5_ANSWER_HASH
