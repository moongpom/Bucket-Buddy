
from django.urls import path
from .views import *
urlpatterns = [
   #게시글
   path('detailPage/<str:postId>',detail,name="detailPage"),
   path('newPost/<str:cate>',new,name="newPost"),
   path('editPost/<str:postId>',edit,name="editPost"),
   path('deletePost/<str:postId>',delete,name="deletePost"),

   #게시판 카테고리

   path('allPost/<str:cate>', allPost,name="allPost"),

   #검색
   path('search/', SearchFormView, name='search'),

   #댓글
   path('deleteComment/<str:postId>/<str:commentId>',deleteComment,name="deleteComment"),
   path('update_review/<str:post_id>/<str:comment_id>', update_review, name="update_review"),
   path('create_comment/<str:postId>',create_comment,name="create_comment"),
   path('create_re_comment/<str:postId>/<str:comment_id>',create_re_comment,name="create_re_comment"),
] 

