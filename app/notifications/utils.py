from django.conf import settings
from django.contrib.auth import get_user_model
from pyfcm import FCMNotification
from .models import MobileDevice

DEFAULT_MESSAGE = "새로운 제보가 도착했습니다."
DEFAULT_TITLE = "FirstCitizen"

User = get_user_model()


def push_notifications(recipient, title=DEFAULT_TITLE, body=DEFAULT_MESSAGE):
    assert isinstance(recipient, User)
    fcm = FCMNotification(api_key=settings.FCM_API_KEY)
    extra_kwargs = {
        "mutable_content": True,
    }

    return fcm.notify_multiple_devices(
        registration_ids=[device.token for device in recipient.devices],
        message_title=title,
        message_body=body,
        content_available=True,
        extra_kwargs=extra_kwargs
    )
