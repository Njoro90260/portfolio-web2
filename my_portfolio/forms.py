from django import forms
from .models import Client, Testimonial

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields =['name', 'logo', 'website']
        labels = {'testimonial': ''}


class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['testimonial_text']
        