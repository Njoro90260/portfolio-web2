from django import forms
from .models import Client, Testimonial, ContactMessage, NewsletterSubscription, UserProfile

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields =['name', 'logo', 'website']
        labels = {'testimonial': ''}


class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['testimonial_text']
        widgets = {
            'testimonial_text': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'submit your testimonial',
                'rows': 4,
            }),
        }

class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = [
            'name',
            'email',
            'subject',
            'message',
        ]
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your name',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email',
            }),
            'subject': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email',
            }),
            'subject': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter the subject',
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your message',
                'rows': 4,
            }),
        }
    
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

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'profile_picture', 'social_links']
        