from django.urls import path
from .views import *

app_name = "buckets"
urlpatterns = [
  path('bucketList/', view_bucket, name="view_bucket"), # 버킷리스트 카테고리 목록
  path('write/', write, name="write"), # 버킷리스트 작성
  path('create/', create, name="create"), # CREATE
  path('update/<int:bucket_id>', update, name="update"), # UPDATE
  path('delete/<int:bucket_id>', delete, name="delete"), # UPDATE
  
  path('bucketdetail/<str:category_str>', detail, name="detail"), # 버킷리스트 카테고리 클릭시 상세
]