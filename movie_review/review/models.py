from django.db import models

# Create your models here.

class Review(models.Model):
    title = models.CharField(max_length=30)
    release_date = models.IntegerField(default=1990)
    genre = models.CharField(max_length=50)
    rating = models.FloatField(default=0)
    running_time = models.CharField(max_length=20)
    content = models.TextField()
    director = models.CharField(max_length=20)
    actor = models.CharField(max_length=255)
