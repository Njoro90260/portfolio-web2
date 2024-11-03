from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# User profile model to store additional information about the website owner (me)
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    social_links = models.JSONField(default=dict, blank=True)

    def __str__(self):
        return self.username
    
