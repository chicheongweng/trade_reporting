from django.views.generic import TemplateView
from profits.models import Profit
import random
from django.contrib.auth.models import User
from user_profile.models import Profile
from operation_centers.models import OperationCenter
from orders.models import Order
from profits.models import Profit
from profits.tables import ProfitTable
from operation_centers.tables import OperationCenterTable
from django_tables2 import RequestConfig
from django.views.generic.detail import DetailView
from profits.tables import ProfitTable
from orders.tables import OrderTable

class IndexView(TemplateView):
    template_name = "index.html"
    
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['total_user'] = User.objects.count()
        context['total_orders'] = Order.objects.count()
        context['total_operation_centers'] = OperationCenter.objects.count()

        oc_table = OperationCenterTable(OperationCenter.objects.all())
        context['operation_centers'] = RequestConfig(self.request, paginate={'per_page': 10}).configure(oc_table)

        profits_table = ProfitTable(Profit.objects.all())
        context['profits'] = RequestConfig(self.request, paginate={'per_page': 10}).configure(profits_table)
        return context

class UserDetailView(DetailView):

    model = User
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        context = super(UserDetailView, self).get_context_data(**kwargs)
        
        profits_table = ProfitTable(Profit.objects.filter(user=self.get_object()))
        context['profits'] = RequestConfig(self.request, paginate={'per_page: 10'}).configure(profits_table)
        
        orders_table = OrderTable(Order.objects.filter(user=self.get_object()))
        context['orders'] = RequestConfig(self.request, paginate={'per_page': 10}).configure(orders_table)
        return context

    