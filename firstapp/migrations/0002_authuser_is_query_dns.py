# Generated by Django 3.2.7 on 2021-09-08 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='authuser',
            name='is_query_DNS',
            field=models.BooleanField(default=False),
        ),
    ]
