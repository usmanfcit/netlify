from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .serializers import MoviesSerializer
from ..models import Netflix
from .filters import MovieFilter
from users.api.permissions import IsStaff


class CreateMovieAPIView(generics.CreateAPIView):
    permission_classes = (IsStaff,)
    serializer_class = MoviesSerializer


class ListMoviesAPIView(generics.ListAPIView):
    queryset = Netflix.objects.all()
    serializer_class = MoviesSerializer
    filter_backends = [DjangoFilterBackend]
    permission_classes = [AllowAny]
    filterset_class = MovieFilter

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        if not queryset.exists():
            # Custom response representing that data is empty.
            return Response({"detail": "No movies found.", "data": []},
                            status=status.HTTP_404_NOT_FOUND)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class DeleteMoviesAPIView(generics.DestroyAPIView):
    permission_classes = (IsStaff,)
    queryset = Netflix.objects.all()

    def perform_destroy(self, instance):
        instance.delete()

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(
            {'message': f'{instance} was successfully deleted.'},
            status=status.HTTP_200_OK )

class MovieDetailAPIView(generics.RetrieveAPIView):
    queryset = Netflix.objects.all()
    serializer_class = MoviesSerializer


class MovieUpdateAPIView(generics.UpdateAPIView):
    queryset = Netflix.objects.all()
    permission_classes = (IsStaff,)
    serializer_class = MoviesSerializer