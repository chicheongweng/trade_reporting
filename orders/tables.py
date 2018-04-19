from orders.models import Order
import django_tables2 as tables
from django.contrib.humanize.templatetags.humanize import intcomma
from django_tables2.utils import A

class ColumnWithThousandsSeparator(tables.Column):
    def render(self,value):
        return intcomma(value)

class OrderTable(tables.Table):
    net = ColumnWithThousandsSeparator()
    
    class Meta:
        model = Order
        fields = ['time_stamp', 'order_type', 'symbol', 'price']
        sequence = ['time_stamp', 'order_type', 'symbol', 'price']
