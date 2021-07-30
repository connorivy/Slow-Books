from django import forms
from django.contrib.auth.models import User
from django.db import models
from dashboard.models import employees
from crispy_forms.helper import FormHelper 

class addEmployee(forms.ModelForm):
    helper = FormHelper()
    helper.form_show_labels = False

    fname = forms.CharField()
    lname = forms.CharField()
    add1 = forms.CharField()
    add2 = forms.CharField()

    class Meta:
        model = employees
        # fields = ['fname', 'lname', 'add1', 'add2', 'city', 'state', 'zip', 'ssn', 'with', 'sal', 'mes']
        fields = ['fname', 'lname', 'add1', 'add2', 'city','state']
