from django.shortcuts import render, redirect
from django.http import Http404
from django.urls import reverse
from .models import *


# Create your views here.
def index(request):
    """View function for the page."""
    projects = Project.objects.all()[:3]
    context = {'projects': projects}
    return render(request, 'my_portfolio/index.html', context)

def projects_view(request):
    """Fetch all projects."""
    all_projects = Project.objects.all()
    context = {'projects': all_projects}
    return render(request, 'my_portfolio/projects.html', context)