from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Post
from django.contrib.auth.models import User

# Create your views here.
@login_required
def create(request):
  if request.method == 'POST':
    if request.POST['title'] and request.POST['url']:
      # Create new Post object (from models)
      post = Post()
      post.title = request.POST['title']
      # Check for http(s)
      if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
        post.url = request.POST['url']
      else:
        post.url = 'http://' + request.POST['url']
      post.publish_date = timezone.now()
      post.author = request.user
      post.save()
      return redirect('home')
    else: # some error
      return render(request, 'posts/create.html', {'error':'ERROR: You must include a title and a URL to create a post.'})
  else: # GET
    return render(request, 'posts/create.html')

def home(request):
  posts = Post.objects.order_by('-votes_total')
  return render(request, 'posts/home.html', {'posts':posts})

def upvote(request, pk):
  if request.method == 'POST':
    post = Post.objects.get(pk=pk)
    # Increment votes
    post.votes_total += 1
    post.save()
    user_id = -1
    if 'uid' in request.POST.keys() and request.POST['uid']:
      user_id = request.POST['uid']
    if user_id != -1:
      return redirect('posts:userposts', uid=user_id)
    else:
      return redirect('home')

def downvote(request, pk):
  if request.method == 'POST':
    post = Post.objects.get(pk=pk)
    # Decrement votes
    post.votes_total += -1
    post.save()
    user_id = -1
    if 'uid' in request.POST.keys() and request.POST['uid']:
      user_id = request.POST['uid']
    if user_id != -1:
      return redirect('posts:userposts', uid=user_id)
    else:
      return redirect('home')

def userposts(request, uid):
  user = get_object_or_404(User, pk=uid)
  posts = Post.objects.filter(author_id=uid).order_by('-votes_total')
  return render(request, 'posts/userposts.html', {'user':user, 'posts':posts})
