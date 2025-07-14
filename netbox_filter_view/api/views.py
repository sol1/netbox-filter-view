from netbox.api.viewsets import NetBoxModelViewSet

from .. import models
from .serializers_ import filterviews


class FilterviewViewSet(NetBoxModelViewSet):
    queryset = models.Filterview.objects.all()
    serializer_class = filterviews.FilterviewSerializer