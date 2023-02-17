import math
from datetime import date
from typing import List, Dict

jobs = [
    {"min_salary": 5000, "max_salary": 15000, "date_posted": "2016-08-09"},
    {"min_salary": 2000, "max_salary": 5000, "date_posted": "2020-10-01"},
    {"min_salary": 600, "max_salary": 1000, "date_posted": "2022-25-05"},
    {"min_salary": 2500, "max_salary": 5500, "date_posted": "2002-12-09"},
]


def max_salary_key(job: Dict) -> int:
    """
    Gets max_salary as a sorting key.

    Missing information is treated as the lowest possible value.

    Parameters
    ----------
    job : dict
        Dict represeting a job from the dataset.

    Returns
    -------
    Job's max salary as an int, or -infinite.
    """
    try:
        return int(job["max_salary"])
    except (KeyError, TypeError, ValueError):
        return -math.inf


def min_salary_key(job: Dict) -> int:
    """
    Gets min_salary as a sorting key.

    Missing information is treated as the highest possible value.

    Parameters
    ----------
    job : dict
        Dict represeting a job from the dataset.

    Returns
    -------
    Job's min salary as an int, or infinite.
    """
    try:
        return int(job["min_salary"])
    except (KeyError, TypeError, ValueError):
        return math.inf


def date_posted_key(job: Dict) -> date:
    """
    Gets date_posted as a sorting key.

    Missing information is treated as the lowest possible value.

    Parameters
    ----------
    job : dict
        Dict represeting a job from the dataset.

    Returns
    -------
    Job's date_posted as a date object.
    """
    try:
        return date.fromisoformat(job["date_posted"])
    except (KeyError, TypeError, ValueError):
        return date.min


def sort_by(jobs: List[Dict], criteria: str) -> None:
    """
    Sorts jobs by a given criteria, in-place.

    Sorting must be descending, except for `min_salary` criteria.
    Jobs missing the criteria should end up last.
    Invalid criteria should raise ValueError.

    Parameters
    ----------
    jobs : list
        List of dicts representing the jobs.
    criteria : str
        One of `min_salary`, `max_salary` or `date_posted`.
    """
    criteria_keys = {
        "date_posted": date_posted_key,
        "max_salary": max_salary_key,
        "min_salary": min_salary_key,
    }

    try:
        key = criteria_keys[criteria]
    except KeyError:
        raise ValueError(f"invalid sorting criteria: {criteria}")

    reverse = criteria in ["max_salary", "date_posted"]

    jobs.sort(key=key, reverse=reverse)


# sort_by(jobs, "date_posted")
# sort_by(jobs, "max_salary")
sort_by(jobs, "min_salary")

print(jobs)
