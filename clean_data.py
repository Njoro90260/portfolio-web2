import os
import django

# Setup django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_portfolio.settings')
django.setup()

from my_portfolio.models import Testimonial
from django.db import models
import unicodedata

def clean_data(model):
    """Clean data in a model."""
    for obj in model.objects.all():
        for field in obj._meta.fields:
            if isinstance(field, models.CharField) or isinstance(field, models.TextField):
                value = getattr(obj, field.name)
                if value:
                    cleaned_value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('utf-8', 'ignore')
                    setattr(obj, field.name, cleaned_value)

        obj.save()

if __name__ == '__main__':
    # call clean_data for each relevant model
    clean_data(Testimonial)