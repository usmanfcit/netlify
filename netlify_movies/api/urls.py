from django.urls import path

from . import views

urlpatterns = [
    path("", views.ListMoviesAPIView.as_view()),
    path("create/", views.CreateMovieAPIView.as_view()),
    path("delete/<int:pk>", views.DeleteMoviesAPIView.as_view()),
    path("get/<int:pk>", views.MovieDetailAPIView.as_view()),
    path("update/<int:pk>", views.MovieUpdateAPIView.as_view())
]