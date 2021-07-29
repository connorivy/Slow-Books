from django.db import models

class employees(models.Model):
    fname = models.CharField(max_length=25)
    lname = models.CharField(max_length=25)
    add1 = models.CharField(max_length=25)
    add2 = models.CharField(max_length=25)
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=25)
    zipcode = models.IntegerField()
    ssn = models.CharField(max_length=25)
    withholding = models.IntegerField(max_length=25)
    salary = models.CharField(max_length=25)
    message = fname = models.CharField(max_length=100)

