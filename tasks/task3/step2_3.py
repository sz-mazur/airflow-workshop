"""
Welcome to the final Quiz!
How good do you know macros in Airflow? Let's see!
"""


def question01() -> str:
    """
    Which macro will you use to get date in YYYY-mm-dd format?
    """
    answer = "{{ ds }}"
    return answer


def question02() -> str:
    """
    Which macro will you use to get date in ISO format?
    """
    answer = "{{ ts }}"
    return answer


def question03() -> str:
    """
    Which macro will you use to get execution date in YYYYmmdd format?
    """
    answer = "{{ ds_nodash }}"
    return answer


def question04() -> str:
    """
    Which macro will you use to get the currently running DAG ID?
    """
    answer = "dag.dag_id"
    return answer


def question05() -> str:
    """
    Which macro will you use to get next execution date?
    """
    answer = "{{ next_execution_date }}"
    return answer
