from rest_framework import serializers

from netlify_movies.models import Netflix


class MoviesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Netflix
        fields = [
            "id",
            "movie_name",
            "category",
            "description",
            "year_released",
            "director",
            "rating"
        ]