from django.shortcuts import render, redirect
from django.http import Http404
from django.urls import reverse


# Create your views here.
def index(request):
    """View function for the page."""
    return render(request, 'my_portfolio/index.html')
