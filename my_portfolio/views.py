from django.shortcuts import render, redirect, get_object_or_404
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

def project_view(request, id):
    """page for a specific project."""
    project = get_object_or_404(Project, id=id)
    context = {'project': project}
    return render(request, 'my_portfolio/project.html', context)

