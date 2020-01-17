from django.shortcuts import render

def allblogs(request):

    """
     Django automatically checks templates, having another sub blog folder is best syntax but must include if it is not
     just sitting under templates in current application.

     Best syntax to have subfolder (e.g. blog, jobs) because multiple pages will have home pages, better for syntax/
     avoiding confusion

    """
    return render(request, 'blog/allblogs.html')

