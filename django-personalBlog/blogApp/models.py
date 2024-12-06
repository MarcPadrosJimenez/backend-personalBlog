# from mongoengine import Document, StringField, DateTimeField, ReferenceField, CASCADE
from datetime import datetime
from django.db import models

class Section(models.Model):
    name = models.CharField(required=True)
    description = models.CharField()

class Post(models.Model):
    content = models.CharField(required=True)
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)