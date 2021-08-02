from django.contrib import admin
from .models import employee, customer, product, vendor, invoice, po

# Register your models here.
admin.site.register(employee)
admin.site.register(customer)
admin.site.register(vendor)
admin.site.register(invoice)
admin.site.register(po)
admin.site.register(product)
