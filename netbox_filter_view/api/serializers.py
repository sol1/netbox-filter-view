from netbox.api.serializers import NetBoxModelSerializer
from rest_framework import serializers

from netbox_filter_view.models import Filterview

__all__ = ('FilterviewSerializer',)


class FilterviewSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_filter_view-api:filterview-detail'
    )
    filter_url = serializers.CharField(allow_blank=False)

    class Meta:
        model = Filterview
        fields = (
            'id',
            'url',
            'name',
            'description',
            'filter_url',
            'created',
            'last_updated',
            'custom_fields',
            'tags',
        )
        brief_fields = ('id', 'url', 'name', 'filter_url')