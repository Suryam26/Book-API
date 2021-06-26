from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    title = models.CharField(max_length=256)
    synopsis = models.TextField()
    cover = models.ImageField(upload_to='cover/')
    author = models.ForeignKey(
        User, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
