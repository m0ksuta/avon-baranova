# Generated by Django 3.1.5 on 2021-02-04 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_auto_20210203_2235'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainPageParagraph',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='actual',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
