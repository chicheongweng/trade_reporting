from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class OperationCenter(models.Model):
    name = models.CharField(max_length=64)
    profit = models.FloatField(default=0.0)

    def __unicode__(self):
        return '%s' % (self.name)