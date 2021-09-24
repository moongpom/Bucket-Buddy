from django import forms
from django.contrib.auth.models import User
from django.forms.fields import FileField, ImageField
from user.models import Profile

class SignupForm(forms.Form):
  class Meta:
    model = User
  
  address = forms.CharField()
  photo = ImageField(required=False)
  
  def signup(self, request, user):
    userProfile = Profile()
    userProfile.user = user
    userProfile.address = self.cleaned_data['address']
    userProfile.photo = self.cleaned_data['photo']
    userProfile.save()
    user.save()
    return user