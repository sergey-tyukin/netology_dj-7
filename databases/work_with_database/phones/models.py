from django.db import models
from django.template.defaultfilters import slugify


class Phone(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    price = models.FloatField()
    image = models.CharField(max_length=256)
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=64, unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Phone, self).save(*args, **kwargs)
