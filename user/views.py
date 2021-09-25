from django.shortcuts import render, get_object_or_404
from .models import Profile
from buckets.models import Bucket
from board.models import Post, Comment
from django.contrib.auth.models import User

# Create your views here.
def mypage(request, id):
  user = get_object_or_404(User, pk=id)
  context = {
    'user': user,
    'profile': Profile.objects.filter(user = user),
    'buckets': Bucket.objects.filter(writer = user),
    'posts': Post.objects.filter(writer = user),
    'comments': Comment.objects.filter(writer = user),
  }
  return render(request, 'user/mypage.html', context)



