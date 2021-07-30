from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper 

class UserRegisterForm(UserCreationForm):
    helper = FormHelper()
    helper.form_show_labels = False
    # email = forms.EmailField()

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Email Address', 'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
            self.fields['username'].widget.attrs['placeholder'] = 'Business Name'
            self.fields['email'].widget.attrs['placeholder'] = 'Email'
            self.fields['password1'].widget.attrs['placeholder'] = 'Password'
            self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
