from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    synopsis = models.TextField()
    author = models.CharField(max_length=100)
    read = models.BooleanField(default=False)
