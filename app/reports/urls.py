from rest_framework import routers
from .views import ReportViewSet

router = routers.SimpleRouter()
router.register(r'', ReportViewSet)

urlpatterns = [
]

urlpatterns += router.urls
