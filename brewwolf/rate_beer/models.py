from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Beer(models.Model):
    name = models.CharField(max_length=200)
    average_rating = models.IntegerField(default=0])
    brewery = models.CharField(max_length=200)
    beer_type = models.CharField(max_length=200)

class Rating(models.Model):
    beer = models.ForeignKey(Beer, on_delete=models.CASCADE)
    user = models.CharField(max_length=200)
    rating = models.IntegerField(default=5, validators=[MaxValueValidator(10), MinValueValidator(1)])
    created_date = models.DateTimeField(auto_now_add=True, blank=True)
    comment = models.CharField(max_length=256, blank=True)
