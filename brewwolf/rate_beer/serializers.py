from rest_framework import serializers

from rate_beer.models import Beer, Rating


class BeerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Beer
        fields = ('id', 'name', 'average_rating', 'brewery', 'beer_type')


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id', 'beer', 'user', 'rating', 'created_date', 'comment')
