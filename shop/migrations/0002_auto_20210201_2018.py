# Generated by Django 3.1.5 on 2021-02-01 17:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Catalogue',
            new_name='Product',
        ),
    ]