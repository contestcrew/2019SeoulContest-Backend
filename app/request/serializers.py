from rest_framework import serializers
from .models import Category, Request, RequestImage


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class RequestSerializer(serializers.ModelSerializer):
    images = serializers.StringRelatedField(many=True, read_only=True)
    status = serializers.CharField(required=False)
    status_display = serializers.CharField(source='get_status_display', read_only=True)

    class Meta:
        model = Request
        fields = ('category',
                  'author',
                  'title',
                  'content',
                  'status',
                  'status_display',
                  'score',
                  'main_address',
                  'detail_address',
                  'latitude',
                  'longitude',
                  'occurred_at',
                  'images',)

    def create(self, validated_data):
        images = self.context.get('view').request.FILES
        request = super().create(validated_data)
        for image in images.getlist('images'):
            RequestImage.objects.create(request=request, image=image)
        return request
