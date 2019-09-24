# Generated by Django 2.2.5 on 2019-09-24 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MobileDevice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='MobileNotification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('message', models.TextField()),
                ('status', models.CharField(default='unread', max_length=10)),
            ],
        ),
    ]