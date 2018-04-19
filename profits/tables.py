from profits.models import Profit
import django_tables2 as tables
from django.contrib.humanize.templatetags.humanize import intcomma
from django_tables2.utils import A

class ColumnWithThousandsSeparator(tables.Column):
    def render(self,value):
        return intcomma(value)

class ProfitTable(tables.Table):
    net = ColumnWithThousandsSeparator()
    user = tables.LinkColumn('user_detail', args=[A('pk')])
    """
    def __init__(self, *args, **kwargs):
        super(ProfitTable, self).__init__(*args, **kwargs)
        for column in self.base_columns:
                self.base_columns[column].verbose_name = \
                    self.Meta.model._meta.get_field(column).verbose_name
    """
    class Meta:
        model = Profit
        fields = ['user', 'symbol', 'net']
        sequence = ['user', 'symbol', 'net']