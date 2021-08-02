from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='dashboard-home'),
    path('employees/', views.employees, name="dashboard-employees"),
    path('customers/', views.customers, name="dashboard-customers"),
    path('vendors/', views.vendors, name="dashboard-vendors"),
    path('invoice/', views.invoices, name="dashboard-invoice"),
    path('inventory/', views.inventoryView, name="dashboard-inventory"),


    path('test/', views.myview, name="dashboard-myview"),
]