from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer
from django.shortcuts import render
from django.http import JsonResponse

class PostCreateView(APIView):
    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save() 
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
def post_list(request):
    posts = Post.objects.all()
    post_data = [
        {'content': post.content, 'created_at': post.created_at, 'updated_at': post.updated_at} for post in posts
    ]
    return JsonResponse(post_data, safe=False)

def index(request):
    return render(request, 'index.html')