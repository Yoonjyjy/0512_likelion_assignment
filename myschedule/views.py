from django.shortcuts import render, get_object_or_404, redirect
from .models import Schedule
from django.utils import timezone
from .forms import PostForm

# Create your views here.
def home(request) :
    posts = Schedule.objects
    return render(request, 'myschedule/home.html', {'posts':posts})

def detail(request, post_id) :
    post_detail = get_object_or_404(Schedule, pk = post_id)
    return render(request, 'myschedule/detail.html', {'post':post_detail})

def post_new(request) :
    if request.method =="POST":
        form = PostForm(request.POST)
        if form.is_valid() :
            post = form.save(commit=False)
            post.published_date = timezone.datetime.now()
            post.save()
            return redirect('detail', post_id=post.pk)
    else :
        form = PostForm()
    return render(request, 'myschedule/post_new.html', {'form':form})

def post_edit(request, post_id) :
    post = get_object_or_404(Schedule, pk = post_id)
    if request.method == "POST" :
        form = PostForm(request.POST, instance=post)
        if form.is_valid() :
            post = form.save(commit=False)
            post.published_date = timezone.datetime.now()
            post.save()
            return redirect('detail', post_id=post.pk)
    else :
        form = PostForm(instance=post)
    return render(request, 'myschedule/post_edit.html', {'form':form})

def post_delete(request, post_id) :
    post = get_object_or_404(Schedule, pk = post_id)
    post.delete()
    return redirect('home')