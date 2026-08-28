"""
Welcome to the first Quiz!
Today topic is {{ ds }} and {{ ts }} macro.
For each question you should give FIRST 3 consecutive values for asked macro.
"""


def question01() -> dict[str, int]:
    """
    Please, give {{ ds }} output. If today is 2023-01-25.
    @start_date = "2023-01-01"
    @schedule = "@daily"
    @zone = Buenos Aires UTC-3
    """
    answer1 = "2023-01-01"
    answer2 = "2023-01-02"
    answer3 = "2023-01-03"

    answer = {"first": hash(answer1), "second": hash(answer2), "third": hash(answer3)}
    return answer


def question02() -> dict[str, int]:
    """
    Please, give {{ ts }} output. If today is 2023-02-17.
    @start_date = "2023-02-02 2:00"
    @schedule = "15 4 * * *"
    @zone = Warsaw UTC+1/+2
    """
    answer1 = "2023-02-02T04:15:00+01:00"
    answer2 = "2023-02-03T04:15:00+01:00"
    answer3 = "2023-02-04T04:15:00+01:00"

    answers = {"first": hash(answer1), "second": hash(answer2), "third": hash(answer3)}
    return answers


def question03() -> dict[str, int]:
    """
    Please, give {{ ts }} output. If today is 2022-12-12.
    @start_date = "2022-09-17 11:45"
    @schedule = "0/25 * * * *"
    @zone = Tokyo UTC+9
    """
    answer1 = "2022-09-17T11:50:00+09:00"
    answer2 = "2022-09-17T12:00:00+09:00"
    answer3 = "2022-09-17T12:25:00+09:00"

    answers = {"first": hash(answer1), "second": hash(answer2), "third": hash(answer3)}
    return answers


def question04() -> dict[str, int]:
    """
    Please, give {{ ds }} output. If today is 2025-09-25.
    @start_date = "2020-03-03 10:26"
    @schedule = "10 11 5 6 *"
    @zone = Bogota UTC-5
    """
    answer1 = "2020-06-05"
    answer2 = "2021-06-05"
    answer3 = "2022-06-05"

    answers = {"first": hash(answer1), "second": hash(answer2), "third": hash(answer3)}
    return answers


def question05() -> dict[str, int]:
    """
    Please, give {{ ts }} output. If today is 2020-10-01 10:00.
    @start_date = "2019-10-31 9:59"
    @schedule = "0 10 * */3 *"
    @zone = Honolulu UTC-10
    """
    answer1 = "2019-10-31T10:00:00-10:00"
    answer2 = "2020-01-01T10:00:00-10:00"
    answer3 = "2020-01-02T10:00:00-10:00"

    answers = {"first": hash(answer1), "second": hash(answer2), "third": hash(answer3)}
    return answers
