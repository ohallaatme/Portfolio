from django.shortcuts import render

def home(request):
    # will automatically look for templates folder, so important top folder is named that!
    # best practice to sub-directory with a template folder that references the name with jobs so
    # it doesn't get confused
    return render(request, 'jobs/home.html')