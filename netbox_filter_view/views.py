from django.views.generic import TemplateView


class FilterView(TemplateView):
    template_name = 'netbox_filter_view/filter_view.html'