from django.conf import settings
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Category(models.Model):
    pass


class Request(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='작성자')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='카테고리')
    title = models.CharField('제목', maxlength=100)
    content = models.TextField('의뢰내용')
    offer_point = models.PositiveIntegerField('추가제공포인트', default=0)
    latitude = models.FloatField('위도', blank=True)
    longitude = models.FloatField('경도', blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class PostImage(models.Model):
    request = models.ForeignKey(
        Request,
        related_name='images',
        on_delete=models.CASCADE,
    )
    image = models.ImageField(upload_to='request', verbose_name='이미지')

    class Meta:
        verbose_name = '요청'
        verbose_name_plural = f'{verbose_name} 목록'
        ordering = ['-pk']
