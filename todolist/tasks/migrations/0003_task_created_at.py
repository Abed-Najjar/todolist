# Generated by Django 4.2.8 on 2024-01-13 13:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_remove_task_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='created_at',
            field=models.DateField(default=datetime.date(2024, 1, 13)),
        ),
    ]