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
    path('projects/', views.projects_view, name='projects'),
    path('project/<int:id>', views.project_view, name='project'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
