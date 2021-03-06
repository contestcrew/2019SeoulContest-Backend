# Generated by Django 2.2.5 on 2019-09-24 09:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='제목')),
                ('content', models.TextField(verbose_name='내용')),
                ('is_agreed_inform', models.BooleanField(verbose_name='정보제공동의')),
                ('helped_at', models.DateTimeField(verbose_name='도움을 주기 시작한 시간')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='업로드 시각')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='수정 시각')),
            ],
        ),
        migrations.CreateModel(
            name='ReportImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='report/%Y/%m/%d', verbose_name='이미지')),
                ('report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='reports.Report', verbose_name='제보')),
            ],
        ),
    ]
