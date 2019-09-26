from rest_framework import viewsets
from .models import Report
from .serializers import ReportSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

report_query_parameter = openapi.Parameter('request', openapi.IN_QUERY,
                                           description="특정 Request의 Report를 list\nex) report/?request=1",
                                           type=openapi.TYPE_INTEGER)


class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        request_id = self.request.query_params.get('request', None)
        if request_id is not None:
            queryset = queryset.filter(request=request_id)
        return queryset

    @swagger_auto_schema(manual_parameters=[report_query_parameter])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
