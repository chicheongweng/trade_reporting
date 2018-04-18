from django.contrib import admin
from operation_centers.models import OperationCenter

# Register your models here.

class OperationCenterAdmin(admin.ModelAdmin):
    list_display = ['name', 'total_users', 'profit']
    search_fields = ['user__username']

admin.site.register(OperationCenter, OperationCenterAdmin)