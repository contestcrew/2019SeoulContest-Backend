# Generated by Django 2.2.5 on 2019-09-25 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0003_auto_20190924_2107'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='pin_image',
            field=models.ImageField(blank=True, null=True, upload_to='category_pinimage'),
        ),
    ]