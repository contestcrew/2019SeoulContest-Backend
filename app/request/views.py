from rest_framework import viewsets
from .models import Category, Request
from .serializers import CategorySerializer, RequestSerializer
from rest_framework.decorators import action
from django.db.models import Q
import math


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class RequestViewSet(viewsets.ModelViewSet):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.action == "boundary":
            latitude = float(self.request.query_params.get("latitude"))
            longitude = float(self.request.query_params.get("longitude"))
            variable_for_latitude = 1 / 111.2
            variable_for_longitude = abs(math.cos(latitude * (math.pi / 180.0)))
            boundary = {
                "max_latitude": latitude + variable_for_latitude,
                "min_latitude": latitude - variable_for_longitude,
                "max_longitude": longitude + variable_for_longitude,
                "min_longitude": longitude - variable_for_longitude,
            }
            queryset = Request.objects.filter(
                Q(latitude__lte=boundary["max_latitude"])
                & Q(latitude__gte=boundary["min_latitude"])
                & Q(longitude__lte=boundary["max_longitude"])
                & Q(longitude__gte=boundary["min_longitude"])
            )
        return queryset

    @action(methods=["get"], detail=False)
    def boundary(self, request, *args, **kwargs):
        return self.list(request)
