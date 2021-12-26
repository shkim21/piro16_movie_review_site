from django.db import models

# Create your models here.

GENRE_CHOICES= (('SF', 'SF'), ('Action', 'Action'), ('Comedy', 'Comedy'), ('Drama', 'Drama'), ('Fantasy', 'Fantasy'))

class Review(models.Model):
    title = models.CharField(max_length=30)
    release_date = models.IntegerField(default=1990)#개봉년도
    genre = models.CharField(max_length=50, choices=GENRE_CHOICES)
    rating = models.FloatField(default=0)#별점
    running_time = models.IntegerField(null=True, blank=True)
    content = models.TextField()#리뷰내용
    director = models.CharField(max_length=20)
    actor = models.CharField(max_length=255)

    def __str__(self):
        return self.title