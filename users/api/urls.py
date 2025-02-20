from django.urls import path

from . import views

urlpatterns = [
    path("", views.UserListingAPIView.as_view()),
    path("login/", views.LoginAPIView.as_view()),
    path("register/", views.UserRegistrationAPIView.as_view()),
    path("user/<int:pk>", views.UserDetailAPIView.as_view()),
    path("user/delete/<int:pk>", views.UserDeleteAPIView.as_view()),
    path("user/update/<int:pk>", views.UserUpdateAPIView.as_view()),
    path("user/update/<int:pk>", views.UserUpdateAPIView.as_view()),
]