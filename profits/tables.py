from profits.models import Profit
import django_tables2 as tables
from django.contrib.humanize.templatetags.humanize import intcomma
from django_tables2.utils import A

class ColumnWithThousandsSeparator(tables.Column):
    def render(self,value):
        return intcomma(value)

class ProfitTable(tables.Table):
    net = ColumnWithThousandsSeparator()
    user = tables.LinkColumn('user_detail', args=[A('user.pk')], order_by=('user.username'))
    
    class Meta:
        model = Profit
        fields = ['user', 'symbol', 'net']
        sequence = ['user', 'symbol', 'net']