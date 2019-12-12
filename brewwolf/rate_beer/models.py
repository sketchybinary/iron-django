import uuid

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.auth.models import User


class Beer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    brewery = models.CharField(max_length=200)
    beer_type = models.CharField(max_length=200)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    @property
    def average_rating(self):
        ratings = Rating.objects.filter(beer=self.id)
        if len(ratings) == 0:
            return "N/A"

        return sum([r.rating for r in ratings]) / len(ratings)


class Rating(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    beer = models.ForeignKey(Beer, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(
        default=5, validators=[MaxValueValidator(5), MinValueValidator(1)]
    )
    created_date = models.DateTimeField(auto_now_add=True, blank=True)
    comment = models.CharField(max_length=256, blank=True)
    public = models.BooleanField(default=False)
