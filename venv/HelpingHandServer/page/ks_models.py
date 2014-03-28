
from django.contrib.auth.models import User
from django.db import models

class Item(models.Model):
    owner = models.CharField(max_length=32)
    menu = models.CharField(max_length=32,null=True,blank=True)
    page = models.CharField(max_length=32,null=True,blank=True)
    title = models.CharField(max_length=32)

    def __unicode__(self):
        return '%s' % (self.title)

class Page(models.Model):
    title = models.CharField(max_length=32)
    content = models.TextField()

    def __unicode__(self):
        return '%s' % (self.title)

