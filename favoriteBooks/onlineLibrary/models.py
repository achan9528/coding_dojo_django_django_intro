from django.db import models
import re

# Create your models here.

class userManager(models.Manager):
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

    def loginValidator(self,postData):
        errors = {}
        EMAIL_REGREX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGREX.match(postData['email']):
            errors['email'] = "Invalid email address!"
        if len(postData['password']) < 8:
            errors['password'] = "Password must be at least 8 characters!"
        return errors

class bookManager(models.Manager):
    def creationManager(self, postData):
        errors = {}
        if len(postData['title']) < 5:
            errors['title'] = "Title must be at least 5 characters!"
        if len(postData['desc']) < 5:
            errors['desc'] = "Descriptoin must be at least 5 characters!"
        return errors

# class Favorite(models.Model):
#     # bookID = models.ForeignKey(Book, related_name="favorites", on_delete=models.CASCADE)
#     # userID = models.ManyToManyField(User, related_name = "users")

#     def __str__ (self):
#         return f"Book ID: {self.bookID}, Users That Favorited: {self.userID}"

class User(models.Model):
    firstName = models.CharField(max_length=45)
    lastName = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=255)
    createdAt = models.DateTimeField(auto_now=True)
    updatedAt = models.DateTimeField(auto_now_add=True)
    objects = userManager()
    
    # Foreign Key Fields
    # books = list of books added by user

    # Many-To-Many Fields
    # favorites = list of favorited books. Many users can like many books

    def __str__ (self):
        return f"First Name: {self.firstName}, Last Name: {self.lastName}, Email: {self.email}, PW: {self.password}"

class Book(models.Model):
    title = models.CharField(max_length=45)
    desc = models.TextField(default="No Description")
    uploadedBy = models.ForeignKey(User, related_name = "books_uploaded", on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now=True)
    updatedAt = models.DateTimeField(auto_now_add=True)
    usersWhoLike = models.ManyToManyField(User, related_name="books_liked")
    objects = bookManager()

    def __str__ (self):
        return f"Title: {self.title}, Desc: {self.desc}, Uploaded By: {self.uploadedBy}"




