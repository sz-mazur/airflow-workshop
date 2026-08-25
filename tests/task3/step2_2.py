from tasks.task3.step2_2 import (
    question01,
    question02,
    question03,
    question04,
    question05,
)
from tests.helper import quiz_helper
from tests.task3 import config


def test_correctness_question_1() -> None:
    answer = question01()
    schedule01 = quiz_helper.get_schedule(config.DATA_TIME03, answer)
    schedule02 = quiz_helper.get_schedule(config.DATA_TIME04, answer)
    schedule03 = quiz_helper.get_schedule(config.DATA_TIME05, answer)

    assert "2022-09-18T00:00:00+09:00" == schedule01.next().isoformat()
    assert "2020-03-04T00:00:00+00:00" == schedule02.next().isoformat()
    assert "2019-11-01T00:00:00-10:00" == schedule03.next().isoformat()


def test_correctness_question_2() -> None:
    answer = question02()
    schedule01 = quiz_helper.get_schedule(config.DATA_TIME03, answer)
    schedule02 = quiz_helper.get_schedule(config.DATA_TIME04, answer)
    schedule03 = quiz_helper.get_schedule(config.DATA_TIME05, answer)

    assert "2022-09-21T03:15:00+09:00" == schedule01.next().isoformat()
    assert "2020-03-04T03:15:00+00:00" == schedule02.next().isoformat()
    assert "2019-11-06T03:15:00-10:00" == schedule03.next().isoformat()


def test_correctness_question_3() -> None:
    answer = question03()
    schedule01 = quiz_helper.get_schedule(config.DATA_TIME03, answer)
    schedule02 = quiz_helper.get_schedule(config.DATA_TIME04, answer)
    schedule03 = quiz_helper.get_schedule(config.DATA_TIME05, answer)

    assert "2022-10-01T05:17:00+09:00" == schedule01.next().isoformat()
    assert "2020-04-01T05:17:00+00:00" == schedule02.next().isoformat()
    assert "2019-11-01T05:17:00-10:00" == schedule03.next().isoformat()


def test_correctness_question_4() -> None:
    answer = question04()
    schedule01 = quiz_helper.get_schedule(config.DATA_TIME03, answer)
    schedule02 = quiz_helper.get_schedule(config.DATA_TIME04, answer)
    schedule03 = quiz_helper.get_schedule(config.DATA_TIME05, answer)

    assert "2022-10-01T12:00:00+09:00" == schedule01.next().isoformat()
    assert "2020-04-01T12:00:00+00:00" == schedule02.next().isoformat()
    assert "2020-01-01T12:00:00-10:00" == schedule03.next().isoformat()


def test_correctness_question_5() -> None:
    answer = question05()
    schedule01 = quiz_helper.get_schedule(config.DATA_TIME03, answer)
    schedule02 = quiz_helper.get_schedule(config.DATA_TIME06, answer)
    schedule03 = quiz_helper.get_schedule(config.DATA_TIME07, answer)

    assert "2022-09-19T00:00:00+09:00" == schedule01.next().isoformat()
    assert "2022-09-19T00:30:00+00:00" == schedule02.next().isoformat()
    assert "2019-10-31T01:15:00+00:00" == schedule03.next().isoformat()
