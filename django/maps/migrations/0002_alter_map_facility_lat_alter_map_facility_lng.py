# Generated by Django 4.2.6 on 2024-05-15 11:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("maps", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="map",
            name="facility_lat",
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name="map",
            name="facility_lng",
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
