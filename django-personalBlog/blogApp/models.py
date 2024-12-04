from mongoengine import Document, StringField, DateTimeField, ReferenceField, CASCADE
from datetime import datetime

class Section(Document):
    name = StringField(required=True)
    description = StringField()

class Post(Document):
    content = StringField(required=True)
    created_at = DateTimeField(default=datetime.now)
    updated_at = DateTimeField(default=datetime.now)
    section = ReferenceField(Section, reverse_delete_rule=CASCADE)