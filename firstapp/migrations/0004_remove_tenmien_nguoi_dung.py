# Generated by Django 3.2.7 on 2021-09-08 10:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0003_tenmien_nguoi_dung'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tenmien',
            name='nguoi_dung',
        ),
    ]
