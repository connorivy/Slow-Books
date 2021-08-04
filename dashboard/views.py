from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core import serializers
from django.urls import reverse
from urllib.parse import urlencode
from .models import *
from .forms import *
from utils.update_inventory import *
from utils.model_to_dict import *

# Create your views here.
def home(request):
    context = get_cash(200000, invoice.objects.all(), po.objects.all(), payroll.objects.all(), inventory.objects.all())
    
    return render(request,'dashboard/home.html', context)

def employees(request):
    if request.method == 'POST':
        addform = addEmployee(request.POST)
        payform = pay(request.POST)
        if addform.is_valid():
            addform.save()
            fname = addform.cleaned_data.get('fname')
            lname = addform.cleaned_data.get('lname')
            messages.success(request, f'{fname} {lname} added to employees')
            # return redirect('dashboard-employees')
        if payform.is_valid():
            payform.save()
    else:
        addform = addEmployee()
        payform = pay()

    context = {
        'form': addform,
        'payform':payform,
        'employees': employee.objects.all().values()
    }

    return render(request, 'dashboard/employees.html', context)

def customers(request):
    if request.method == 'POST':
        customerform = addCustomer(request.POST)
        invoiceform = addInvoice(request.POST)
        if customerform.is_valid():
            customerform.save()
            fname = customerform.cleaned_data.get('fname')
            lname = customerform.cleaned_data.get('lname')
            messages.success(request, f'{fname} {lname} added to customers')
        if invoiceform.is_valid():
            # base_url = reverse('dashboard-invoice')  # 1 /products/
            # query_string =  urlencode({
            #     'part': invoiceform.cleaned_data.get('part'),
            #     'cost': invoiceform.cleaned_data.get('cost'),
            #     'quant': invoiceform.cleaned_data.get('quant'),
            #     'invoice_num': invoiceform.cleaned_data.get('invoice_num'),
            #     'customer': invoiceform.cleaned_data.get('customer'),
            # }) 
            # url = '{}?{}'.format(base_url, query_string)  # 3 /products/?category=42
            # return redirect(url)  # 4

            # instance = invoiceform.save(commit=False)
            # cust_id = invoiceform.cleaned_data.get('cust_id')

            # instance.cust = customer.objects.get(pk = cust_id)
            # print(f'\n\n\n {instance.cust} \n\n\n')
            # instance.save()
            invoiceform.save()

            sub_inventory(request)
            return redirect('dashboard-invoice')
    else:
        customerform = addCustomer()
        invoiceform = addInvoice()

    context = {
        'customerform': customerform,
        'invoiceform': invoiceform,
        'customers': customer.objects.all().values()
    }

    return render(request, 'dashboard/customers.html', context)

def vendors(request):
    if request.method == 'POST':
        poform = addPO(request.POST)
        vendorform = addVendor(request.POST)
        if vendorform.is_valid():
            vendorform.save()
            bizname = vendorform.cleaned_data.get('bizname')
            messages.success(request, f'{bizname} added to vendors')
            # return redirect('dashboard-vendors')

        if poform.is_valid():
            part = poform.cleaned_data.get('part')
            cost = poform.cleaned_data.get('cost')
            quant = poform.cleaned_data.get('quant')
            poform.save()
            add_inventory(inventory, part, cost, quant)
    else:
        vendorform = addVendor()
        poform = addPO()

    if request.is_ajax and request.method == 'GET':
        part = request.GET.get('part', None)

    context = {
        'vendorform': vendorform,
        'poform': poform,
        'vendors': vendor.objects.all().values()
    }

    return render(request, 'dashboard/vendors.html', context)

def fillInVendorChoices(request):
    if request.is_ajax and request.method == "GET":
        # get the vendor from the client side.
        ven = request.GET.get("ven", None)
        # check for the vendor in the database.
        try:
            part = vendor.objects.get(pk = ven).part
            cost = vendor.objects.get(pk = ven).cost
        except:
            part = ''
            cost = ''
        return JsonResponse({"part":part,"cost":cost}, status = 200)
    return JsonResponse({}, status = 400)


def invoices(request):
    if request.method == 'POST':
        form = addInvoice(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-invoice', {'form': form })
    else:
        form = addInvoice()

    context = {
        'part': request.GET.get('part'),
        'cost': request.GET.get('cost'),
        'quant': request.GET.get('quant'),
        'customer': request.GET.get('quant'),
        'invoices': invoice.objects.all().values()
    }

    return render(request, 'dashboard/invoice.html', context)

def inventoryView(request):
    if request.method == 'POST':
        prodform = addProduct(request.POST)
        if prodform.is_valid():
            prodform.save()
            # fname = form.cleaned_data.get('fname')
            # lname = form.cleaned_data.get('lname')
            # messages.success(request, f'{fname} {lname} added to employees')
            # return redirect('dashboard-employees')
    else:
        prodform = addProduct()

    context = {
        'prodform': prodform,
        'inventory': inventory.objects.all().values()
    }
    print('inventory', context['inventory'])

    return render(request, 'dashboard/inventory.html', context)

def fillInProdChoices(request):
    if request.is_ajax and request.method == "GET":
        # get the vendor from the client side.
        prod = request.GET.get("prod", None)
        # check for the vendor in the database.
        try:
            price = product.objects.get(pk = prod).price
        except:
            price = ''
        return JsonResponse({"price":price}, status = 200)
    return JsonResponse({}, status = 400)

def myview(request):
    if request.method == 'POST':
        form = MyForm(request.POST, extra=request.POST.get('extra_field_count'))
        if form.is_valid():
            print("valid!")
    else:
        form = MyForm()

    return render(request, "dashboard/test.html", { 'form': form })

def transactions(request):

    context = {
        'invoices': query_to_list(invoice.objects.all(),['paid']),
        'pos': query_to_list(po.objects.all(),['paid']),
        'pays': query_to_list(payroll.objects.all(),['id'])
    }
    print('payrolls', context['pays'])

    return render(request, "dashboard/transactions.html", context)