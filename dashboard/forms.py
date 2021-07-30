from django import forms
from django.contrib.auth.models import User
from django.db import models
from dashboard.models import employees
from crispy_forms.helper import FormHelper 

STATES = (( '', 'Choose...'), ('AL', 'Alabama'),('AK', 'Alaska'),('AZ', 'Arizona'),('AR', 'Arkansas'),('CA', 'California'),('CO', 'Colorado'),('CT', 'Connecticut'),('DE', 'Delaware'),('FL', 'Florida'),('GA', 'Georgia'),('HI', 'Hawaii'),('ID', 'Idaho'),('IL', 'Illinois'),('IN', 'Indiana'),('IA', 'Iowa'),('KS', 'Kansas'),('KY', 'Kentucky'),('LA', 'Louisiana'),('ME', 'Maine'),('MD', 'Maryland'),('MA', 'Massachusetts'),('MI', 'Michigan'),('MN', 'Minnesota'),('MS', 'Mississippi'),('MO', 'Missouri'),('MT', 'Montana'),('NE', 'Nebraska'),('NV', 'Nevada'),('NH', 'New Hampshire'),('NJ', 'New Jersey'),('NM', 'New Mexico'),('NY', 'New York'),('NC', 'North Carolina'),('ND', 'North Dakota'),('OH', 'Ohio'),('OK', 'Oklahoma'),('OR', 'Oregon'),('PA', 'Pennsylvania'),('RI', 'Rhode Island'),('SC', 'South Carolina'),('SD', 'South Dakota'),('TN', 'Tennessee'),('TX', 'Texas'),('UT', 'Utah'),('VT', 'Vermont'),('VA', 'Virginia'),('WA', 'Washington'),('WV', 'West Virginia'),('WI', 'Wisconsin'),('WY', 'Wyoming'))


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
        model = employees
        fields = ['fname', 'lname', 'add1', 'add2', 'city', 'state', 'zipcode', 'ssn', 'withholding', 'salary']