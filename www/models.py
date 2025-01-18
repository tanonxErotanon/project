from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    number = models.CharField(max_length=15)
    point = models.IntegerField()

