# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-13 11:44
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('handle', models.TextField()),
                ('message', models.TextField()),
                ('timestamp', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('label', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('serial_number', models.CharField(max_length=16, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator('^[0-9A-F]{16}$', 'Only hex values are allowed')])),
                ('name', models.TextField(blank=True, max_length=20, null=True)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sensors', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='message',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='sensors.Room'),
        ),
    ]
