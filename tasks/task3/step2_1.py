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
    # TODO
    answer1 = ...
    answer2 = ...
    answer3 = ...

    answer = {"first": hash(answer1), "second": hash(answer2), "third": hash(answer3)}
    return answer


def question02() -> dict[str, int]:
    """
    Please, give {{ ts }} output. If today is 2023-02-17.
    @start_date = "2023-02-02 2:00"
    @schedule = "15 4 * * *"
    @zone = Warsaw UTC+1/+2
    """
    # TODO
    answer1 = ...
    answer2 = ...
    answer3 = ...

    answers = {"first": hash(answer1), "second": hash(answer2), "third": hash(answer3)}
    return answers


def question03() -> dict[str, int]:
    """
    Please, give {{ ts }} output. If today is 2022-12-12.
    @start_date = "2022-09-17 11:45"
    @schedule = "0/25 * * * *"
    @zone = Tokyo UTC+9
    """
    # TODO
    answer1 = ...
    answer2 = ...
    answer3 = ...

    answers = {"first": hash(answer1), "second": hash(answer2), "third": hash(answer3)}
    return answers


def question04() -> dict[str, int]:
    """
    Please, give {{ ds }} output. If today is 2025-09-25.
    @start_date = "2020-03-03 10:26"
    @schedule = "10 11 5 6 *"
    @zone = Bogota UTC-5
    """
    # TODO
    answer1 = ...
    answer2 = ...
    answer3 = ...

    answers = {"first": hash(answer1), "second": hash(answer2), "third": hash(answer3)}
    return answers


def question05() -> dict[str, int]:
    """
    Please, give {{ ts }} output. If today is 2020-10-01 10:00.
    @start_date = "2019-10-31 9:59"
    @schedule = "0 10 * */3 *"
    @zone = Honolulu UTC-10
    """
    # TODO
    answer1 = ...
    answer2 = ...
    answer3 = ...

    answers = {"first": hash(answer1), "second": hash(answer2), "third": hash(answer3)}
    return answers
