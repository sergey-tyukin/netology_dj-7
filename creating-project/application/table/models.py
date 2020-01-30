from django.db import models


class PhonesFieldsFormat(models.Model):
    name = models.CharField(max_length=32)
    width = models.IntegerField(default=3)
    order = models.IntegerField()

    def __str__(self):
        return self.name

    @classmethod
    def clear(cls):
        cls.objects.all().delete()


class FilePath(models.Model):
    path = models.CharField(max_length=256)

    def __str__(self):
        return self.path

    @classmethod
    def clear(cls):
        cls.objects.all().delete()

    @classmethod
    def get_path(cls):
        return cls.objects.first().path

    @classmethod
    def set_path(cls, path):
        cls.objects.create(path=path)