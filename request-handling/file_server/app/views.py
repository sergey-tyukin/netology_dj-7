import os
from _datetime import datetime

from django.shortcuts import render
from django.conf import settings


def file_list(request, date=None):
    template_name = 'index.html'

    files = os.listdir(settings.FILES_PATH)
    # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:

    files_list = []

    for file in files:
        statinfo = os.stat(os.path.join(settings.FILES_PATH, file))

        files_list.append({'name': file,
                           'ctime': datetime.fromtimestamp(statinfo.st_ctime),
                           'mtime': datetime.fromtimestamp(statinfo.st_mtime)})

    context = {
        'files': files_list,
        'date': date
    }

    return render(request, template_name, context)


def file_content(request, name):
    # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
    with open(os.path.join(settings.FILES_PATH, name), 'r') as f:
        content = f.read()
    return render(
        request,
        'file_content.html',
        context={'file_name': name, 'file_content': content}
    )

