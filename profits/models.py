from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _

# Create your models here.
class Profit(models.Model):
    net = models.FloatField(_('net'))
    user = models.ForeignKey(User, verbose_name = _('user'))
    symbol = models.CharField(_('symbol'), max_length=16)
