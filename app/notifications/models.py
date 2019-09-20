from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class MobileDevice(models.Model):
    owner = models.ForeignKey(User, related_name='devices')
    platform = models.CharField(max_length=20, choices=(('iOS', 'iOS'), ('Android', 'Android'),))
    token = models.TextField()


class MobileNotification(models.Model):
    recipient = models.ForeignKey(User, related_name='notifications', on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=True, blank=True)
    message = models.TextField()
    status = models.CharField(max_length=10, default='unread')
