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

RATIO_OF_USERS = 0.75
TOTAL_USERS = int(User.objects.count()*0.75)
TOTAL_ORDERS_PER_USER = 100
ORDER_QUANTITY_STD = 100
SYMBOLS = ['GLD', 'SLV', 'EURUSD', 'RMBUSD', 'OIL']

def get_random_time_stamp(years=3):
    return str(timezone.now()-timedelta(days=365*randint(0,years)))

def get_random_date(min=20,max=50):
    return str(timezone.now()-timedelta(days=365*randint(min,max))).split(' ')[0]

def get_random_order_type():
    return random.sample(SYMBOLS,1)

def get_price(symbol):
    return {
        'GLD': round(random.normalvariate(1400,10),2),
        'SLV': round(random.normalvariate(15,3),2),
        'EURUSD': round(random.normalvariate(1.2,0.1),2),
        'RMBUSD': round(random.normalvariate(0.16, 0.1),2),
        'OIL': round(random.normalvariate(60,3),2),
    }[symbol]

def get_random_user():
    number_of_users = User.objects.count() - 1
    random_index = int(random.random()*number_of_users)+1
    random_user = User.objects.get(pk = random_index)
    return random_user

def get_random_order_list(symbol, num_of_orders=1000):
    quantity_list = [int(random.normalvariate(0,ORDER_QUANTITY_STD)) for x in range(0,1000)]

    order_list = [
        {
            "symbol": symbol,
            "time_stamp": get_random_time_stamp(),
            "order_type": 'B' if x>0 else 'S',
            "quantity": x,
            "price": get_price(symbol)
        }
        for x in quantity_list
    ]
    return order_list

class Command(BaseCommand):

    help = 'generate ' + str(TOTAL_ORDERS_PER_USER) + 'orders'

    def handle(self, *args, **options):
        self.stdout.write("TOTAL_USERS %i" % TOTAL_USERS)
        for _ in range(0, TOTAL_USERS):
            for symbol in SYMBOLS:
                self.stdout.write("SYMBOL %s" % symbol)
                orders_list = get_random_order_list(symbol)
                for order in orders_list:
                    print order
                    new_order = Order.objects.create(
                        user=get_random_user(),
                        symbol=order["symbol"],
                        time_stamp=order["time_stamp"],
                        order_type=order["order_type"],
                        quantity=abs(order["quantity"]),
                        price=order["price"]
                    )
                    new_order.save()


