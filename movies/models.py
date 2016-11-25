from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    running_time = models.CharField(max_length=20)
    director = models.CharField(max_length=255)


    def __unicode__(self):
        return self.title


    def publish(self):
        self.published_date = timezone.now()
        self.save()









