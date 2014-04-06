
from django.contrib.auth.models import User
from django.db import models

class Item(models.Model):
    targetType = models.CharField(max_length=32)
    title = models.CharField(max_length=32)
    target = models.CharField(max_length=32,blank=True,null=True)
    menu = models.CharField(max_length=32)

    def __unicode__(self):
        return '%s' % (self.title)

class Page(models.Model):
    content = models.TextField()
    title = models.CharField(max_length=32)

    def __unicode__(self):
        return '%s' % (self.title)

