# Generated by Django 3.1 on 2020-09-01 07:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='photo_main',
            field=models.ImageField(default=datetime.datetime.now, upload_to='photos/%Y/%M/%d/'),
        ),
    ]
