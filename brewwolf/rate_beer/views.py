from rest_framework import permissions, viewsets

from rate_beer.models import Beer, Rating
from rate_beer.serializers import BeerSerializer, RatingSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Instance must have an attribute named `owner`.
        return obj.owner == request.user


@permission_classes([IsOwnerOrReadOnly])
class BeerViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `text` action.
    """

    queryset = Beer.objects.none()
    serializer_class = BeerSerializer

    def get_queryset(self):
        """
        This view should return a list of all the beers
        for the currently authenticated user.
        """
        user = self.request.user
        return Beer.objects.filter(owner=user)

class RatingViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `text` action.
    """

    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
