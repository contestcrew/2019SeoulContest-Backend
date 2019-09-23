from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from model_utils import Choices

User = get_user_model()


class Category(models.Model):
    name = models.CharField('이름', max_length=30)
    score = models.PositiveIntegerField('점수', default=0)
    image = models.ImageField(upload_to='category')


class Request(models.Model):
    REQUEST_STATUS = Choices(
        (0, "REQUEST", _("REQUEST")),
        (1, "PROGRESS", _("PROGRESS")),
        (2, "COMPLETE", _("COMPLETE")),
    )
    category = models.ForeignKey(Category, related_name='requests', on_delete=models.CASCADE, verbose_name='카테고리')
    author = models.ForeignKey(User, related_name='requests', on_delete=models.CASCADE, verbose_name='작성자')
    title = models.CharField('제목', max_length=100)
    content = models.TextField('내용')
    status = models.IntegerField('상태', choices=REQUEST_STATUS, default=REQUEST_STATUS.REQUEST)
    score = models.PositiveIntegerField('점수', default=0)
    main_address = models.CharField('메인 주소', max_length=30)
    detail_address = models.CharField('상세 주소', max_length=50)
    latitude = models.FloatField('위도', blank=True)
    longitude = models.FloatField('경도', blank=True)
    occurred_at = models.DateField('발생 시각')
    created_at = models.DateTimeField('업로드 시각', auto_now_add=True)
    updated_at = models.DateTimeField('수정 시각', auto_now=True)


class RequestImage(models.Model):
    request = models.ForeignKey(Request, related_name='images', on_delete=models.CASCADE, verbose_name='의뢰')
    image = models.ImageField(upload_to='request/%Y/%m/%d', verbose_name='이미지')
