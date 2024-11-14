from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.urls import reverse
from .models import *
from .forms import ClientForm


# Create your views here.
def index(request):
    """View function for the page."""
    projects = Project.objects.all()[:3]
    services = Service.objects.all()
    clients = Client.objects.all()
    """Clients Testimonial."""
    client_testimonial = None
    # Client to add testimonial.
    if request.method != 'POST':
        # No data submitted; create a blank form
        form = ClientForm()
    else:
        # Post data submitted; process data.
        form = ClientForm(data=request.POST)
        if form.is_valid():
            client_testimonial = form.save(commit=False)
            client_testimonial.save()
            # Redirect to prevent duplicate submission
            return redirect('index')
    context = {
        'projects': projects,
        'services': services, 
        'clients': clients,
        'client_testimonial': client_testimonial,
        'form': form
        }
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

