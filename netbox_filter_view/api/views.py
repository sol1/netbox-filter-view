from netbox.api.viewsets import NetBoxModelViewSet

from .. import models
from .serializers import FilterviewSerializer


class FilterviewViewSet(NetBoxModelViewSet):
    queryset = models.Filterview.objects.all()
    serializer_class = FilterviewSerializer