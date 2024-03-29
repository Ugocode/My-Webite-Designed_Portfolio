from django.shortcuts import render, get_object_or_404
from .models import Blog
# Create your views here.


#this lists out all the blogs in the blog page 
def allblogs(request):
    blogs = Blog.objects
    return render(request, 'blog/allblogs.html', { 'blogs':blogs})


#This function brings out the deaitls of the writeup in the blog section
def detail(request, blog_id):
    detailblog = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'blog/detail.html', {'blog': detailblog })
