from django.urls import include, path

from utilities.urls import get_model_urls

from . import views


urlpatterns = (
    path(
        'filterviews/',
        include(get_model_urls('netbox_filter_view', 'filterview', detail=False)),
    ),
    path(
        'filterviews/<int:pk>/',
        include(get_model_urls('netbox_filter_view', 'filterview')),
    ),
    path('render/', views.RenderFilterView.as_view(), name='filterview_render'),
)
