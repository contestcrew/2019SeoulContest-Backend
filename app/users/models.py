from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils import Choices


class User(AbstractUser):
    USER_GRADE = Choices(
        (0, "GENERAL", _("GENERAL")),
        (1, "POLICE", _("POLICE")),
        (2, "FIREMAN", _("FIREMAN")),
        (3, "ADMIN", _("ADMIN")),
    )
    email = models.EmailField("이메일", max_length=50, blank=True)
    phone = models.PositiveIntegerField("전화번호", blank=True, null=True)
    manner_score = models.IntegerField("매너점수", default=0)
    point = models.IntegerField("포인트 점수", default=0)
    grade = models.IntegerField(
        "사용자 등급", choices=USER_GRADE, default=USER_GRADE.GENERAL
    )

    class Meta:
        verbose_name = "사용자"
        verbose_name_plural = f"{verbose_name} 목록"