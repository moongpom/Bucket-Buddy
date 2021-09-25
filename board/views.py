from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.utils import timezone
from .forms import  *
from django.views.generic.edit import FormView
from django.db.models import Q

from django.core.paginator import Paginator
# Create your views here.



#상세창
def detail(request,postId):
    post = get_object_or_404(Post,pk=postId)
    comments = Comment.objects.filter(postId=postId,comment_id__isnull=True)
    re_comments=[]
    for comment in comments:
        re_comments += list(Comment.objects.filter(comment_id=comment.id))
    commentForm = CommentForm()
    return  render(request,'detail.html',{'posts':post,'comments':comments,'re_comments':re_comments,'commentForms':commentForm})
#게시판 카테고리 
def allPost(request,cate):
    if cate=="all":
        post=Post.objects.all().order_by('-id')
    else :
        post=Post.objects.filter( category = cate).order_by('-id')
    paginatorPost = Paginator(post, 10)
    page = request.GET.get('page')
    posts = paginatorPost.get_page(page)
    return render(request,"allPost.html",{'posts':posts,'cate':cate})

#새로운 글 작성 않이 이거 cate원하는대로 ㅇ안됨
def new(request,cate):
    if request.method == 'POST': #글 작성 후 저장버튼 눌렀을 때
        post_form = PostForm(request.POST,request.FILES)
        if post_form.is_valid():
            post = post_form.save(commit = False)
            post.writer = request.user
            post.pub_date = timezone.now() 
            post.save()
            return redirect("detailPage",post.id)
    else:
        post_form = PostForm()
        #if cate == post_form.category:
        post_form.category = cate
        print(post_form.category)
        context = {}
        context['postsform'] = post_form
        return render(request,'new.html',context)


#수정
def edit(request,postId):
    post = get_object_or_404(Post,pk=postId)
    if request.method == 'GET': #수정
        post_form=PostForm(instance=post)
        context = {}
        context['edit_post'] = post_form
        return render(request,'edit.html',context)
    else:
        post_form = PostForm(request.POST,request.FILES,instance = post)
        if post_form.is_valid():
            post = post_form.save(commit = False)
            post.pub_date = timezone.now() # 날짜 생성
            post.save()
        return redirect("detailPage",post.id)

#게시글 삭제
def delete(request,postId):
    deletePost = get_object_or_404(Post,pk=postId)
    deletePost.delete() #삭제해주는 메소드
    if deletePost.category=="free":
        return redirect('free')
    elif deletePost.category=="suggest":
        return redirect('suggest') 
    elif deletePost.category=="review":
        return redirect('review')  
    else:
        return redirect('allpost')


#댓글작성
def create_comment(request, postId):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            #이부분왜 id할당이 아니라 제목이 할당되지
            comment.postId = Post.objects.get(pk = postId)
            #
            comment.post_id = postId
            #
            comment.writer = request.user
            comment.pub_date = timezone.now()
            comment.save()
    return redirect('/board/detailPage/'+str(postId))
#대댓글작성
def create_re_comment(request, postId, comment_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.postId = Post.objects.get(pk = postId)
            comment.post_id = postId
            comment.writer = request.user
            comment.comment_id = Comment.objects.get(pk = comment_id)
            comment.pub_date = timezone.now()
            comment.save()
    return redirect('/board/detailPage/'+str(postId))

# 댓글 수정
def update_review(request, post_id, comment_id):
    com=Comment.objects.get(id= comment_id)
    com_form=CommentForm(instance=com)
    if request.method == "POST":
        update_form= CommentForm(request.POST, instance = com)
        if update_form.is_valid():
            update_form.save()
            return redirect('/board/detailPage/'+ str(post_id))
    return render(request, 'review_update.html',{'com_form':com_form})

#댓글삭제
def deleteComment(request,postId,commentId):
    deleteComment = get_object_or_404(Comment,pk=commentId)
    deleteComment.delete() #삭제해주는 메소드
    return redirect("detailPage",postId)
'''
#검색
class SearchFormView(FormView):
    form_class = PostSearchForm
    template_name = 'search.html'

    def form_valid(self, form):
        searchWord = form.cleaned_data['search_word']
        post_list = Post.objects.filter(Q(title__icontains=searchWord) | Q(body__icontains=searchWord) ).distinct().order_by('-id')

        context = {}
        context['form'] = form
        context['search_term'] = searchWord
        context['object_list'] = post_list

        return render(self.request, self.template_name, context)'''

def SearchFormView(request):
    list = Post.objects.all()
    search_key = request.GET.get('search_key') # 검색어 가져오기
    if search_key: # 만약 검색어가 존재하면
        list = list.filter(Q(title__icontains=search_key) | Q(body__icontains=search_key) ).distinct().order_by('-id')# 해당 검색어를 포함한 queryset 가져오기
    return render(request, 'search.html', {'list':list})
