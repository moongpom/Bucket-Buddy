from django.shortcuts import render, redirect, get_object_or_404
from .models import Bucket
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from django.core.paginator import Paginator

# bucketList
def view_bucket(request):
  return render(request, 'buckets/bucketlist.html')

def write(request):
  return render(request, 'buckets/write_bucket.html')

def create(request):
  new_bucket = Bucket()
  new_bucket.category = request.POST['category']
  new_bucket.pub_date = timezone.now()
  new_bucket.content = request.POST['content']
  new_bucket.writer = request.user
  new_bucket.save()
  return redirect('buckets:detail', request.POST['category'])

@login_required
def update(request, bucket_id):
  update_bucket = get_object_or_404(Bucket, pk=bucket_id)
  if update_bucket.writer == request.user:
    if request.method == "POST":
      update_bucket.category = request.POST['category']
      update_bucket.content = request.POST['content']
      update_bucket.save()
      return redirect('buckets:detail', request.POST['category'])
  return render(request, 'buckets/update_bucket.html', {'bucket': update_bucket})

def detail(request, category_str):
  bucket_list = Bucket.objects.filter(category = category_str).order_by('-pub_date')
  paginatorBucket = Paginator(bucket_list, 10)
  page = request.GET.get('page')
  buckets = paginatorBucket.get_page(page)
  context = { 'buckets': buckets, 'category': category_str }
  return render(request, 'buckets/detail_bucket.html', context)

@login_required
def delete(request, bucket_id):
  bucket = get_object_or_404(Bucket, id=bucket_id)
  bucket.delete()
  return redirect("buckets:detail", bucket.category)
