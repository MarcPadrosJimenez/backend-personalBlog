# from mongoengine import Document, StringField, DateTimeField, ReferenceField, CASCADE
from datetime import datetime
from django.db import models

class Section(models.Model):
    name = models.CharField(null=False, blank=False)
    description = models.CharField()

class Post(models.Model):
    content = models.CharField(null=False, blank=False)
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)