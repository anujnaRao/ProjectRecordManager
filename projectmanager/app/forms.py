from django import forms

from django.contrib.auth.forms import UserCreationForm
from .models import Faculty,Student,Project,Team

class ExtendedFacultyCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Email", max_length=100, widget=forms.EmailInput(attrs={
        'class': 'form-control rounded-pill',
        'placeholder': 'Email Id'
    }))

    name = forms.CharField(label="Name", max_length=100, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control rounded-pill',
        'placeholder': 'Name'
    }))

    phone = forms.CharField(label="Mobile", max_length=100, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control rounded-pill',
        'placeholder': 'Mobile Number'
    }))

    password1 = forms.CharField(max_length=50, label='Password', widget=forms.PasswordInput(attrs={
        "class": "form-control rounded-pill",
        "placeholder": "Enter password"
    }))
    password2 = forms.CharField(max_length=50, label='Confirm password', widget=forms.PasswordInput(attrs={
        "class": "form-control rounded-pill",
        "placeholder": "Confirm password"
    }))

    class Meta:
        model = Faculty
        fields = ['email', 'phone','name','password1','password2']