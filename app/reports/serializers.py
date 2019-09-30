from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Report, ReportImage
from notifications.utils import push_notifications

User = get_user_model()


class UserNicknameScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'nickname', 'manner_score')


class ReportSerializer(serializers.ModelSerializer):
    author = UserNicknameScoreSerializer(read_only=True)
    images = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Report
        fields = (
            "id",
            "request",
            "author",
            "title",
            "content",
            "is_agreed_inform",
            "helped_at",
            "created_at",
            "updated_at",
            "images",
            "is_select",
        )

    def create(self, validated_data):
        images = self.context.get("view").request.FILES
        user = self.context.get("request").user
        validated_data["author"] = user
        report = super().create(validated_data)
        for image in images.getlist('images'):
            ReportImage.objects.create(report=report, image=image)
        recipient = report.request.author
        if recipient.devices.exists():
            push_notifications(recipient)
        return report
