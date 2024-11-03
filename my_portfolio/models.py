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
        return self.username
    
class Project(models.Model):
    """Project model to store information about each project."""
    title  = models.CharField(max_length=200)
    description = models.TextField()
    technologies = models.CharField(max_length=300) # list technologies as a comma sepatared string
    live_link = models.URLField(blank=True, null=True)
    repo_link = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    # client = models.ForeignKey('Client', on_delete=models.SET_NULL, null=True, blank=True, related_name='projects')
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title