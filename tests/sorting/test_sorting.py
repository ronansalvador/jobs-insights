from src.pre_built.sorting import sort_by

jobs = [
    {"min_salary": 5000, "max_salary": 15000, "date_posted": "2016-08-09"},
    {"min_salary": 2000, "max_salary": 5000, "date_posted": "2020-10-01"},
    {"min_salary": 600, "max_salary": 1000, "date_posted": "2022-25-05"},
    {"min_salary": 2500, "max_salary": 5500, "date_posted": "2002-12-09"},
    {"min_salary": 8000, "max_salary": 14000, "date_posted": "2005-04-01"},
    {"min_salary": 300, "max_salary": 500, "date_posted": "2021-26-01"},
]


def test_sort_by_criteria():
    pass
    max_sorted = [
        {'min_salary': 5000, 'max_salary': 15000, 'date_posted': '2016-08-09'},
        {'min_salary': 8000, 'max_salary': 14000, 'date_posted': '2005-04-01'},
        {'min_salary': 2500, 'max_salary': 5500, 'date_posted': '2002-12-09'},
        {'min_salary': 2000, 'max_salary': 5000, 'date_posted': '2020-10-01'},
        {'min_salary': 600, 'max_salary': 1000, 'date_posted': '2022-25-05'},
        {'min_salary': 300, 'max_salary': 500, 'date_posted': '2021-26-01'},
    ]

    sort_by(jobs, "max_salary")
    assert jobs == max_sorted

    min_sorted = [
        {'min_salary': 300, 'max_salary': 500, 'date_posted': '2021-26-01'},
        {'min_salary': 600, 'max_salary': 1000, 'date_posted': '2022-25-05'},
        {'min_salary': 2000, 'max_salary': 5000, 'date_posted': '2020-10-01'},
        {'min_salary': 2500, 'max_salary': 5500, 'date_posted': '2002-12-09'},
        {'min_salary': 5000, 'max_salary': 15000, 'date_posted': '2016-08-09'},
        {'min_salary': 8000, 'max_salary': 14000, 'date_posted': '2005-04-01'},
    ]

    sort_by(jobs, "min_salary")
    assert jobs == min_sorted

    date_sorted = [
        {'min_salary': 2000, 'max_salary': 5000, 'date_posted': '2020-10-01'},
        {'min_salary': 5000, 'max_salary': 15000, 'date_posted': '2016-08-09'},
        {'min_salary': 8000, 'max_salary': 14000, 'date_posted': '2005-04-01'},
        {'min_salary': 2500, 'max_salary': 5500, 'date_posted': '2002-12-09'},
        {'min_salary': 600, 'max_salary': 1000, 'date_posted': '2022-25-05'},
        {'min_salary': 300, 'max_salary': 500, 'date_posted': '2021-26-01'},
      ]

    sort_by(jobs, "date_posted")
    assert jobs == date_sorted
