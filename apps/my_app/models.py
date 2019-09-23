from __future__ import unicode_literals
from django.db import models


class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['name']) < 3:
            errors["name"] = "user name should be at least 3 characters"
        if len(postData['email']) < 8:
            errors["email"] = "user email should be at least 8 characters"
        if len(postData['password']) < 8:
            errors["password"] = "password should be at least 8 characters"
        if User.objects.filter(email=postData['email']).exists():
            errors["email"]='An account with this email exist.'

        return errors

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True, error_messages={'unique': 'An account with this email exist.'})
    password = models.CharField(max_length=255)
    actived=models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()  


class Admin(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True, error_messages={'unique': 'An account with this email exist.'})
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()  


