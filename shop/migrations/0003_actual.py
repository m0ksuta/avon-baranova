# Generated by Django 3.1.5 on 2021-02-03 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20210201_2018'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actual',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]