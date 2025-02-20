from django.db import models


class Netflix(models.Model):
    movie_name = models.CharField(max_length=50, unique=True)
    category = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=128, blank=True, null=True)
    year_released = models.CharField(max_length=50, blank=True, null=True)
    director = models.CharField(max_length=50, blank=True, null=True)
    rating = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)

    def __str__(self):
        return self.movie_name

    class Meta:
        verbose_name_plural = "Netflix"