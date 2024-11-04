from django.contrib import admin
from django.apps import apps


# Register your models here.

app = apps.get_app_config('my_portfolio')

for model in app.get_models():
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass
