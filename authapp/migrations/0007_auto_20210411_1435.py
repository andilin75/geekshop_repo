# Generated by Django 3.1.5 on 2021-04-11 11:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0006_auto_20210322_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='activation_key_expired',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 13, 11, 35, 6, 962673, tzinfo=utc)),
        ),
    ]