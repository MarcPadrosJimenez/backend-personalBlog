from datetime import datetime
from django.db import models

class Section(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    description = models.CharField(max_length=255, null=True, blank=True)

class Post(models.Model):
    content = models.TextField(max_length=255, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True) # auto_now_add=True means the field will be automatically set to the current time when the object is first created
    updated_at = models.DateTimeField(auto_now=True) # auto_now=True means the field will be updated to the current time whenever the object is saved
    section = models.ForeignKey(Section, on_delete=models.CASCADE)