from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import TemplateView
from netbox.views import generic
from utilities.views import register_model_view

from . import forms, models, tables

__all__ = (
    'FilterviewView',
    'FilterviewListView',
    'FilterviewEditView',
    'FilterviewDeleteView',
    'RenderFilterView',
    'RenderFilterViewURL',
)


@register_model_view(models.Filterview)
class FilterviewView(generic.ObjectView):
    queryset = models.Filterview.objects.all()


@register_model_view(models.Filterview, 'list', path='', detail=False)
class FilterviewListView(generic.ObjectListView):
    queryset = models.Filterview.objects.all()
    table = tables.FilterviewTable


@register_model_view(models.Filterview, 'edit')
@register_model_view(models.Filterview, 'add', detail=False)
class FilterviewEditView(generic.ObjectEditView):
    queryset = models.Filterview.objects.all()
    form = forms.FilterviewForm


@register_model_view(models.Filterview, 'delete')
class FilterviewDeleteView(generic.ObjectDeleteView):
    queryset = models.Filterview.objects.all()


class RenderFilterView(TemplateView):
    template_name = 'netbox_filter_view/filter_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query_params'] = self.request.GET.urlencode()
        context['filter_url'] = self.request.GET.get('filter_url', '')
        return context


class RenderFilterViewURL(TemplateView):
    template_name = 'netbox_filter_view/filterview_render_url.html'

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        obj = models.Filterview.objects.get(pk=pk)
        filter_url = obj.filter_url
        redirect_url = f"{reverse('plugins:netbox_filter_view:filterview_render')}?{filter_url}"
        return redirect(redirect_url)
