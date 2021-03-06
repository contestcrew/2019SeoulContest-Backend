from django.contrib.auth import get_user_model
from rest_framework import serializers
from notifications.models import MobileDevice

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    device_token = serializers.CharField(max_length=200, write_only=True)
    request_count = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "password",
            "nickname",
            "first_name",
            "last_name",
            "email",
            "phone",
            "grade",
            "gender",
            "manner_score",
            "citizen_score",
            "device_token",
            "request_count",
        )

    def get_request_count(self, obj):
        request_count = obj.requests.exclude(status="complete").count()
        return request_count

    def create(self, validated_data):
        device_token = validated_data.pop("device_token")
        instance = self.Meta.model.objects.create_user(**validated_data)
        MobileDevice.objects.create(owner=instance, token=device_token)

        return instance
