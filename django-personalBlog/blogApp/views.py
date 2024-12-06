from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer
from django.shortcuts import render
from rest_framework.decorators import api_view

@api_view(['POST'])
def create_post(request):
    if request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
@api_view(['GET'])
def post_list(request):
    posts = Post.objects.all() # fetches all posts from the database
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data) # returns the serialized data as a JSON response

def index(request):
    return render(request, 'index.html')