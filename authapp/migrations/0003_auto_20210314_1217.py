# Generated by Django 3.1.5 on 2021-03-14 09:17

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0002_auto_20210313_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='activation_key_expired',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 16, 9, 17, 45, 493935, tzinfo=utc)),
        ),
    ]
