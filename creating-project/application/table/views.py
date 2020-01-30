import csv

from django.shortcuts import render
from django.conf import settings

from .models import FilePath, PhonesFieldsFormat


def table_view(request):

    PhonesFieldsFormat.clear()
    FilePath.clear()

    FilePath.set_path(settings.CSV_FILENAME)

    for num, field in enumerate(settings.COLUMNS):
        PhonesFieldsFormat.objects.create(order=num,
                                          name=field['name'],
                                          width=field['width'])

    template = 'table.html'
    with open(FilePath.get_path(), 'rt') as csv_file:
        header = []
        table = []
        table_reader = csv.reader(csv_file, delimiter=';')
        for table_row in table_reader:
            if not header:
                header = {idx: value for idx, value in enumerate(table_row)}
            else:
                row = {header.get(idx) or 'col{:03d}'.format(idx): value
                       for idx, value in enumerate(table_row)}
                table.append(row)

        context = {
            # 'columns': settings.COLUMNS,
            'columns': PhonesFieldsFormat.objects.all(),
            'table': table,
            'csv_file': FilePath.get_path()
        }
        result = render(request, template, context)
    return result
