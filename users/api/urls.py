from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import UserViewSet

router = DefaultRouter()
router.register(r"", UserViewSet)

urlpatterns = [
    path("login/", views.LoginAPIView.as_view()),
    path("register/", views.UserRegistrationAPIView.as_view()),
    path("", include(router.urls))
]