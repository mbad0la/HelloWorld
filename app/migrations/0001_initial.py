# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-09 14:53
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=300)),
                ('options', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=50), size=None)),
                ('active', models.BooleanField(default=True)),
                ('startDate', models.DateField()),
                ('endDate', models.DateField()),
                ('pollType', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectName', models.CharField(max_length=100)),
                ('projectDescription', models.CharField(max_length=300)),
                ('repo', models.CharField(max_length=300)),
                ('languages', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=20), size=None)),
                ('frameworks', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=20), size=None)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=30)),
                ('lastName', models.CharField(max_length=30)),
                ('dob', models.DateField()),
                ('batch', models.IntegerField()),
                ('department', models.CharField(max_length=30)),
                ('adminPrivilege', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Votes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.CharField(max_length=50)),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Poll')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.User')),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='contributors',
            field=models.ManyToManyField(related_name='projects', to='app.User'),
        ),
        migrations.AddField(
            model_name='project',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.User'),
        ),
        migrations.AddField(
            model_name='login',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.User'),
        ),
    ]
