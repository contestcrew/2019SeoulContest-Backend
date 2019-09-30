from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import PoliceOffice, Category, Request, RequestImage

User = get_user_model()


class UserNicknameSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "nickname")


class PoliceOfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PoliceOffice
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class RequestSerializer(serializers.ModelSerializer):
    images = serializers.StringRelatedField(many=True, read_only=True)
    status = serializers.ChoiceField(choices=Request.REQUEST_STATUS, required=False)
    status_display = serializers.SerializerMethodField()
    author = UserNicknameSerializer(read_only=True)
    category_score = serializers.IntegerField(source="category.score", read_only=True)

    class Meta:
        model = Request
        fields = (
            "id",
            "category",
            "police_office",
            "author",
            "title",
            "content",
            "status",
            "status_display",
            "category_score",
            "score",
            "main_address",
            "detail_address",
            "latitude",
            "longitude",
            "occurred_at",
            "created_at",
            "updated_at",
            "images",
        )

    def get_status_display(self, obj):
        return obj.get_status_display()

    def create(self, validated_data):
        images = self.context.get("view").request.FILES
        user = self.context.get("request").user
        validated_data["author"] = user
        request = super().create(validated_data)
        for image in images.getlist("images"):
            RequestImage.objects.create(request=request, image=image)
        return request
