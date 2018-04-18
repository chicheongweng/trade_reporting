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
from operation_centers.models import OperationCenter
from profits.models import Profit

operation_centers = OperationCenter.objects.all()
RATIO_OF_USERS_PLACEING_ORDERS = 0.2
TOTAL_USERS_PLACING_ORDERS = int(User.objects.count()*RATIO_OF_USERS_PLACEING_ORDERS)
RATIO_OF_TOTAL_USERS_WITH_OPERATION_CENTERS = 0.1
TOTAL_USERS_WITH_OPERATION_CENTERS = int(User.objects.count()*RATIO_OF_TOTAL_USERS_WITH_OPERATION_CENTERS)
TOTAL_ORDERS_PER_USER = 20
ORDER_QUANTITY_STD = 10

def get_random_user():
    number_of_users = User.objects.count() - 1
    random_index = int(random.random()*number_of_users)+1
    random_user = User.objects.get(pk = random_index)
    return random_user

def get_random_oc():
    number_of_records = OperationCenter.objects.count()
    random_index = int(random.random()*number_of_records)+1
    random_oc = OperationCenter.objects.get(pk = random_index)
    return random_oc

class Command(BaseCommand):

    help = 'calculate profits for all users'

    def handle(self, *args, **options):
        #self.stdout.write("TOTAL_USERS %i" % TOTAL_USERS)
        for operation_center in operation_centers:
            count = User.objects.all().count()
            slice = random.random() * (count - TOTAL_USERS_WITH_OPERATION_CENTERS)
            users = User.objects.all()[slice: slice+TOTAL_USERS_WITH_OPERATION_CENTERS]

        for user in users:
            profile = Profile.objects.get(user=user)
            profile.operation_center = get_random_oc()
            profile.save()

        for operation_center in operation_centers:
            net = 0.0
            id = operation_center.id
            profits = Profit.objects.filter(user__profile__operation_center__id=id, symbol='TOTAL')
            for profit in profits:
                net = net + profit.net
            oc = OperationCenter.objects.get(id=id)
            oc.profit = round(net, 2)
            oc.save()
