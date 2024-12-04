from django import forms
from .models import Section, Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['date', 'content', 'section']