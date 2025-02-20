import django_filters
from netlify_movies.models import Netflix


class MovieFilter(django_filters.FilterSet):
    movie_name = django_filters.CharFilter(field_name="movie_name", lookup_expr="icontains")
    max_rating = django_filters.NumberFilter(field_name="rating", lookup_expr="lte") ,
    min_rating = django_filters.NumberFilter(field_name="rating", lookup_expr="gte"),
    category = django_filters.CharFilter(field_name="category", lookup_expr="contains")
    director = django_filters.CharFilter(field_name="director", lookup_expr="contains")
    year_released = django_filters.CharFilter(field_name="year_released", lookup_expr="icontains")
    description = django_filters.CharFilter(field_name="description", lookup_expr="icontains")

    class Meta:
        model = Netflix
        fields = ['movie_name', 'rating', 'category', 'director', 'year_released', 'description']
