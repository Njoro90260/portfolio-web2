"""Defines url patterns for the website."""
from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from.views import UserProfileDetailView, UserProfileUpdateView

app_name = 'my_portfolio'
urlpatterns = [
    # The view page.
    path('', views.index, name='index'),
    path('projects/', views.projects_view, name='projects'),
    path('project/<int:id>', views.project_view, name='project'),
    path('client/<uuid:token>/testimonial/', views.submit_testimonial, name='submit_testimonial'),
    path('thank-you/', views.testimonial_thank_you, name='testimonial_thank_you'),
    path('profile/<str:username>/', UserProfileDetailView.as_view(), name='profile'),
    path('profile/<str:username>/edit/', UserProfileUpdateView.as_view(), name='edit_profile'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
