from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

ORDER_TYPES = (
    ('B', 'BUY'),
    ('S', 'SELL'),
    ('SS', 'SELL_SHORT')
)
# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(User, unique=True)
    time_stamp = models.CharField(max_length=32)
    order_type = models.CharField(max_length=2, choices=ORDER_TYPES, default='B')
    quantity = models.IntegerField()
    price = models.FloatField()
