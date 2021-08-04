from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(employee)
admin.site.register(customer)
admin.site.register(vendor)
admin.site.register(invoice)
admin.site.register(po)
admin.site.register(product)
admin.site.register(inventory)
admin.site.register(payroll)
