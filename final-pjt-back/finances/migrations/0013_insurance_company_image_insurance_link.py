# Generated by Django 4.2.6 on 2024-05-22 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finances', '0012_deposit_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='insurance',
            name='company_image',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='insurance',
            name='link',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
    ]