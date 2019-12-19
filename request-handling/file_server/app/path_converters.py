from datetime import datetime, date

from django.urls import register_converter


class DateConverter:
    regex = r'[0-9]{4}-[0-9]{1,2}-[0-9]{1,2}'
    date_format = '%Y-%m-%d'

    def to_python(self, value: str) -> date:
        return datetime.strptime(value, self.date_format).date()

    def to_url(self, value: date) -> str:
        return value.strftime(self.date_format)
