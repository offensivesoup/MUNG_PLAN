<<<<<<< HEAD

=======
>>>>>>> dev
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0004_article_like_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='Category',
            field=models.CharField(choices=[('고민나누기', '고민나누기'), ('중고장터', '중고장터'), ('동네사람들', '동네사람들')], max_length=5),
        ),
    ]
