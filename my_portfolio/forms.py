from django import forms
from .models import Client, Testimonial, ContactMessage, NewsletterSubscription

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields =['name', 'logo', 'website']
        labels = {'testimonial': ''}


class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['testimonial_text']

class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = [
            'name',
            'email',
            'subject',
            'message',
        ]
        
class NewsletterSubscriptionForm(forms.ModelForm):
    class Meta:
        model= NewsletterSubscription
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email',
                'required': True,
            }),
        }
        labels = {
            'email': '',
        }