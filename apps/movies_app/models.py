from __future__ import unicode_literals
from django.db import models
import re
import datetime
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
class UserManager(models.Manager):
    def user_validator(self, postData):
        errors = {}
        if len(postData['name']) < 2:
            errors["name"] = "First name should be more than 2 characters"
        if len(postData['username']) < 2:
            errors["username"] = "Username should be more than 2 characters"
        if not re.match(EMAIL_REGEX, postData['email'] ):
            errors["email"] = "Email needs to be valid"
        if len(postData['password']) < 8:
            errors["password"] = "Password should be 8 charcters or more"
        if postData['password'] != postData['confirm_password']:
            errors['confirm_password'] = 'Password has to match confirmation'
        if str(postData['birth']) > str(datetime.date.today()):
            errors['birth'] = 'You havent been born yet?'
        if len(postData['zipCode']) != 5:
            errors['zipCode'] = 'Please enter a valid zip code'
        return errors

class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    birthday = models.DateField()
    zipCode = models.IntegerField()
    objects = UserManager()

class Showtime(models.Model):
    movieID = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    theatre = models.CharField(max_length=255)
    users = models.ManyToManyField(User, related_name='Users_attending')
