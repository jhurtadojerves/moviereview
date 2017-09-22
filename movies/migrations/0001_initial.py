# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-22 03:30
from __future__ import unicode_literals

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('directors', '0001_initial'),
        ('userprofiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('review', models.TextField()),
                ('created_date', models.DateField(auto_now_add=True)),
                ('slug', autoslug.fields.AutoSlugField(always_update=True, editable=False, populate_from='title', unique=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movies', to='userprofiles.Profile')),
                ('director', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movies', to='directors.Director')),
            ],
        ),
    ]