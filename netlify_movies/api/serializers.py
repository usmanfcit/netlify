from rest_framework import serializers

from ..models import Netflix


class MoviesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Netflix
        fields = "__all__"