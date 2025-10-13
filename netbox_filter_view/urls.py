from django.urls import include, path
from utilities.urls import get_model_urls

from . import views

urlpatterns = (
    # Ensure the import route name exists for the list page action button
    path('filterviews/import/', views.FilterviewBulkImportView.as_view(), name='filterview_import'),
    path(
        'filterviews/',
        include(get_model_urls('netbox_filter_view', 'filterview', detail=False)),
    ),
    path(
        'filterviews/<int:pk>/',
        include(get_model_urls('netbox_filter_view', 'filterview')),
    ),
    path('filterviews/<int:pk>/render/', views.RenderFilterViewURL.as_view(), name='filterview_render_url'),
    path('render/', views.RenderFilterView.as_view(), name='filterview_render'),
)
