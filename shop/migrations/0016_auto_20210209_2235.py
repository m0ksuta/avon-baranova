# Generated by Django 3.1.5 on 2021-02-09 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0015_auto_20210209_2234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='living_index',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='passport_number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='passport_series',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='registration_index',
            field=models.IntegerField(),
        ),
    ]
