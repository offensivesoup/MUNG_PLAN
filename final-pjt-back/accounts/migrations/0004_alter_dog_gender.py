# Generated by Django 4.2.6 on 2024-05-17 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_dog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dog',
            name='gender',
            field=models.CharField(choices=[('M', '남성(Man)'), ('W', '여성(Woman)'), ('Q', '중성')], max_length=1),
        ),
    ]
