from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _

# Create your models here.
class OperationCenter(models.Model):
    name = models.CharField(_('name'), max_length=64)
    profit = models.FloatField(_('profit'), default=0.0)
    
    def total_users(self):
        return self.profile_set.count()
    total_users.short_description = _('total users')

    def __unicode__(self):
        return '%s' % (self.name)