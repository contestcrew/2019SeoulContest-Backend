# Generated by Django 2.2.5 on 2019-09-26 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0004_category_pin_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='occurred_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='발생 시각'),
        ),
    ]
