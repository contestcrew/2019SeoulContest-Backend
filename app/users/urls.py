from django.urls import path
from rest_framework import routers
from .views import UserViewSet
from users import views

router = routers.SimpleRouter()
router.register(r"", UserViewSet)

urlpatterns = [path("get_token/", views.CustomTokenAuth.as_view())]

urlpatterns += router.urls
