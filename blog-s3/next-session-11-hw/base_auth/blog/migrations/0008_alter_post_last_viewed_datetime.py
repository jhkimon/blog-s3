# Generated by Django 5.0.4 on 2024-05-03 05:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_post_last_viewed_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='last_viewed_datetime',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 3, 5, 54, 38, 744412)),
        ),
    ]
