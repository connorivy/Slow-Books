from django.shortcuts import render, redirect
from django.contrib import messages
from .models import employee, customer, vendor
from .forms import addEmployee, addCustomer, addVendor, MyForm

# Create your views here.
def home(request):
    return render(request,'dashboard/home.html')

def employees(request):
    if request.method == 'POST':
        form = addEmployee(request.POST)
        if form.is_valid():
            form.save()
            fname = form.cleaned_data.get('fname')
            lname = form.cleaned_data.get('lname')
            messages.success(request, f'{fname} {lname} added to employees')
            # return redirect('dashboard-employees')
    else:
        form = addEmployee()

    context = {
        'form': form,
        'employees': employee.objects.all().values()
    }

    return render(request, 'dashboard/employees.html', context)

def customers(request):
    if request.method == 'POST':
        form = addCustomer(request.POST)
        if form.is_valid():
            form.save()
            fname = form.cleaned_data.get('fname')
            lname = form.cleaned_data.get('lname')
            messages.success(request, f'{fname} {lname} added to customers')
            # return redirect('dashboard-customers')
    else:
        form = addCustomer()

    context = {
        'form': form,
        'customers': customer.objects.all().values()
    }

    return render(request, 'dashboard/customers.html', context)

def vendors(request):
    if request.method == 'POST':
        form = addVendor(request.POST)
        if form.is_valid():
            form.save()
            bizname = form.cleaned_data.get('bizname')
            messages.success(request, f'{bizname} added to vendors')
            # return redirect('dashboard-vendors')
    else:
        form = addVendor()

    context = {
        'form': form,
        'vendors': vendor.objects.all().values()
    }
    print(context['vendors'])

    return render(request, 'dashboard/vendors.html', context)

def invoice(request):
    return render(request, 'dashboard/invoice.html')

def myview(request):
    if request.method == 'POST':
        form = MyForm(request.POST, extra=request.POST.get('extra_field_count'))
        if form.is_valid():
            print("valid!")
    else:
        form = MyForm()
        
    return render(request, "dashboard/test.html", { 'form': form })