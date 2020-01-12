from django.contrib import admin

# Register your models here.
# dot recognizes we are in the current directory, models is the file with the job model
# Job is the name of our model
from .models import Job

# this line of code makes the Job model available to the super user in the admin interface
admin.site.register(Job)