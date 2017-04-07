from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User



# Create your models here.

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

class login(models.Model):
    user_name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

