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
def random_first_name(loc='en_US'):
    return Faker(loc).first_name()

def random_last_name(loc='en_US'):
    return Faker(loc).last_name()

def random_lorem(loc='en_US'):
    return Faker(loc).sentence()

def random_dob():
    return str(datetime.now()-timedelta(days=365*randint(20,50))).split(' ')[0]

def random_username(first_name, last_name):
    fake = Faker('en_US')
    return first_name.lower() + last_name.lower() + str(randint(0,999))

def random_phone(loc='zh'):
    return '+'+Faker(loc).phone_number()

class Command(BaseCommand):

    help = 'generate 10K Jobseeker profiles for Addis Ababa'

    def handle(self, *args, **options):
        for i in range(5):

            first_name = random_first_name()
            last_name = random_last_name()
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
            p.date_of_birth = random_dob()
            p.bio = random_lorem()
            p.phone_number = random_phone()
            p.save()
