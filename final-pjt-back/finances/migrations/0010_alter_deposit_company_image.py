# Generated by Django 4.2.6 on 2024-05-19 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finances', '0009_deposit_company_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deposit',
            name='company_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
