from django.contrib import admin
from operation_centers.models import OperationCenter

# Register your models here.

class OperationCenterAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(OperationCenter, OperationCenterAdmin)