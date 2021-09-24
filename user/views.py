from django.shortcuts import render, get_object_or_404
from .models import Profile
from django.contrib.auth.models import User

# Create your views here.
def mypage(request, id):
  user = get_object_or_404(User, pk=id)
  context = {
    'user': user,
    'profile': Profile.objects.filter(user=user)
  }
  return render(request, 'user/mypage.html', context )