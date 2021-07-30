from django.db import models
from django.contrib.auth.models import User

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

