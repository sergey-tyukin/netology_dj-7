# Generated by Django 2.0.13 on 2020-01-29 19:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='phonesfileformat',
            name='field_type',
        ),
    ]
