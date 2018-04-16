from django.contrib import admin
from orders.models import Order

# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'time_stamp', 'symbol', 'order_type', 'quantity', 'price']
    search_fields = ['user__username', 'symbol']
    list_filter = ['time_stamp']
admin.site.register(Order, OrderAdmin)
