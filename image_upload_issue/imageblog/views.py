from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
# Create your views here.
from imageblog.models import Post
def posts_create(request):
    return HttpResponse('<h1>CREATE</h1>')

def posts_detail(request):
    return HttpResponse('<h1>DETAIL</h1>')

def posts_home(request):
    queryset = Post.objects.all()
    if request.user.is_authenticated:
        context = {
            'queryset' : queryset,
            'title' : 'My user list'
            }
    else:
        context ={
            'title' : 'list'
            }
    return render(request, 'index.html', context)

def posts_update(request):
    return HttpResponse('<h1>Update</h1>')

def posts_delete(request):
    return HttpResponse('<h1>DELETE</h1>')

