from django.conf import settings
from django.db import models
from django.utils import timezone


class Binatang(models.Model):
    name = models.CharField(max_length=200)
    images = models.CharField(max_length=200)
    description = models.TextField()
    species = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name