from django.shortcuts import render
from .models import Profile

# Create your views here.
def mypage(request):
  user = request.user
  profile = Profile.objects.filter(user=user)
  context = { 'user': user, 'profile': profile }
  return render(request, 'user/mypage.html', context)