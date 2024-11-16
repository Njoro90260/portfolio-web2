from django.contrib import admin
from django.apps import apps
from .models import Client


# Register your models here.
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'website', 'unique_token')

app = apps.get_app_config('my_portfolio')

for model in app.get_models():
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass