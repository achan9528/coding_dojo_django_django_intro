from django.db import models
from loginRegistration.models import User

# Create your models here.
class MessageManager(models.Manager):
    def messageValidator(self, postData):
        errors = {}
        if len(postData['messageText']) < 1:
            errors['messageText'] = "You're not submitting anything - try typing a message!"
        
        return errors

class CommentManager(models.Manager):
    def commentValidator(self, postData):
        errors = {}
        if len(postData['comment']) < 1:
            errors['comment'] = "You're not submitting anything - try typing a message!"
        
        return errors

class Message(models.Model):
    user = models.ForeignKey('loginRegistration.User', related_name = "messages", on_delete=models.CASCADE)
    message = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = MessageManager()

    def __str__(self):
        return f"User: {self.user}, Message: {self.message}"

class Comment(models.Model):
    user = models.ForeignKey('loginRegistration.User', related_name = "comments", on_delete=models.CASCADE)
    message = models.ForeignKey(Message, related_name = "comments", on_delete=models.CASCADE)
    comment = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CommentManager()

    def __str__(self):
        return f"User: {self.user}, Comment: {self.comment}"


