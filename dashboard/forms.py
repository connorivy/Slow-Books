from django import forms
from django.contrib.auth.models import User
from django.db import models
from dashboard.models import employees
from crispy_forms.helper import FormHelper 

STATES = (
    ('', 'Choose...'),
    ('MG', 'Minas Gerais'),
    ('SP', 'Sao Paulo'),
    ('RJ', 'Rio de Janeiro')
)

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
        widget=forms.TextInput(attrs={'placeholder': 'Apartment, studio, or floor', 'class': 'form-control'})
    )
    city = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    state = forms.ChoiceField(choices=STATES, widget=forms.Select(attrs={'class': 'form-control'}))
    zip = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    ssn = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    hold = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    sal = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = employees
        fields = ['fname', 'lname', 'add1', 'add2', 'city', 'state', 'zip', 'ssn', 'hold', 'sal']
        # widgets = {
        #   'hold': forms.IntegerField(widget=forms.FileInput(attrs={'class': 'form-control '})),
        # }
        # hold = forms.IntegerField()
        # hold.widget.attrs.update({'class': 'form-control'})
        # fields = ['fname', 'lname', 'add1', 'add2', 'city','state']
