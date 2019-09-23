# Generated by Django 2.2.5 on 2019-09-23 15:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("request", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="request",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="requests",
                to=settings.AUTH_USER_MODEL,
                verbose_name="작성자",
            ),
        ),
        migrations.AddField(
            model_name="request",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="requests",
                to="request.Category",
                verbose_name="카테고리",
            ),
        ),
    ]