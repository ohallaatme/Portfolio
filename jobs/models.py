from django.db import models

"""
Our subclass of models.Model provides us with 
abilities to connect and save into database

model makes it easy for us to use db of our choice but still have same code
"""

class Job(models.Model):

    """ properties of class are what we want to make a job """

    # image property
    # upload_to is where we want to send information
    # all images from one job go to a central directory
    image = models.ImageField(upload_to='images/')
    # Summary is description that tells us what is going on for the job
    # max length not required but recommended for CharField
    summary = models.CharField(max_length=200)
