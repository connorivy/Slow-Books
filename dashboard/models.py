from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

class employee(models.Model):
    fname = models.CharField(max_length=25)
    lname = models.CharField(max_length=25)
    add1 = models.CharField(max_length=50)
    add2 = models.CharField(max_length=10, null=True, blank=True)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    zipcode = models.IntegerField()
    ssn = models.CharField(primary_key=True,max_length=18) 
    withholding = models.IntegerField()
    salary = models.IntegerField()

    # definitely remove null and blank in the future to make the employer required
    employer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.fname} {self.lname}'

class customer(models.Model):
    fname = models.CharField(max_length=25)
    lname = models.CharField(max_length=25)
    email = models.EmailField()
    phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
    phone = models.CharField(primary_key=True, validators = [phoneNumberRegex], max_length = 16, unique = True)
    add1 = models.CharField(max_length=50)
    add2 = models.CharField(max_length=10, null=True, blank=True)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    zipcode = models.IntegerField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.fname} {self.lname}'

class vendor(models.Model):
    bizname = models.CharField(primary_key=True, max_length=25)
    part = models.CharField(max_length=25)
    cost = models.DecimalField(max_digits=10, decimal_places=4)
    fname = models.CharField(max_length=25, null=True, blank=True)
    lname = models.CharField(max_length=25, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
    phone = models.CharField(validators = [phoneNumberRegex], max_length = 16, unique = True, null=True, blank=True, default=None)
    add1 = models.CharField(max_length=50, null=True, blank=True)
    add2 = models.CharField(max_length=10, null=True, blank=True)
    city = models.CharField(max_length=20, null=True, blank=True)
    state = models.CharField(max_length=20, null=True, blank=True)
    zipcode = models.IntegerField(null=True, blank=True)
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.bizname}'

class product(models.Model):
    name = models.CharField(primary_key=True, max_length=25)
    part_ids = models.CharField(max_length=150)
    part_quants = models.CharField(max_length=25)
    price = models.DecimalField(max_digits=10, decimal_places=4)
    

    def __str__(self):
        return f'{self.name}'

class invoice(models.Model):
    invoice_num = models.AutoField(primary_key=True)
    cust = models.ForeignKey(customer, on_delete=models.CASCADE)
    prod = models.ForeignKey(product, on_delete=models.CASCADE)
    quant = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=4)

    date_added = models.DateTimeField(default=timezone.now)
    paid = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return f'{self.invoice_num}'

class po(models.Model):
    ven = models.ForeignKey(vendor, on_delete=models.CASCADE)
    part = models.CharField(max_length=25)
    quant = models.IntegerField()
    cost = models.DecimalField(max_digits=10, decimal_places=4)

    date_added = models.DateTimeField(default=timezone.now)
    paid = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return f'{self.quant} {self.part}'

class inventory(models.Model):
    part = models.CharField(max_length=25)
    quant = models.IntegerField()
    costper = models.DecimalField(max_digits=10, decimal_places=4)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    threshold = models.CharField(max_length=2, null=True, blank=True)
    

    def __str__(self):
        return f'{self.quant} {self.part}'

class payroll(models.Model):
    date = models.DateTimeField(default=timezone.now)
    emp = models.ForeignKey(employee, on_delete=models.CASCADE)

    fed = models.DecimalField(max_digits=8, decimal_places=2)
    ss = models.DecimalField(max_digits=8, decimal_places=2)
    med = models.DecimalField(max_digits=8, decimal_places=2)
    sal_after_tax = models.DecimalField(max_digits=8, decimal_places=2)
    amount_to_match = models.DecimalField(max_digits=8, decimal_places=2)
    
    def __str__(self):
        return f'{self.emp} {self.date}'

class balancesheet(models.Model):
    cash = models.DecimalField(max_digits=8, decimal_places=2)
    # acounts_recievable = models.DecimalField(max_digits=8, decimal_places=2)
    # building = models.DecimalField(max_digits=8, decimal_places=2)
    # med = models.DecimalField(max_digits=8, decimal_places=2)
    # sal_after_tax = models.DecimalField(max_digits=8, decimal_places=2)
    # amount_to_match = models.DecimalField(max_digits=8, decimal_places=2)
    
    # def __str__(self):
    #     return f'{self.emp} {self.date}'


