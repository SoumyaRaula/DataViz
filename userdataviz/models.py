"""
Author : Soumyaranjan
Email : soumya.raula@gmail.com
Created : 19 Sep 2015

"""
from django.db import models

# Create your models here.
class UserDataUpload(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField(max_length=400)
    upload_date = models.DateTimeField('date uploaded')
    filescount = models.IntegerField(default=0)
    #likes=models.IntegerField(default=0)
    
    def __unicode__(self):
        return self.title
    