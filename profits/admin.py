from django.contrib import admin
from profits.models import Profit

class ProfitAdmin(admin.ModelAdmin):
    list_display = ['user', 'symbol', 'net']
    search_fields = ['user__username']

admin.site.register(Profit, ProfitAdmin)