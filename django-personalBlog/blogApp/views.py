from django.shortcuts import render
from .models import Section

# Create your views here.

def section(request):
    return render(request, "blogApp/section.html");