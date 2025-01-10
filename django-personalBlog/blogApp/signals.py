from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Section

@receiver(post_migrate)
def create_default_sections(sender, **kwargs):
    if sender.name == 'blogApp':
        Section.objects.get_or_create(name='Test', description='This is a default section')
