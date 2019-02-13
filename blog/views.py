from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm

def input_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('db_binatang')
    else:
        form = PostForm()
    return render(request, 'blog/post_new.html', {'form': form})