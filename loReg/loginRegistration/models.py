from django.db import models
import re

# Create your models here.
class UserManager(models.Manager):
    def registrationValidator(self, postData):
        errors = {}
        EMAIL_REGREX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(postData['firstName']) < 2:
            errors['firstName'] = "First Name should be at least 2 characters!"
        if len(postData['lastName']) < 2:
            errors['lastName'] = "Last Name should be at least 2 characters!"
        if not EMAIL_REGREX.match(postData['email']):
            errors['email'] = "Invalid email address!"
        if len(postData['password']) < 8:
            errors['password'] = "Password must be at least 8 characters!"
        if postData['password'] != postData['passwordConfirm']:
            errors['passwordConfirm'] = "Password does not match!"
        return errors
        
    def loginValidator(self, postData):
        errors = {}
        EMAIL_REGREX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGREX.match(postData['email']):
            errors['email'] = "Invalid email address!"
        if len(postData['password']) < 8:
            errors['password'] = "Password must be at least 8 characters!"
        return errors

class User(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

    def __str__(self):
        return f"First Name: {self.firstName}, Last Name: {self.lastName}, Email: {self.email}, PW: {self.pw_hash}"
