from rest_framework import serializers

from netbox.api.serializers import NetBoxModelSerializer

from netbox_filter_view.models import Filterview

__all__ = ('FilterviewSerializer',)


class FilterviewSerializer(NetBoxModelSerializer):
    filter_url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_filter_view-api:filterview-detail'
    )

    class Meta:
        model = Filterview
        fields = (
            'pk',
            'id',
            'name',
            'description',
            'filter_url',
            'tags',
        )
        brief_fields = ('id', 'name', 'description', 'filter_url')