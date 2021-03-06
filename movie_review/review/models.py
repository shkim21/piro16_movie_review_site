from django.db import models

# Create your models here.

class Director(models.Model):
    name = models.CharField(max_length=30)
    age = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Actor(models.Model):
    name = models.CharField(max_length=30)
    age = models.CharField(max_length=30)

    def __str__(self):
        return self.name


GENRE_CHOICES= (('SF', 'SF'), ('Action', 'Action'), ('Comedy', 'Comedy'), ('Drama', 'Drama'), ('Fantasy', 'Fantasy'))
class Review(models.Model):
    title = models.CharField(max_length=30)
    release_date = models.IntegerField(default=1990)#개봉년도
    genre = models.CharField(max_length=50, choices=GENRE_CHOICES)
    rating = models.FloatField(default=0)#별점
    running_time = models.IntegerField(null=True, blank=True)
    content = models.TextField()#리뷰내용
    # director = models.CharField(max_length=20)
    # actor = models.CharField(max_length=255)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    actor = models.ManyToManyField(Actor, blank=True)
    image = models.ImageField(upload_to="poster", null=True, blank=True)

    def __str__(self):
        return self.title

