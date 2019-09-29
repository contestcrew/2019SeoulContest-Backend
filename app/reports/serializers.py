from rest_framework import serializers
from .models import Report, ReportImage
from request.serializers import UserNicknameSerializer


class ReportSerializer(serializers.ModelSerializer):
    author = UserNicknameSerializer(read_only=True)
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
        images = self.context.get("view").request.FILES
        user = self.context.get("request").user
        validated_data["author"] = user
        report = super().create(validated_data)
        for image in images.getlist('images'):
            ReportImage.objects.create(report=report, image=image)
        return report
