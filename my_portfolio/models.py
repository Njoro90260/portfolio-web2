from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# User profile model to store additional information about the website owner (me)
class UserProfile(models.Model):
    """The UserProfile model stores user information."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    social_links = models.JSONField(default=dict, blank=True)

    def __str__(self):
        return self.user

class Client(models.Model):
    """Client model to store information about clients worked with."""
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='clients/', blank=True, null=True)
    website = models.URLField(blank=True)
    testimonial = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    """Project model to store information about each project."""
    title  = models.CharField(max_length=200)
    description = models.TextField()
    technologies = models.CharField(max_length=300) # list technologies as a comma sepatared string
    live_link = models.URLField(blank=True, null=True)
    repo_link = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    client = models.ForeignKey('Client', on_delete=models.SET_NULL, null=True, blank=True, related_name='projects')
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class Service(models.Model):
    """Service model to store details about services offered."""
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class NewsletterSubscription(models.Model):
    """NewsletterSubscription model to manage subscribers."""
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.email


class ContactMessage(models.Model):
    """ContactMessage model to store messages from the contact form"""
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    status = models.CharField(max_length=20, choices=[('unread', 'Unread'), ('read', 'Read'), ('replied', 'Replied')], default='unread')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name