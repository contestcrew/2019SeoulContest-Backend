from rest_framework import serializers
from .models import Report


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
        return super().create(validated_data)
