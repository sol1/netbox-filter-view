from netbox.forms import NetBoxModelForm
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