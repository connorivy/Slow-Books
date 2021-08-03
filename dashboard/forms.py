from django import forms
from django.contrib.auth.models import User
from django.db import models
from dashboard.models import employee, customer, vendor, invoice, po, product
from crispy_forms.helper import FormHelper 

STATES = [( '', 'Choose...'), ('AL', 'Alabama'),('AK', 'Alaska'),('AZ', 'Arizona'),('AR', 'Arkansas'),('CA', 'California'),('CO', 'Colorado'),('CT', 'Connecticut'),('DE', 'Delaware'),('FL', 'Florida'),('GA', 'Georgia'),('HI', 'Hawaii'),('ID', 'Idaho'),('IL', 'Illinois'),('IN', 'Indiana'),('IA', 'Iowa'),('KS', 'Kansas'),('KY', 'Kentucky'),('LA', 'Louisiana'),('ME', 'Maine'),('MD', 'Maryland'),('MA', 'Massachusetts'),('MI', 'Michigan'),('MN', 'Minnesota'),('MS', 'Mississippi'),('MO', 'Missouri'),('MT', 'Montana'),('NE', 'Nebraska'),('NV', 'Nevada'),('NH', 'New Hampshire'),('NJ', 'New Jersey'),('NM', 'New Mexico'),('NY', 'New York'),('NC', 'North Carolina'),('ND', 'North Dakota'),('OH', 'Ohio'),('OK', 'Oklahoma'),('OR', 'Oregon'),('PA', 'Pennsylvania'),('RI', 'Rhode Island'),('SC', 'South Carolina'),('SD', 'South Dakota'),('TN', 'Tennessee'),('TX', 'Texas'),('UT', 'Utah'),('VT', 'Vermont'),('VA', 'Virginia'),('WA', 'Washington'),('WV', 'West Virginia'),('WI', 'Wisconsin'),('WY', 'Wyoming')]


class addEmployee(forms.ModelForm):
    helper = FormHelper()
    helper.form_show_labels = False

    fname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    lname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    add1 = forms.CharField(
        label='Address',
        widget=forms.TextInput(attrs={'placeholder': '1234 Main St', 'class': 'form-control'})
    )
    add2 = forms.CharField(
        required= False,
        widget=forms.TextInput(attrs={'placeholder': 'Apartment, studio, or floor', 'class': 'form-control'})
    )
    city = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    state = forms.ChoiceField(choices=STATES, widget=forms.Select(attrs={'class': 'form-control'}))
    zipcode = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    ssn = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    withholding = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    salary = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = employee
        fields = ['fname', 'lname', 'add1', 'add2', 'city', 'state', 'zipcode', 'ssn', 'withholding', 'salary']

class addCustomer(forms.ModelForm):
    helper = FormHelper()
    helper.form_show_labels = False

    fname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    lname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    add1 = forms.CharField(
        label='Address',
        widget=forms.TextInput(attrs={'placeholder': '1234 Main St', 'class': 'form-control'})
    )
    add2 = forms.CharField(
        required= False,
        widget=forms.TextInput(attrs={'placeholder': 'Apartment, studio, or floor', 'class': 'form-control'})
    )
    city = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    state = forms.ChoiceField(choices=STATES, widget=forms.Select(attrs={'class': 'form-control'}))
    zipcode = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = customer
        fields = ['fname', 'lname', 'email', 'phone', 'add1', 'add2', 'city', 'state', 'zipcode']

class addVendor(forms.ModelForm):
    helper = FormHelper()
    helper.form_show_labels = False

    bizname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    part = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    cost = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control'}))

    fname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    lname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    add1 = forms.CharField(
        label='Address',
        widget=forms.TextInput(attrs={'placeholder': '1234 Main St', 'class': 'form-control'})
    )
    add2 = forms.CharField(
        required= False,
        widget=forms.TextInput(attrs={'placeholder': 'Apartment, studio, or floor', 'class': 'form-control'})
    )
    city = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    state = forms.ChoiceField(choices=STATES, widget=forms.Select(attrs={'class': 'form-control'}))
    zipcode = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = vendor
        fields = ['bizname', 'part', 'cost', 'fname', 'lname', 'email', 'phone', 'add1', 'add2', 'city', 'state', 'zipcode']

class addInvoice(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super(addInvoice, self).__init__(*args, **kwargs)
    helper = FormHelper()
    helper.form_show_labels = False

    # the next 8ish lines of code are embarrasing. I need to learn queries 
    q_prods = product.objects.all().values()
    print('q_prods', q_prods)
    ids = [prod3['id'] for prod3 in q_prods]
    name = [prod3['name'] for prod3 in q_prods]
    l_prods = [( '', 'Choose...')]

    for index in range(len(q_prods)):
        l_prods.append((ids[index],f'{name[index]}'))
    print('l_prods', l_prods)

    prod = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control prodchoices'}),choices=l_prods)

    invoice_num = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    cost = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control prodcost', 'readonly':''}))

    # the next 10 lines of code are embarrasing. I need to learn queries 
    q_customers = customer.objects.all().values()
    ids = [customer3['id'] for customer3 in q_customers]
    fname = [customer3['fname'] for customer3 in q_customers]
    lname = [customer3['lname'] for customer3 in q_customers]
    l_customers = [( '', 'Choose...')]

    for index in range(len(q_customers)):
        l_customers.append((ids[index],f'{fname[index]} {lname[index]}'))

    # customers = customer.objects.filter(author=author).values_list('id', flat=True)

    cust = forms.ChoiceField(choices=l_customers, widget=forms.Select(attrs={'class': 'form-control'}))
    # customer = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    quant = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))

    class Meta:
        model = invoice
        fields = ['prod', 'invoice_num', 'cost', 'cust', 'quant']

class addPO(forms.ModelForm):
    helper = FormHelper()
    helper.form_show_labels = False

    part = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control vendorpart', 'readonly':''}))
    cost = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control vendorcost', 'readonly':''}))

    # the next 10 lines of code are embarrasing. I need to learn queries 
    q_vendor = vendor.objects.all().values()
    ids = [vendor3['id'] for vendor3 in q_vendor]
    name = [vendor3['bizname'] for vendor3 in q_vendor]
    l_vendors = [( '', 'Choose...')]

    for index in range(len(q_vendor)):
        l_vendors.append((ids[index],f'{name[index]}'))

    ven = forms.ChoiceField(choices=l_vendors, widget=forms.Select(attrs={'class': 'form-control vendorchoices'}))
    quant = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))

    class Meta:
        model = po
        fields = ['ven', 'part', 'cost', 'quant']

class addProduct(forms.ModelForm):
    helper = FormHelper()
    helper.form_show_labels = False

    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    # the next 8ish lines of code are embarrasing. I need to learn queries 
    q_vendor = vendor.objects.all().values()
    ids = [vendor3['id'] for vendor3 in q_vendor]
    name = [vendor3['part'] for vendor3 in q_vendor]
    l_parts = []

    for index in range(len(q_vendor)):
        l_parts.append((ids[index],f'{name[index]}'))

    part_ids = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}),choices=l_parts)

    part_quants = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    cost = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control'}))

    class Meta:
        model = product
        fields = ['name', 'part_ids', 'part_quants', 'cost']

class MyForm(forms.Form):
    # part = forms.CharField(
    #     widget=forms.TextInput(attrs={'class': 'form-control'},forms.HiddenInput()
    # ))
    # cost = forms.DecimalField(
    #     widget=forms.NumberInput(attrs={'class': 'form-control'},forms.HiddenInput()
    # ))
    # quant = forms.IntegerField(
    #     widget=forms.NumberInput(attrs={'class': 'form-control'},forms.HiddenInput()
    # ))
    
    original_field = forms.CharField()
    extra_field_count = forms.CharField(widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        extra_fields = kwargs.pop('extra', 0)

        super(MyForm, self).__init__(*args, **kwargs)
        self.fields['extra_field_count'].initial = extra_fields

        for index in range(int(extra_fields)):
            # generate extra fields in the number specified via extra_fields
            self.fields['extra_field_{index}'.format(index=index)] = \
                forms.CharField()

    # class Meta:
    #     model = invoice
    #     fields = ['part', 'cost', 'quant']