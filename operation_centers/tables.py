from operation_centers.models import OperationCenter
import django_tables2 as tables
from django.contrib.humanize.templatetags.humanize import intcomma

class ColumnWithThousandsSeparator(tables.Column):
    def render(self,value):
        return intcomma(value)

class OperationCenterTable(tables.Table):
    profit = ColumnWithThousandsSeparator()
    total_users = ColumnWithThousandsSeparator(orderable=False)

    class Meta:
        model = OperationCenter
        fields = ['name', 'total_users', 'profit']
        sequence = ['name', 'total_users', 'profit']