from django.contrib import admin
from .models import employee, customer, vendor, invoice

# Register your models here.
admin.site.register(employee)
admin.site.register(customer)
admin.site.register(vendor)
admin.site.register(invoice)
