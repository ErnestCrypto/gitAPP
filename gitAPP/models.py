# Creating our models
from django.db import models


class Person(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    date = models.DateField(auto_now_add=True)
