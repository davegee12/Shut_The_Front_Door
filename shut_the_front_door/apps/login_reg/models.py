from __future__ import unicode_literals
from django.db import models
from django.core.exceptions import ObjectDoesNotExist
import re
from datetime import datetime
import bcrypt
date = datetime.now()

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]+[a-zA-Z-]*[a-zA-Z]+$')

# MODELS FOR LOGIN_REG APP
# Create your models here.

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        grab = User.objects.filter(email=postData['email'])
        if not NAME_REGEX.match(postData['first_name']):
            errors['first_name'] = "First name must be at least two characters in length containing only letters and cannot begin or end with a hyphen"
        if not NAME_REGEX.match(postData['last_name']):
            errors['last_name'] = "Last name must be at least two characters in length containing only letters and cannot begin or end with a hyphen"
        if len(postData['email']) < 1:
            errors['email'] = "E-mail address is empty. Enter e-mail."
        elif not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid e-mail address. Enter e-mail."
        if len(grab) > 0:
        # if {'email' : postData['email']} in grab:
            errors['email'] = "The e-mail address entered already exists in the database."
        if len(postData['password']) < 8:
            errors['password'] = "Password must be at least eight characters in length"
        if postData['password'] != postData['pw_confirmation']:
            errors['pw_confirmation'] = "Passwords do not match!"
        if errors:
            errors['pw_confirmation'] = "Re-enter Password and Password Confirmation."
        return errors

    def login_validator(self, postData):
        errors = {}
        user = User.objects.filter(email=postData['email'])
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid e-mail address. Enter e-mail."
        if len(user) == 0:
            errors['email'] = "Email is not registered. Please register"
        else:
            if not bcrypt.checkpw(postData['login_password'].encode(), user[0].password.encode()):
                errors['login_password'] = "Wrong password!"
                print("%"*50)
                print(postData['login_password'])
            if len(postData['login_password']) < 8:
                errors['login_password'] = "Password should be at least 8 characters"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    
    
    def __repr__(self):
        return f"<User object: {self.id} ({self.email})>"