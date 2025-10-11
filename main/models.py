from django.db import models
from django.core.validators import MinValueValidator


class Country(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Club(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='clubs')
    president = models.CharField(max_length=255, blank=True, null=True)
    coach = models.CharField(max_length=255, blank=True, null=True)
    found_date = models.DateField(blank=True, null=True)

    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Player(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    number = models.PositiveSmallIntegerField()
    age = models.PositiveSmallIntegerField(null=True, blank=True)
    price = models.FloatField(validators=[MinValueValidator(0.0)])

    nation = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    club = models.ForeignKey(Club, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
