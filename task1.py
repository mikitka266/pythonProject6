'В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.'
from datetime import datetime


def _check_leap_year(date: str) -> bool:
    NORMAL_1 = 4
    NORMAL_2 = 100
    NORMAL_3 = 400
    YEARS = range(1, 10000)
    year = int(date.split(".")[-1])
    if year in YEARS and year % NORMAL_1 == 0 and year % NORMAL_2 !=0 or year % NORMAL_3 == 0:
        return True
    return False


def check_year(year: str) -> bool:
    try:
        _value = datetime.strptime(year, "%d.%m.%Y").date()
        return True
    except:
        return False


def date_validator(date: str) -> str:
    if check_year(date):
        return 'Leap year' if _check_leap_year(date) else 'Not a leap year'
    else:
        return f'Date is not corrected'


