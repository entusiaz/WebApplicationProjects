from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=225)
    email = models.EmailField()
    age = models.IntegerField()
    salary = models.CharField(max_length=60)
    location = models.CharField(max_length=125)


