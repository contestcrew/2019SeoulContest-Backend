from rest_framework import serializers
from .models import Report
from notifications.utils import push_notifications


class ReportSerializer(serializers.ModelSerializer):
    images = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Report
        fields = (
            "request",
            "author",
            "title",
            "content",
            "is_agreed_inform",
            "helped_at",
            "created_at",
            "updated_at",
            "images",
        )

    def create(self, validated_data):
        report = super().create(validated_data)
        recipient = report.request.author
        if recipient.devices.exists():
            push_notifications(recipient)
        return report
