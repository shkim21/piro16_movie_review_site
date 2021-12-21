from django.db import models

# Create your models here.

class Review(models.Model):
    title = models.CharField(max_length=30)
    release_date = models.IntegerField(default=1990)#개봉년도
    genre = models.CharField(max_length=50)
    rating = models.FloatField(default=0)#별점
    running_time = models.CharField(max_length=20)
    content = models.TextField()#리뷰내용
    director = models.CharField(max_length=20)
    actor = models.CharField(max_length=255)

    def __str__(self):
        return self.title