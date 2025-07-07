import django_tables2 as tables
from django.utils.html import format_html

from netbox.tables import NetBoxTable, columns

from . import models


class FilterviewTable(NetBoxTable):
    filter_url = tables.TemplateColumn(
        template_code="""
            <a href="{% url 'plugins:netbox_filter_view:filterview_render' %}?{{ record.filter_url|safe }}">
                {{ record.filter_url }}
            </a>
        """,
        orderable=False,
        verbose_name="Filter URL",
    )
    comments = columns.MarkdownColumn()
    tags = columns.TagColumn()

    class Meta(NetBoxTable.Meta):
        model = models.Filterview
        fields = (
            'pk',
            'id',
            'name',
            'description',
            'filter_url',
            'tags',
            'comments',
        )
        default_columns = (
            'name',
            'description',
            'filter_url',
        )
