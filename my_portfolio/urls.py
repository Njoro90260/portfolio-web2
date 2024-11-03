"""Defines url patterns for the website."""
from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

app_name = 'my_portfolio'
urlpatterns = [
    # The view page.
    path('', views.index, name='index'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
