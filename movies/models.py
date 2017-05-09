from django.db import models


class MovieInfo(models.Model):
    movie_title = models.CharField(max_length=400)
    movie_poster = models.CharField(max_length=1000)
    genre = models.CharField(max_length=400)
    director = models.CharField(max_length=400)
    starring = models.CharField(max_length=500)
    year = models.IntegerField(default=1900)
    summary = models.CharField(max_length=2000, default='No description found')

    def __str__(self):
        return self.movie_title + "-" + self.genre


class Comment(models.Model):
    post = models.ForeignKey(MovieInfo, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()

    def __str__(self):
        return self.text
