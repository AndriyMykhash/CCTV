# Generated by Django 3.0.6 on 2020-05-19 15:38

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('time', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('image', models.ImageField(upload_to='record/2020/05/19')),
            ],
            options={
                'ordering': ['time'],
            },
        ),
    ]
