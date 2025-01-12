from rest_framework.response import Response
from .models import Post, Section
from .serializers import PostSerializer, SectionSerializer
from django.shortcuts import render
from rest_framework.decorators import api_view

@api_view(['POST'])
def create_section(request):
    serializer = SectionSerializer(data=request.data)
    if serializer.is_valid():
        section_name = serializer.validated_data.get('name')
        section, created = Section.objects.get_or_create(name=section_name, defaults={'description': serializer.validated_data.get('description', '')})
        if created:
            return Response(serializer.data, status=201)
        else:
            return Response({"message": "Section already exists"}, status=200)
    return Response(serializer.errors, status=400)

@api_view(['POST'])
def create_post(request):
    section_name = request.data.get('section')
    if not section_name:
        return Response({"error": "Section name not provided"}, status=400)
    
    try:
        section = Section.objects.get(name=section_name)
    except Section.DoesNotExist:
        return Response({"error": "Section not found"}, status=404)
    
    data = request.data.copy()
    data['section'] = section.id  # Assigns the ID of the section to the post as its foreign key
    
    serializer = PostSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def get_section_posts(request, section_name):
    try:
        section = Section.objects.get(name=section_name)
        posts = Post.objects.filter(section=section)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    except Section.DoesNotExist:
        return Response({"error": "Section not found"}, status=404)

def index(request):
    return render(request, 'index.html')