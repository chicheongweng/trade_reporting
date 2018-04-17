from profits.models import Profit
import django_tables2 as tables
from django.contrib.humanize.templatetags.humanize import intcomma

class ColumnWithThousandsSeparator(tables.Column):
    def render(self,value):
        return intcomma(value)

class ProfitTable(tables.Table):
    net = ColumnWithThousandsSeparator()
    class Meta:
        model = Profit
        fields = ['user', 'symbol', 'net']
        sequence = ['user', 'symbol', 'net']