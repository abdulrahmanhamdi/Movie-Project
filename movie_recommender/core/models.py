# core/models.py

from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.title
