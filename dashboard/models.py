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
    ssn = models.CharField(max_length=18) 
    withholding = models.IntegerField()
    salary = models.CharField(max_length=25)

    # definitely remove null and blank in the future to make the employer required
    employer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.fname} {self.lname}'

class customer(models.Model):
    fname = models.CharField(max_length=25)
    lname = models.CharField(max_length=25)
    email = models.EmailField()
    phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
    phone = models.CharField(validators = [phoneNumberRegex], max_length = 16, unique = True)
    add1 = models.CharField(max_length=50)
    add2 = models.CharField(max_length=10, null=True, blank=True)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    zipcode = models.IntegerField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.fname} {self.lname}'

class vendor(models.Model):
    bizname = models.CharField(max_length=25)
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
        return f'{self.fname} {self.lname}'

class invoice(models.Model):
    customer = models.CharField(max_length=25)
    invoice_num = models.IntegerField(null=True, blank=True)
    prod = models.CharField(max_length=25)
    quant = models.IntegerField()
    cost = models.DecimalField(max_digits=10, decimal_places=4)

    date_added = models.DateTimeField(default=timezone.now)
    paid = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return f'{self.invoice_num}'

class po(models.Model):
    ven = models.CharField(max_length=25)
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
    cost = models.DecimalField(max_digits=10, decimal_places=4)
    threshold = models.IntegerField(null=True, blank=True)
    

    def __str__(self):
        return f'{self.quant} {self.part}'

class product(models.Model):
    name = models.CharField(max_length=25)
    part_ids = models.CharField(max_length=25)
    part_quants = models.IntegerField()
    cost = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True)
    

    def __str__(self):
        return f'{self.name}'


