from __future__ import unicode_literals

from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=50)
    intro = models.TextField()
    body = models.TextField()
    date = models.DateTimeField()

    def __unicode__(self):
        return self.title
