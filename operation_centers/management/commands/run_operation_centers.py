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

OPERATION_CENTERS_ID = settings.OPERATION_CENTERS_ID
RATIO_OF_USERS_PLACEING_ORDERS = 0.1
TOTAL_USERS_PLACING_ORDERS = int(User.objects.count()*RATIO_OF_USERS_PLACEING_ORDERS)
TOTAL_ORDERS_PER_USER = 20
ORDER_QUANTITY_STD = 10

def get_random_user():
    number_of_users = User.objects.count() - 1
    random_index = int(random.random()*number_of_users)+1
    random_user = User.objects.get(pk = random_index)
    return random_user

class Command(BaseCommand):

    help = 'calculate profits for all users'

    def handle(self, *args, **options):
        #self.stdout.write("TOTAL_USERS %i" % TOTAL_USERS)
        for id in OPERATION_CENTERS_ID:
            oc = OperationCenter.objects.get(id=id)
            user=get_random_user()
            profile = Profile.objects.get(user=user)
            profile.operation_center = oc
            profile.save()


