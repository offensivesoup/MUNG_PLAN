# Generated by Django 4.2.6 on 2024-05-19 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finances', '0010_alter_deposit_company_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deposit',
            name='company_image',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
