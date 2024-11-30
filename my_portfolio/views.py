from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.contrib import messages
from django.urls import reverse
from .models import *
from .forms import *
from django.core.mail import send_mail
from decouple import config

# Create your views here.
def index(request):
    """View function for the page."""
    projects = Project.objects.all()[:3]
    services = Service.objects.all()
    clients = Client.objects.all()
    client_instance = Client.objects.first()
    testimonials = Testimonial.objects.all()

    def handle_contact_form():
        """Contact Form Handling Function."""
        if request.method == 'POST':
            form = ContactMessageForm(request.POST)
            if form.is_valid():
                message = form.save()
                # Send email notification.
                send_mail(
                    subject=f"New Contact Message from {message.name}",
                    message = f"You've recieved a new message:\n\n"
                        f"Name: {message.name}\n"
                        f"Email: {message.email}\n"
                        f"Subject: {message.subject}\n\n"
                        f"{message.message}",
                from_email= config('EMAIL_HOST_USER'),
                recipient_list= config('RECIPIENT_LIST').split(','),
                )
                return True, "Your message has been sent successfully!" 
            else:
                messages.error(request, "Whoops! There was an error sending your message. Please Try again")
        return False
    
    def newsletter_subscribe():
        if request.method == 'POST':
            form = NewsletterSubscriptionForm(request.POST)
            if form.is_valid():
                email = form.cleaned_data['email']
                subscription, created = NewsletterSubscription.objects.get_or_create(email=email)
                if created:
                    messages.success(request, "Thank you for subscribing!")
                else:
                    messages.info(request, "You're already subscribed.")
                return redirect('my_portfolio:index')
        else:
            return NewsletterSubscriptionForm()
        
    newsletter = newsletter_subscribe()
    contact_form = ContactMessageForm()
    form_submitted = handle_contact_form()
    if form_submitted:
        return redirect('my_portfolio:index')

    context = {
        'projects': projects,
        'services': services, 
        'clients': clients,
        'token': client_instance.unique_token,
        'testimonials': testimonials,
        'contact_form': contact_form,
        'newsletter': newsletter
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

def submit_testimonial(request, token):
    client = get_object_or_404(Client, unique_token=token)
    testimonials = Testimonial.objects.filter(client=client)
    if request.method == 'POST':
        form = TestimonialForm(request.POST)
        if form.is_valid():
            testimonial = form.save(commit=False)
            testimonial.client = client
            testimonial.save()
            return redirect('my_portfolio:testimonial_thank_you')
    else:
        form = TestimonialForm()
    context = {'form': form, 'client': client, 'testimonials': testimonials}
    return render(request, 'my_portfolio/submit_testimonial.html', context)

def testimonial_thank_you(request):
    return render(request, 'my_portfolio/testimonial_thank_you.html')