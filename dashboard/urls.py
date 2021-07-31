from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='dashboard-home'),
    path('employees/', views.employees, name="dashboard-employees"),
    path('customers/', views.customers, name="dashboard-customers"),
]