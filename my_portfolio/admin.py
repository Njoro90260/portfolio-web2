from django.contrib import admin
from django.apps import apps
from .models import Client
from django.urls import reverse
from django.core.mail import send_mail
from django.utils.html import format_html

def send_testimonial_email(modeladmin, request, queryset):
    for client in queryset:
        """Generate the personalised testimonial link."""
        link = reverse('my_portfolio:submit_testimonial', args=[client.unique_token])
        full_link = f"http://localhost:8000{link}" # To be replaced with my domain
        message = (
            f"Hello {client.name},\n\n"
            f"Please submit your testimonial using the following link:\n{full_link}"
            "Thank you for your feedback!"
        )
        # send the email to the client
        if client.email:
            send_mail(
                'Submit Your Testimonial',
                message,
                'peternjoroge738@yahoo.com',
                [client.email],
            )
    modeladmin.message_user(request, "Testimonial links sent successfully!")

# Register your models here.
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'testimonial_link')
    actions = [send_testimonial_email]

    def testimonial_link(self, obj):
        """Display a clickable link in the admin interface."""
        url = reverse('my_portfolio:submit_testimonial', args=[obj.unique_token])
        return format_html('<a href="{}" target="_blank">Submit Testimonial</a>', f"http://localhost:8000{url}")

    testimonial_link.short_description = 'Testimonial Link'   

app = apps.get_app_config('my_portfolio')

for model in app.get_models():
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass