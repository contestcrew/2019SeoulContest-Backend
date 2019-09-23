from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "password",
            "nickname",
            "first_name",
            "last_name",
            "email"
            "phone",
            "manner_score",
            "citizen_score",
            "grade"
        )

    def create(self, validated_data):
        instance = self.Meta.model.objects.create_user(**validated_data)
        return instance
