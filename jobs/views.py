from django.shortcuts import render
# recall .models means the models file in the current directory
from .models import Job


def home(request):
    # will automatically look for templates folder, so important top folder is named that!
    # best practice to sub-directory with a template folder that references the name with jobs so
    # it doesn't get confused
    """
    To have our jobs show up post Bootstrapping, we want to return them
    with the render. Recall we can return dictionary of values.

    MUST be a dictionary
    """

    jobs = Job.objects # this goes and gets all of the jobs
    return render(request, 'jobs/home.html', {'jobs': jobs})