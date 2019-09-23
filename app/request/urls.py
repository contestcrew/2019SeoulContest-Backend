from rest_framework import routers
from .views import CategoryViewSet, RequestViewSet

router = routers.SimpleRouter()
router.register(r'category', CategoryViewSet)
router.register(r'', RequestViewSet)

urlpatterns = [
]

urlpatterns += router.urls
