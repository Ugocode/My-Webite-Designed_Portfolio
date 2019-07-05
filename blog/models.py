from django.db import models

# Create your models here.
#this creates the models for the blog app in the portfolio-project

class Blog(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to= 'media/')
    pub_date = models.DateTimeField()
    body = models.TextField()

    #To make us get the real title of each blog in the admin interface:
    def __str__(self):
        return self.title

    # To give us a little summary of each blog on the blog page:
    def summary(self):
        return self.body [:100]

    #To help print the date only on the blog page:
    #def pub_date_pretty(self):
    #    return self.pub_date.strftime('%b %e %Y')
