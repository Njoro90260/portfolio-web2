from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.urls import reverse
from .models import *
from .forms import ClientForm
from django.http import JsonResponse


# Create your views here.
def index(request):
    """View function for the page."""
    projects = Project.objects.all()[:3]
    services = Service.objects.all()
    clients = Client.objects.all()
    context = {
        'projects': projects,
        'services': services, 
        'clients': clients,
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

def client_detail(request, client_id):
    client = get_object_or_404(Client, unique=client_id)
    return render(request, 'client_detail.html', {'client': client})

def submit_testimonial(request, toke)
# def add_testimonial(request):
#     """Client to add testimonial """
#     if request.method == 'POST':
#         client_id = request.POST.get('client_id')
#         testimonial_text = request.POST.get('testimonial')

#         try:
#             # Fetch the client and update the testimonial
#             client = Client.objects.get(id=client_id)
#             client.testimonial = testimonial_text
#             client.save()
#             return JsonResponse({'status': 'success', 'message': 'Testimonial added successfully.'})
#         except Client.DoesNotExist:
#             return JsonResponse({'status': 'error', 'message': 'Client not found'})
#     else:
#         return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})