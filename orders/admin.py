from django.contrib import admin
from orders.models import Order

# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'time_stamp', 'symbol', 'order_type', 'quantity', 'price']

admin.site.register(Order, OrderAdmin)
