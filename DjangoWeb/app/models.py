"""
Definition of models.
"""
#-*- coding: utf-8 -*-
from django.db import models
from django.contrib import admin
# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length = 150)#标题
    body = models.TextField()#正文
    timestamp = models.DateTimeField()#时间
    def __unicode__(self):
        return self.title
    class Meta():
        ordering = ['-timestamp']
admin.site.register(BlogPost)
