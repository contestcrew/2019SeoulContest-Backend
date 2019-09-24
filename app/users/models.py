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
    GENDER = Choices((0, "MAN", _("MAN")), (1, "WOMAN", _("WOMAN")))
    nickname = models.CharField("별명", max_length=10, null=True, blank=True)
    email = models.EmailField("이메일", max_length=50, blank=True)
    phone = models.PositiveIntegerField("전화번호", null=True, blank=True)
    manner_score = models.IntegerField("매너점수", default=0)
    citizen_score = models.IntegerField("포인트 점수", default=0)
    grade = models.IntegerField(
        "사용자 등급", choices=USER_GRADE, default=USER_GRADE.GENERAL
    )
    gender = models.IntegerField("성별", choices=GENDER, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "사용자"
        verbose_name_plural = f"{verbose_name} 목록"
