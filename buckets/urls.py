from django.urls import path
from .views import *

app_name = "buckets"
urlpatterns = [
  path('bucketList/', view_bucket, name="view_bucket"), # 버킷리스트 카테고리 목록
  path('write/', write, name="write"), 
]