from django.db.models import Q
from netbox.filtersets import NetBoxModelFilterSet

from .models import Filterview


class FilterviewFilterSet(NetBoxModelFilterSet):
    class Meta:
        model = Filterview
        fields = (
            'id',
            'name',
            'description',
            'filter_url',
        )

    def search(self, queryset, name, value):
        query = Q(
            Q(name__icontains=value)
            | Q(description__icontains=value)
            | Q(filter_url__icontains=value)
        )
        return queryset.filter(query)