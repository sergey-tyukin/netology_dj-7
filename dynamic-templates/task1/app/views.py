import csv

from django.shortcuts import render

def inflation_view(request):
    template_name = 'inflation.html'

    with open('inflation_russia.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=';')
        data = []

        header = next(reader)
        for row in reader:
            tmp_data = [int(row[0])]
            for elem in row[1:]:
                try:
                    val = float(elem)
                except ValueError:
                    val = '-'
                finally:
                    tmp_data.append(val)

            data.append(tmp_data)
    context = {'header': header, 'data': data}

    return render(request, template_name, context)