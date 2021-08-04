
from django.db.models import ForeignKey
from dashboard.models import *

def query_to_list(query, fields_to_ignore=[]):
    data = []
    for obj in query:
        sub_data = []
        for field in obj._meta.get_fields():
            if field.name in fields_to_ignore:
                continue
            value = field.value_from_object(obj)
            print(field.name)
            if isinstance(field, ForeignKey):
                model = field.remote_field.model
                value = str(model.objects.get(pk=value))
            sub_data.append(value)
            print('value', value)
            print('sub_data', sub_data)
        data.append(sub_data)
    return data

def get_choices_list(model):

    query = model.objects.all()
    ids = [obj.pk for obj in query]
    name = [str(obj) for obj in query]
    list = [( '', 'Choose...')]

    for index in range(len(query)):
        list.append((ids[index],f'{name[index]}'))

    print(model, list)
    return list

def get_withheld_amount(salary):
    fed = 0
    ss = 0
    medicare = 0

    ss = .062 * min(128000, salary)
    medicare = .0145 * salary

    if salary > 523601:
        fed = (salary - 523601) * .37 + 995 + 3668.88 + 10086.78 + 18851.76 + 14239.68 + 109960.90
    elif salary > 209425:
        fed = (salary - 209425) * .35 + 995 + 3668.88 + 10086.78 + 18851.76 + 14239.68
    elif salary > 164925:
        fed = (salary - 164925) * .32 + 995 + 3668.88 + 10086.78 + 18851.76
    elif salary > 86375:
        fed = (salary - 86375) * .24 + 995 + 3668.88 + 10086.78
    elif salary > 40525:
        fed = (salary - 40525) * .22 + 995 + 3668.88
    elif salary > 9950:
        fed = (salary - 9950) * .12 + 995
    else:
        fed = salary * .1

    return fed/12, ss/12, medicare/12

def get_cash(initial, invoices, pos, payroll, inventory):
    cash = initial 
    sales = 0
    cogs = 0
    inv = 0
    pay = 0
    tax = 0
    bills = 1250.00
    ann_exp = 13750.00
    lib = 0

    for invoice in invoices:
        sales += invoice.price
        # cogs += invoice.product.costper * item.quant
        prod = invoice.prod
        vendor_ids = prod.part_ids
        quants_in_inventory = prod.part_quants.split('/')

        disallowed_characters = "[]'"

        for character in disallowed_characters:
            vendor_ids = vendor_ids.replace(character, "")

        vendor_ids = vendor_ids.split(",")

        print(vendor_ids)
        for index in range(len(vendor_ids)):
            vendor_ids[index] = vendor_ids[index].strip(' ')
            vendor_entry = vendor.objects.get(pk=vendor_ids[index])
            cogs += vendor_entry.cost * invoice.quant * int(quants_in_inventory[index])

    # cash += sales

    for po in pos:
        cash -= po.cost

    for item in inventory:
        inv += item.value

    for item in payroll:
        pay += item.sal_after_tax
        tax += item.fed
        tax += item.ss
        tax += item.med
        tax += item.amount_to_match
    cash -= pay
    cash -= tax

    gp = round(sales - cogs,2)
    expenses = round(float(pay)+float(tax)+float(bills)+float(ann_exp),2)
    ar = sales
    # inv -= 

    context = {
        'cash': round(cash,2),
        'inventory': round(inv,2),
        'current_assets': round(cash+inv+ar,2),
        'current_liabilities': lib,
        'sales': round(sales, 2),
        'cogs': round(cogs, 2),
        'gp': gp,
        'payroll': round(pay,2),
        'withholding': round(tax,2),
        'bills': bills,
        'ann_exp': ann_exp,
        'expenses': expenses,
        'net_income': float(gp) - float(expenses),
        'nw': round(float(cash)+float(inv)+float(ar)-float(lib),2),
        'ar': round(ar,2),
    }


    return context
