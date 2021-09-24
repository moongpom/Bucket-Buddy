from django.db import models
from django.contrib.auth.models import User

class Bucket(models.Model):
  id = models.AutoField(primary_key=True)
  Category_choice = (
    ("travel", "여행"),
    ("develop", "자기 개발"),
    ("leisure", "여가"),
    ("healthy", "건강"),
    ("love", "사랑"),
    ("society", "사회"),
    ("dream", "꿈"),
    ("family", "가족"),
    ("more", "기타"),
  )
  category = models.CharField(choices=Category_choice, max_length=100)
  content = models.TextField()
  pub_date = models.DateTimeField()
  writer = models.ForeignKey(User,on_delete=models.CASCADE)