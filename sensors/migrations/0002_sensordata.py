# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-13 20:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sensors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SensorData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('value', models.DecimalField(decimal_places=2, max_digits=6)),
                ('sensor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='data', to='sensors.Sensor')),
            ],
        ),
    ]
