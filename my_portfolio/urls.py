"""Defines url patterns for the website."""
from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'my_portfolio'
urlpatterns = [
    # The view page.
    path('', views.index, name='index'),
]
