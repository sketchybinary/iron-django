from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from rate_beer.models import Beer, Rating
from rate_beer.serializers import BeerSerializer, RatingSerializer


class BeerViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `text` action.
    """
    queryset = Beer.objects.all()
    serializer_class = BeerSerializer

    
class RatingViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `text` action.
    """
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
