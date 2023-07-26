# models.py
from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=100)

class City(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

class Street(models.Model):
    name = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

class Position(models.Model):
    title = models.CharField(max_length=100)

class Department(models.Model):
    name = models.CharField(max_length=100)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
