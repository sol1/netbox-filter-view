from netbox.forms import (NetBoxModelFilterSetForm, NetBoxModelForm,
                          NetBoxModelImportForm)
from utilities.forms.fields import CommentField
from utilities.forms.rendering import FieldSet

from . import models


class FilterviewForm(NetBoxModelForm):
    comments = CommentField()

    fieldsets = (FieldSet('name', 'description', 'filter_url', name='Filter View'),)
    class Meta:
        model = models.Filterview
        fields = (
            'name',
            'description',
            'filter_url',
            'comments',
            'tags',
        )


class FilterviewFilterForm(NetBoxModelFilterSetForm):
    model = models.Filterview
    fieldsets = (
        FieldSet('q', 'filter_id', 'tags'),
    )


class FilterviewImportForm(NetBoxModelImportForm):
    class Meta:
        model = models.Filterview
        fields = (
            'name',
            'description',
            'filter_url',
        )
