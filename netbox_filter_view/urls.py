from django.urls import path

from . import views


urlpatterns = [
    path('', views.FilterView.as_view(), name='filter_view'),
]