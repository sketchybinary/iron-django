from rest_framework import serializers

from rate_beer.models import Beer, Rating


class BeerSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Beer
        fields = (
            "id",
            "url",
            "name",
            "average_rating",
            "brewery",
            "beer_type",
            "owner",
        )


class RatingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Rating
        fields = ("id", "url", "beer", "user", "rating", "created_date", "comment")
