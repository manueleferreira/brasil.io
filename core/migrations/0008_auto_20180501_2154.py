# Generated by Django 2.0.3 on 2018-05-01 21:54

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20180426_2308'),
    ]

    operations = [
        migrations.AddField(
            model_name='field',
            name='choices',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='field',
            name='has_choices',
            field=models.BooleanField(default=False),
        ),
    ]