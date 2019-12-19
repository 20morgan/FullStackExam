from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=250)
    genre = models.CharField(max_length=250)
    rating = models.IntegerField()
    director = models.CharField(max_length=250)

    def get_absolute_url(self):
        return f"/movies/"

    def __str__(self):
        return self.title
