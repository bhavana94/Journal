from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Publication(models.Model):
	
    title = models.CharField(max_length=30)

    def __unicode__(self):           
        return '%s :'%(self.title)

class Article(models.Model):

    headline = models.CharField(max_length=100)
    publications = models.ManyToManyField(Publication)

    def __unicode__(self):             
        return '%s :'%(self.headline)