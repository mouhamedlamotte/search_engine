from collections.abc import Iterable
from django.db import models

# Create your models here.

class filmGenre(models.Model):
    name = models.CharField(max_length=50)
    
    # def __str__(self):
    #     self.name


class Film(models.Model):
    adult = models.BooleanField()
    genre_ids = models.ManyToManyField(filmGenre, null=True)
    original_language = models.CharField(max_length=20)
    original_title = models.CharField(max_length=150)
    overview = models.TextField()
    popularity = models.FloatField()
    poster_path = models.CharField(max_length=200)
    release_date = models.DateField()
    title = models.CharField(max_length=150)
    vote_average = models.FloatField()
    vote_count = models.IntegerField()
    
    def __str__(self):
        return self.title
    
    