from django.shortcuts import render, redirect
from .forms import PostForm

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('post_detail', pk=post.pk) # Redirects to post detail
    else:
        form = PostForm() 
    return render(request, 'create_post.html', {'form': form})