from django.db import models


class Blog(models.Model):

    # title with max length of 200
    title = models.CharField(max_length=200)

    # publication date - use DateTimeField()
    pub_date = models.DateTimeField()

    # image for blog post, should be same as Job model
    image = models.ImageField(upload_to='images/')

    # text body - using TextField instead of CharField as this should be a larger body of text
    body = models.TextField()