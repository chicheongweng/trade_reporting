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

TOTAL_ORDERS = 1000

def random_date(min=20,max=50):
    return str(datetime.now()-timedelta(days=365*randint(min,max))).split(' ')[0]

def random_order_type():
    return random.sample(['GLD','SLV','USDEUR','USDRMB','OIL'],1)

def random_time_stamp(years=3):
    return str(datetime.now()-timedelta(days=365*randint(0,years)))

class Command(BaseCommand):

    help = 'generate ' + TOTAL_ORDERS + 'orders'

    def handle(self, *args, **options):
        for i in range(TOTAL_ORDERS):

            first_name = random_first_name()
            last_name = random_last_name()
            username = random_username(first_name, last_name)

            number_of_records = models.Painting.objects.count()
            random_index = int(random.random()*number_of_records)+1
            random_paint = models.Painting.get(pk = random_index)

            new_user = User.objects.create(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=username+"@gmail.com",
                password=make_password("Abcde12345")
            )
            new_user.save()
            self.stdout.write("user.id %i" % new_user.id)

            p = Profile.objects.get(user=new_user)
            p.date_of_birth = random_dob()
            p.bio = random_lorem()
            p.phone_number = random_phone()
            p.save()
