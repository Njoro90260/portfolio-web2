# Generated by Django 5.1.2 on 2024-11-16 16:13

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_portfolio', '0006_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='testimonial',
        ),
        migrations.RemoveField(
            model_name='project',
            name='client',
        ),
        migrations.AddField(
            model_name='client',
            name='unique_token',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testimonial_text', models.TextField()),
                ('submitted_on', models.DateTimeField(auto_now_add=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_portfolio.client')),
            ],
        ),
    ]
