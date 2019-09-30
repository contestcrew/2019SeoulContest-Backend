from django.db import models
from django.contrib.auth import get_user_model
from request.models import Request

User = get_user_model()


class Report(models.Model):
    request = models.ForeignKey(
        Request, related_name="reports", on_delete=models.CASCADE, verbose_name="의뢰"
    )
    author = models.ForeignKey(
        User, related_name="reports", on_delete=models.CASCADE, verbose_name="작성자"
    )
    title = models.CharField("제목", max_length=100)
    content = models.TextField("내용")
    is_agreed_inform = models.BooleanField("정보제공동의")
    helped_at = models.DateTimeField("도움을 주기 시작한 시간")
    created_at = models.DateTimeField("업로드 시각", auto_now_add=True)
    updated_at = models.DateTimeField("수정 시각", auto_now=True)
    is_select = models.BooleanField("선택 여부 확인", default=False)


class ReportImage(models.Model):
    report = models.ForeignKey(
        Report, related_name="images", on_delete=models.CASCADE, verbose_name="제보"
    )
    image = models.ImageField(upload_to="report/%Y/%m/%d", verbose_name="이미지")

    def __str__(self):
        return self.image.url
