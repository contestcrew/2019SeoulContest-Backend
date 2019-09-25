from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Category, Request, PoliceOffice
from .serializers import PoliceOfficeSerializer, CategorySerializer, RequestSerializer
from rest_framework.decorators import action
from django.db.models import Q
import math


class PoliceOfficeViewSet(viewsets.ModelViewSet):
    queryset = PoliceOffice.objects.all()
    serializer_class = PoliceOfficeSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class RequestViewSet(viewsets.ModelViewSet):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.action == "boundary":
            latitude = float(self.request.query_params.get("latitude"))
            longitude = float(self.request.query_params.get("longitude"))
            variable_for_latitude = 1 / 54.979244565
            variable_for_longitude = 1 / 44.37
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
