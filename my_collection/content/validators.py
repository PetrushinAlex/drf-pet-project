import datetime

from django.core.exceptions import ValidationError


def validate_release_date(year):
    now = datetime.date.today().year
    if year > now:
        raise ValidationError(
            f'Введите корректную дату, {year} еще не наступил.'
        )
    return year
