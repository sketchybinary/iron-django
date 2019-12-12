from rest_framework import serializers

from rate_beer.models import Beer, Rating


class BeerSerializer(serializers.ModelSerializer):
    creator = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Beer
        fields = ("id", "name", "average_rating", "brewery", "beer_type", "creator")


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ("id", "beer", "user", "rating", "created_date", "comment")
