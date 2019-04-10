from django.db import models

# Create your models here.

class Job(models.Model):

    image = models.ImageField(upload_to= 'media/')
    summary = models.CharField(max_length = 200)


    #this brings out the title of each jobs on the admin page
    def __str__(self):
        return self.summary [ :20]
