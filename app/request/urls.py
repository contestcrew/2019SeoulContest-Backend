from rest_framework import routers
from .views import CategoryViewSet, RequestViewSet, PoliceOfficeViewSet

router = routers.SimpleRouter()
router.register(r'category', CategoryViewSet)
router.register(r'', RequestViewSet)
router.register(r'police', PoliceOfficeViewSet)

urlpatterns = [
]

urlpatterns += router.urls
