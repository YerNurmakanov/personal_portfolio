from turtle import title
from django.db import models


class Projects(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    img = models.FilePathField(path='/img')
