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

fake=Faker('en_US')

end=datetime.now()
start=end-timedelta(days=365*3)

def random_lorem(loc='en_US'):
    return Faker(loc).sentence()

def random_dob():
    start=end-timedelta(days=365*50)
    return start+(end-start)*random.random()

def random_username(first_name, last_name):
    fake = Faker('en_US')
    return first_name.lower() + last_name.lower() + str(randint(0,999))

def random_date():
    return start+(end-start)*random.random()

def random_phone(loc='zh'):
    return '+'+Faker(loc).phone_number()

class Command(BaseCommand):

    help = 'generate 10K Jobseeker profiles for Addis Ababa'

    def handle(self, *args, **options):
        for i in range(100):

            first_name = fake.first_name()
            last_name = fake.last_name()
            username = random_username(first_name, last_name)

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
            #p.date_of_birth = random_dob()
            p.bio = random_lorem()
            p.phone_number = random_phone()
            p.save()
