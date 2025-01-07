from .models import *
from django import forms
from django.core.exceptions import ValidationError

class UserRegisterForm(forms.ModelForm):
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            'class': 'form',
            'placeholder': 'Enter your password',
            'id': 'password1'
        })
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={
            'class': 'form',
            'placeholder': 'Re-enter password',
            'id': 'password2'
        })
    )
    class Meta:
        model = RegisterUsers
        fields = ['emp_id','emp_name', 'emp_email', 'emp_phn_number',  'emp_department', 'emp_role', 'password1', 'password2']
        widgets = {
            'emp_id': forms.TextInput(attrs={
                'class': 'form',
                'placeholder': 'Enter your Employee ID',
                'id': 'emp_id'
            }),
            'emp_name': forms.TextInput(attrs={
                'class': 'form',
                'placeholder': 'Enter your Name',
                'id': 'emp_name'
            }),
            'emp_email': forms.EmailInput(attrs={
                'class': 'form',
                'placeholder': 'e.g. something@steponestepahead.com',
                'id': 'emp_email'
            }),
            'emp_phn_number': forms.TextInput(attrs={
                'class': 'form',
                'placeholder': 'Enter your phone Number',
                'id': 'emp_phn_number'
            }),
            'emp_department': forms.TextInput(attrs={
                'class': 'form',
                'placeholder': 'E.g. Testing',
                'id': 'emp_ddepartment'
            }),
            'emp_role': forms.TextInput(attrs={
                'class': 'form',
                'placeholder': 'E.g. Technical Manager',
                'id': 'emp_role'
            }),
        }

    #Checking here if email exists in our database
    def clean_email(self):
        email = self.cleaned_data.get('emp_email')
        if RegisterUsers.objects.filter(emp_email=email).exists():
            raise ValidationError("A user with this email already exists.")
        return email
    
    #Checking if phone number exists in our database
    def clean_phn_number(self):
        phn_number=self.cleaned_data.get('emp_phn_number')
        if RegisterUsers.objects.filter(emp_email=phn_number).exists():
            raise ValidationError("A user with this phone number already exists.")
        return phn_number

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        # Checking here if both passwords do match
        if password1 and password2 and password1 != password2:
            self.add_error('password2', 'Passwords do not match')

        return cleaned_data
    
class LoginForm(forms.Form):
    emp_email = forms.CharField(
        label="Email",max_length=100, widget=forms.TextInput(attrs={
        'placeholder': 'Email',
        'id': 'emp_email'
    }))
    password = forms.CharField(
        label="Password",widget=forms.PasswordInput(attrs={
        'placeholder': 'Password',
        'id': 'password'
    }))