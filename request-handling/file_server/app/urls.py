from django.urls import path, register_converter

from app.path_converters import DateConverter
from app.views import file_list, file_content
# Определите и зарегистрируйте конвертер для определения даты в урлах и наоборот урла по датам

register_converter(DateConverter, 'date')

urlpatterns = [
    # Определите схему урлов с привязкой к отображениям .views.file_list и .views.file_content
    path('', file_list, name='file_list'),
    path('<date:date>/', file_list, name='file_list'),    # задайте необязательный параметр "date"
                                      # для детальной информации смотрите HTML-шаблоны в директории templates
    path('<str:name>/', file_content, name='file_content'),
]
