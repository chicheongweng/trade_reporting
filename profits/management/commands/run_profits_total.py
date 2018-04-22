#https://medium.com/@gis10kwo/how-to-create-fake-jobseeker-profiles-using-django-2-0-and-faker-dcfb09bda378

from django.db import models
from django.core.management.base import BaseCommand
from faker import Faker
import random
import uuid
from django.contrib.auth.models import User
from datetime import datetime,timedelta
from random import randint
from django.contrib.auth.hashers import make_password
from user_profile.models import Profile
from orders.models import Order
from django.utils import timezone
from profits.models import Profit
from orders.models import Order
from django.conf import settings

SYMBOLS = settings.SYMBOLS
RATIO_OF_USERS_PLACEING_ORDERS = 0.5
TOTAL_USERS_PLACING_ORDERS = int(User.objects.count()*RATIO_OF_USERS_PLACEING_ORDERS)
TOTAL_ORDERS_PER_USER = 20
ORDER_QUANTITY_STD = 10

class Command(BaseCommand):

    help = 'calculate profits for all users'

    def handle(self, *args, **options):
        #self.stdout.write("TOTAL_USERS %i" % TOTAL_USERS)
        all_users = User.objects.all()
        for user in all_users:
            profits = Profit.objects.filter(user=user).exclude(symbol='TOTAL')
            print "profits ",profits
            if profits:
                net = 0.0
                for profit in profits:
                    net = net + profit.net
                try:
                    p = Profit.objects.get(user=user, symbol='TOTAL')
                    p.net = round(net, 2)
                except:
                    p = Profit.objects.create(net=net, user=user, symbol='TOTAL')
                p.save()

