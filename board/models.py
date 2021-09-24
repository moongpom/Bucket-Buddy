from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200) #CharField: 제한있는 문자열
    Category_Choice = (
        ("free","자유게시판"),
        ("review","후기"),
        ("suggest","건의하기"),
    )
    category = models.CharField(choices=Category_Choice, max_length=100)
    writer=models.ForeignKey(User,on_delete=models.CASCADE)
    pub_date=models.DateTimeField()
    body=models.TextField()
    image = models.ImageField(upload_to="mediaForm/",blank=True,null=True)

    #아래 함수는 밑에서 설명
    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:80] 

class Comment(models.Model):
    postId = models.ForeignKey("Post",on_delete=models.CASCADE,db_column="postId")
    post_id = models.CharField(max_length=50)
    comment_id = models.ForeignKey("self",on_delete=models.CASCADE,blank=True,null=True)
    writer=models.ForeignKey(User,on_delete=models.CASCADE)
    body = models.TextField('댓글')
    pub_date=models.DateTimeField()

    def summary(self):
        return self.body[:10] 
