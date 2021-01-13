from django.db import models
from datetime import datetime

# Create your models here.
class Show(models.Model):
    title = models.CharField(max_length=255)
    releaseDate = models.DateTimeField()
    desc = models.CharField(max_length=255, default="No Description")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Title: {self.title}, Release Date: {self.releaseDate}, Description: {self.desc}"

class Network(models.Model):
    name = models.CharField(max_length=255)
    shows = models.ManyToManyField(Show, related_name="networks")
    # desc = models.CharField(max_length=255, default="No Description")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Network Name: {self.name}"