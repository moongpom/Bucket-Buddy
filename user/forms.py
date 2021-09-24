from django import forms
from django.contrib.auth.models import User
from user.models import Profile

class SignupForm(forms.Form):
  class Meta:
    model = User
  
  address = forms.CharField()
  
  def signup(self, request, user):
    userProfile = Profile()
    userProfile.user = user
    userProfile.address = self.cleaned_data['address']
    userProfile.save()
    user.save()
    return user