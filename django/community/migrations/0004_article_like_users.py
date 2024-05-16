# Generated by Django 4.2.6 on 2024-05-16 12:40

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("community", "0003_rename_user_id_article_user_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="article",
            name="like_users",
            field=models.ManyToManyField(
                related_name="like_article", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
