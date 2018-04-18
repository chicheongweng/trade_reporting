from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

ORDER_TYPES = (
    ('B', 'BUY'),
    ('S', 'SELL'),
#   ('SS', 'SELL_SHORT')
)
# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(User)
    time_stamp = models.DateTimeField("Time Stamp")
    order_type = models.CharField(_('order type'), max_length=2, choices=ORDER_TYPES, default='B')
    quantity = models.IntegerField(_('quantity'))
    price = models.FloatField(_('price'))
    symbol = models.CharField(_('symbol'), max_length=32, default="GLD")

    class Meta:
        verbose_name = _('order')
        verbose_name_plural = _('orders')