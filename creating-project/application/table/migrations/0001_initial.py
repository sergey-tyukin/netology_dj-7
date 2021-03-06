# Generated by Django 2.0.13 on 2020-01-29 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FilePath',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='PhonesFileFormat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('field_type', models.CharField(choices=[('str', 'String'), ('int', 'Integer'), ('date', 'Date'), ('bool', 'Boolean')], default='str', max_length=4)),
                ('width', models.IntegerField(default=3)),
                ('order', models.IntegerField()),
            ],
        ),
    ]
