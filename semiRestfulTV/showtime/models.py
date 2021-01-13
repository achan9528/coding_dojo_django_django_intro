from django.db import models
from datetime import datetime

# Create your models here.
class ShowManager(models.Manager):
    def validator(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors["title"] = "Show title should be at least 2 characters!"
        if len(postData['network']) < 3:
            errors["network"] = "Network name should be at least 3 characters!"
        if len(postData['desc']) < 10:
            errors["desc"] = "Description should be at least 10 characters!"
        return errors

class Show(models.Model):
    title = models.CharField(max_length=255)
    releaseDate = models.DateTimeField()
    desc = models.CharField(max_length=255, default="No Description")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()

    def __str__(self):
        return f"Title: {self.title}, Release Date: {self.releaseDate}, Description: {self.desc}"

class Network(models.Model):
    name = models.CharField(max_length=255)
    shows = models.ManyToManyField(Show, related_name="networks")
    # desc = models.CharField(max_length=255, default="No Description")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # objects = ShowManager()

    def __str__(self):
        return f"Network Name: {self.name}"




# Inside your app's models.py file
# from django.db import models
# Our custom manager!
# No methods in our new manager should ever receive the whole request object as an argument! 
# (just parts, like request.POST)
# class BlogManager(models.Manager):
#     def basic_validator(self, postData):
#         errors = {}
#         # add keys and values to errors dictionary for each invalid field
#         if len(postData['name']) < 5:
#             errors["name"] = "Blog name should be at least 5 characters"
#         if len(postData['desc']) < 10:
#             errors["desc"] = "Blog description should be at least 10 characters"
#         return errors
