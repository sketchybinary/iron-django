# Generated by Django 2.1.10 on 2019-12-12 01:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("rate_beer", "0001_initial")]

    operations = [
        migrations.AlterField(
            model_name="rating",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        )
    ]
