# Generated by Django 5.0.4 on 2024-05-02 13:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_image_url_alter_post_last_viewed_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='last_viewed_datetime',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 2, 13, 17, 20, 754360)),
        ),
    ]
