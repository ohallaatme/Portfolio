# get_object_or_404 either gets object back from the database or spits out
# a 404 error if there is no match
from django.shortcuts import render, get_object_or_404
from .models import Blog


def allblogs(request):

    """
     Django automatically checks templates, having another sub blog folder is best syntax but must include if it is not
     just sitting under templates in current application.

     Best syntax to have subfolder (e.g. blog, jobs) because multiple pages will have home pages, better for syntax/
     avoiding confusion

    """
    blogs = Blog.objects
    return render(request, 'blog/allblogs.html', {'blogs': blogs})

# setting up view for blog detail, need to pass in the blog_id outlined
# in urls.py in the path
def detail(request, blog_id):
    # pass in the name of the object and what the primary key (pk) id is
    detail_blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog':detail_blog})

