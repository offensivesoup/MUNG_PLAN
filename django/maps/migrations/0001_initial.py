# Generated by Django 4.2.6 on 2024-05-15 11:34

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Map",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("facility_name", models.CharField(blank=True, max_length=255)),
                ("facility_explain", models.CharField(blank=True, max_length=255)),
                ("facility_parking", models.CharField(blank=True, max_length=255)),
                ("facility_province", models.CharField(blank=True, max_length=255)),
                ("facility_location", models.CharField(blank=True, max_length=255)),
                ("facility_lat", models.IntegerField()),
                ("facility_lng", models.IntegerField()),
                ("facility_new_address", models.CharField(blank=True, max_length=255)),
                ("facility_old_address", models.CharField(blank=True, max_length=255)),
                ("facility_holiday", models.CharField(blank=True, max_length=255)),
                ("facility_category1", models.CharField(blank=True, max_length=255)),
                ("facility_category2", models.CharField(blank=True, max_length=255)),
                ("facility_category3", models.CharField(blank=True, max_length=255)),
                ("facility_link", models.CharField(blank=True, max_length=255)),
            ],
        ),
    ]
