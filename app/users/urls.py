from django.urls import path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from .views import UserViewSet

router = routers.SimpleRouter()
router.register(r'', UserViewSet)

urlpatterns = [
    path('get_token/', obtain_auth_token),
]

urlpatterns += router.urls
