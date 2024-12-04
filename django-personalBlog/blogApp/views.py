from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import PostForm

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/posts/')  # Redirige a una lista de posts
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})