from netbox.api.routers import NetBoxRouter

from . import views

app_name = 'netbox_filter_view'

router = NetBoxRouter()

router.register('filterviews', views.FilterviewViewSet)

urlpatterns = router.urls