from cron_converter import Cron
from cron_converter.sub_modules.seeker import Seeker
from pendulum.datetime import DateTime


def generate_hash_ds_answers(start_date: DateTime, schedule: str) -> dict[str, int]:
    schedule_ = get_schedule(start_date, schedule)
    return {
        "first": hash(schedule_.next().date().strftime("%Y-%m-%d")),
        "second": hash(schedule_.next().date().strftime("%Y-%m-%d")),
        "third": hash(schedule_.next().date().strftime("%Y-%m-%d")),
    }


def generate_hash_ts_answers(start_date: DateTime, schedule: str) -> dict[str, int]:
    schedule_ = get_schedule(start_date, schedule)
    return {
        "first": hash(schedule_.next().isoformat()),
        "second": hash(schedule_.next().isoformat()),
        "third": hash(schedule_.next().isoformat()),
    }


def get_schedule(start_date: DateTime, schedule: str) -> Seeker:
    return Cron(cron_string=schedule).schedule(start_date=start_date)
