# Generated by Django 2.1.10 on 2019-10-14 20:55

import django.core.validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [("rate_beer", "0001_initial")]

    operations = [
        migrations.RemoveField(model_name="beer", name="average_rating"),
        migrations.AlterField(
            model_name="beer",
            name="id",
            field=models.UUIDField(
                default=uuid.uuid4, editable=False, primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="rating",
            name="id",
            field=models.UUIDField(
                default=uuid.uuid4, editable=False, primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="rating",
            name="rating",
            field=models.IntegerField(
                default=5,
                validators=[
                    django.core.validators.MaxValueValidator(5),
                    django.core.validators.MinValueValidator(1),
                ],
            ),
        ),
    ]
