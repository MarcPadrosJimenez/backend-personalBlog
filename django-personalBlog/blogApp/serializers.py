# serializers.py
from rest_framework import serializers
from .models import Section, Post

class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        extra_kwargs = { # This is used to specify that the section field is not required to be present in the request
            'section': {'required': False}
        }