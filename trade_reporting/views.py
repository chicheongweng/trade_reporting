from django.views.generic import TemplateView
from profits.models import Profit
import random
from django.contrib.auth.models import User
from user_profile.models import Profile
from operation_centers.models import OperationCenter
from orders.models import Order
from profits.models import Profit

class IndexView(TemplateView):
    template_name = "index.html"
    
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['total_user'] = User.objects.count()
        context['total_orders'] = Order.objects.count()
        context['total_operation_centers'] = OperationCenter.objects.count()
        context['operation_centers'] = OperationCenter.objects.all()
        context['profits'] = Profit.objects.all()
        return context
