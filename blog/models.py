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

    # this makes it so we see the blog title (vs Blog Object) on the admin page
    def __str__(self):
        return self.title

    # add summary functionality
    def summary(self):
        # give me back the first 100 characters
        return self.body[:100]

    # add time formatting functionality, see strftime.org
    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')