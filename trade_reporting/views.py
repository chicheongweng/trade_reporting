from django.views.generic import TemplateView
from operation_centers.models import OperationCenter
from profits.models import Profit
import random

class IndexView(TemplateView):
    template_name = "index2.html"
    
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['number'] = random.randrange(1, 100)
        return context
