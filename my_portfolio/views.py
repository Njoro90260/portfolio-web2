from django.shortcuts import render, redirect, get_object_or_404
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

    # initialize to avoid UnboundLocalError
    contact_form = ContactMessageForm()
    newsletter_form = NewsletterSubscriptionForm()

    if request.method == 'POST':
        # Handle contact form
        if 'contact_submit' in request.POST:
            contact_form = ContactMessageForm(request.POST)
            if contact_form.is_valid():
                message = contact_form.save()
                # Send email notification
                send_mail(
                    subject=f"New Contact Message from {message.name}",
                    message=f"You've received a new message:\n\n"
                            f"Name: {message.name}\n"
                            f"Email: {message.email}\n"
                            f"Subject: {message.subject}\n\n"
                            f"{message.message}",
                    from_email=config('EMAIL_HOST_USER'),
                    recipient_list=config('RECIPIENT_LIST').split(','),
                )
                messages.success(request, "Your message has been sent successfully!")
                form_submitted = True
            else:
                messages.error(request, "Whoops! There was an error sending your message. Please try again.")

        # Handle newsletter subscription
        elif 'newsletter_submit' in request.POST:
            newsletter_form = NewsletterSubscriptionForm(request.POST)
            if newsletter_form.is_valid():
                email = newsletter_form.cleaned_data['email']
                subscription, created = NewsletterSubscription.objects.get_or_create(email=email)
                if created:
                    messages.success(request, "Thank you for subscribing!")
                    # newsletter_subscribed = True
                else:
                    messages.info(request, "You're already subscribed.")
            else:
                messages.error(request, "Invalid email. Please try again.")

    context = {
        'projects': projects,
        'services': services,
        'clients': clients,
        'token': client_instance.unique_token if client_instance else None,
        'testimonials': testimonials,
        'contact_form': contact_form,
        'newsletter_form': newsletter_form,
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