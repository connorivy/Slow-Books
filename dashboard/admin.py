from django.contrib import admin
from .models import employee, customer, vendor

# Register your models here.
admin.site.register(employee)
admin.site.register(customer)
admin.site.register(vendor)
