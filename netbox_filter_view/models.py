from django.db import models
from django.urls import reverse
from netbox.models import NetBoxModel


class Filterview(NetBoxModel):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    filter_url = models.TextField(
        verbose_name="Filter URL",
        help_text="Full filter URL containing an API call. Starts with ?api_path=...",
    )

    clone_fields = ['name', 'filter_url']

    class Meta:
        ordering = ['name']
        verbose_name = "Filter View"
        verbose_name_plural = "Filter Views"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plugins:netbox_filter_view:filterview', args=[self.pk])
