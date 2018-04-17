from django.contrib import admin
from operation_centers.models import OperationCenter

# Register your models here.

class OperationCenterAdmin(admin.ModelAdmin):
    list_display = ['name', 'users', 'profit']
    search_fields = ['user__username']

    def users(self, obj):
        return ", ".join([k.user.username for k in obj.profile_set.all()])

admin.site.register(OperationCenter, OperationCenterAdmin)