# Generated by Django 5.1 on 2024-08-14 05:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("services", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="service",
            name="service_group",
        ),
        migrations.AddField(
            model_name="servicetype",
            name="service_group",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="services.servicegroup",
            ),
        ),
    ]
