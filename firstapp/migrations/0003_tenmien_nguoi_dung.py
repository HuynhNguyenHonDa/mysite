# Generated by Django 3.2.7 on 2021-09-08 10:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0002_authuser_is_query_dns'),
    ]

    operations = [
        migrations.AddField(
            model_name='tenmien',
            name='nguoi_dung',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='firstapp.authuser'),
            preserve_default=False,
        ),
    ]
