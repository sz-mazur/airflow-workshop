"""
Welcome to the second Quiz!
Today we will talk about creating schedule in the property way.
For each question please put answer in CRON format i.g. "* * * * *"
"""


def question01() -> str:
    """
    Write a schedule to run at 00:00 every day
    """
    answer = "0 0 * * *"
    return answer


def question02() -> str:
    """
    Write a schedule to run every Wednesday at 3:15
    """
    answer = "15 3 * * 3"
    return answer


def question03() -> str:
    """
    Write a schedule to run every month in first day at 5:17
    """
    answer = "17 5 1 * *"
    return answer


def question04() -> str:
    """
    Write a schedule to run at 12:00 every first day of January, April, July, October
    """
    answer = "0 12 1 */3 *"
    return answer


def question05() -> str:
    """
    Write a schedule to run every 15 min only between 00:00 and 3:00 in uneven day of month
    """
    answer = "0,15,30,45 0-3 1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31 * *"
    return answer
