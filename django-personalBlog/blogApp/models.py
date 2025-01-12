from datetime import datetime
from django.db import models

class Section(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    description = models.CharField(max_length=255, null=True, blank=True)

class Post(models.Model):
    content = models.TextField(max_length=255, null=False, blank=False)
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)