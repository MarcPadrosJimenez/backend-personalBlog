# from mongoengine import Document, StringField, DateTimeField, ReferenceField, CASCADE
from datetime import datetime
from django.db import models

class Section(models.Model):
    name = models.StringField(required=True)
    description = models.StringField()

class Post(models.Model):
    content = models.StringField(required=True)
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)
    section = models.ReferenceField(Section, reverse_delete_rule=models.CASCADE)