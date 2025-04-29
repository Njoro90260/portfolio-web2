from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import *
from .forms import *
from django.core.mail import send_mail
from decouple import config
from django.views.generic import DetailView, UpdateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from itertools import zip_longest

# Create your views here.
def make_groups(iterable, group_size):
    """Helper function to group items into chunks."""
    args = [iter(iterable)] * group_size
    return zip_longest(*args, fillvalue=None)

def index(request):
    """View function for the page."""
    projects = Project.objects.all()[:3]
    services = Service.objects.all()
    clients = Client.objects.all()
    for client in clients:
        if not client.logo:
            client.logo = 'logos/default-logo.webp' # Fallback to default.
    client_groups = list(make_groups(clients, 4))
    client_instance = Client.objects.first()
    testimonials = Testimonial.objects.select_related('client').all()

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
        'client_groups': client_groups,
        'token': client_instance.unique_token if client_instance else None,
        'testimonials': testimonials,
        'contact_form': contact_form,
        'newsletter_form': newsletter_form,
        'user': request.user
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
    context = {
        'form': form, 
        'client': client, 
        'testimonials': testimonials
    }
    return render(request, 'my_portfolio/submit_testimonial.html', context)

def testimonial_thank_you(request):
    return render(request, 'my_portfolio/testimonial_thank_you.html')

class UserProfileDetailView(DetailView):
    model = UserProfile
    template_name = 'my_portfolio/user_profile.html'

    context_object_name = 'profile'

    def get_object(self, queryset=None):
        # Get profile based on the username from the URL
        username = self.kwargs.get('username')
        return get_object_or_404(UserProfile, user__username=username)
    

class UserProfileUpdateView(UpdateView):
    model = UserProfile
    template_name = 'my_portfolio/edit_profile.html'
    form_class = UserProfileForm

    def get_object(self, queryset=None):
        # # Restrict edditing to the profile owner
        # profile = get_object_or_404(UserProfile, user=self.request.user)
        # return profile
        username = self.kwargs.get('usernamre')
        user = get_object_or_404(User, username=username)
        # Ensure a UserProfile instance exists for the user
        profile, created = UserProfile.objects.get_or_create(user=self.request.user)
        return profile
    

    def get_success_url(self):
        return reverse_lazy('my_portfolio:profile', kwargs={'username': self.request.user.username})