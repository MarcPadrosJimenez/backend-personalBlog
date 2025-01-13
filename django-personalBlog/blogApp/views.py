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
            return Response(serializer.data, status=201) # 201 code means the request was successful and a new resource was created
        else:
            return Response({"message": "Section " + section_name + " already exists"}, status=200)
    return Response(serializer.errors, status=400)

@api_view(['POST'])
def create_post(request, section_name):
    try:
        section = Section.objects.get(name=section_name)
    except Section.DoesNotExist:
        return Response({"error": "Section " + section_name + " not found"}, status=404)
    
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
        posts = Post.objects.filter(section=section).order_by('-updated_at')  # Orders the posts by the updated_at field, the most recents first
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    except Section.DoesNotExist:
        return Response({"error": "Section " + section_name + " not found"}, status=404)

@api_view(['DELETE'])
def delete_post(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
        post.delete()
        return Response(status=204) # 204 code means the request was successful and the server has no content to return
    except Post.DoesNotExist:
        return Response({"error": "Post not found"}, status=404) # 404 code means the resource was not found

@api_view(['PUT'])
def update_post(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
        data = request.data.copy()
        data['section'] = post.section.id  # Makes sure the section field exists
        serializer = PostSerializer(post, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200) # 200 code means the request was successful and returns the updated post
        return Response(serializer.errors, status=400) # 400 code means the request was malformed 
    except Post.DoesNotExist:
        return Response({"error": "Post not found"}, status=404)

def index(request):
    return render(request, 'index.html')