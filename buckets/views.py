from django.shortcuts import render

# bucketList
def view_bucket(request):
  return render(request, 'buckets/bucketlist.html')

def write(request):
  return render(request, 'buckets/write_bucket.html')