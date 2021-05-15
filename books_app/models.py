from django.db import models
from login_app.models import User

# Create your models here.
class BookManager(models.Manager):
    def validator(self,post_data):
        errors={}
        if len(post_data['title'])<1:
            errors['title']="Please have at least 1 character for title."
        if len(post_data['desc'])<5:
            errors['desc']="Decription must be at least 5 characters long."
        return errors

class Book(models.Model):
    title=models.CharField(max_length=255)
    desc=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    added_by=models.ForeignKey(User,related_name="books_uploaded", on_delete=models.CASCADE)
    users_liked_by=models.ManyToManyField(User, related_name="books_liked")
    objects=BookManager()
