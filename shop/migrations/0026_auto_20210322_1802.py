# Generated by Django 3.1.5 on 2021-03-22 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0025_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='living_index',
            field=models.CharField(max_length=6),
        ),
        migrations.AlterField(
            model_name='order',
            name='passport_number',
            field=models.CharField(max_length=6),
        ),
        migrations.AlterField(
            model_name='order',
            name='passport_series',
            field=models.CharField(max_length=4),
        ),
        migrations.AlterField(
            model_name='order',
            name='registration_index',
            field=models.CharField(max_length=6),
        ),
    ]
