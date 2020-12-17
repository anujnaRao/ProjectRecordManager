from django import forms

from django.contrib.auth.forms import UserCreationForm
from .models import Faculty, Student, Project, Team
from tinymce.widgets import TinyMCE


class CheckboxInput(forms.CheckboxInput):
    def __init__(self, default=False, *args, **kwargs):
        super(CheckboxInput, self).__init__(*args, **kwargs)
        self.default = default

    def value_from_datadict(self, data, files, name):
        if name not in data:
            return self.default
        return super(CheckboxInput, self).value_from_datadict(data, files, name)


class ExtendedFacultyCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Email", max_length=100, widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Email Id'
    }))

    name = forms.CharField(label="Name", max_length=100, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Name'
    }))

    phone = forms.CharField(label="Mobile", max_length=100, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Mobile Number'
    }))

    password1 = forms.CharField(max_length=50, label='Password', widget=forms.PasswordInput(attrs={
        "class": "form-control",
        "placeholder": "Enter password"
    }))
    password2 = forms.CharField(max_length=50, label='Confirm password', widget=forms.PasswordInput(attrs={
        "class": "form-control",
        "placeholder": "Confirm password"
    }))

    isfaculty = forms.BooleanField(
        widget=CheckboxInput(default=True), required=False)

    class Meta:
        model = Faculty
        fields = ['email', 'phone', 'name',
                  'password1', 'password2', 'isfaculty']


class ExtendedStudentCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Email", max_length=100, widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Email Id'
    }))

    name = forms.CharField(label="Name", max_length=100, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Name'
    }))

    usn = forms.CharField(label="USN", max_length=100, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'USN'
    }))
    phone = forms.CharField(label="Mobile", max_length=100, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Mobile Number'
    }))

    password1 = forms.CharField(max_length=50, label='Password', widget=forms.PasswordInput(attrs={
        "class": "form-control",
        "placeholder": "Enter password"
    }))
    password2 = forms.CharField(max_length=50, label='Confirm password', widget=forms.PasswordInput(attrs={
        "class": "form-control",
        "placeholder": "Confirm password"
    }))

    isstudent = forms.BooleanField(
        widget=CheckboxInput(default=True), required=False)

    class Meta:
        model = Student
        fields = ['email', 'phone', 'name', 'password1',
                  'password2', 'usn', 'batch', 'section', 'isstudent']


class ProjectForm(forms.ModelForm):
    synopsis = forms.CharField(
        label="Synopsis", widget=TinyMCE(attrs={'cols': 50, 'rows': 10, "class": "form-control",
                                                "placeholder": "Synopsis details"}))
    phase1 = forms.CharField(
        label="Phase 1", widget=TinyMCE(attrs={'cols': 50, 'rows': 10, "class": "form-control",
                                               "placeholder": "Phase 1 details"}))
    phase2 = forms.CharField(
        label="Phase 2", widget=TinyMCE(attrs={'cols': 50, 'rows': 10, "class": "form-control",
                                               "placeholder": "Phase 2 details"}))
    fianle = forms.CharField(
        label="Final Phase", widget=TinyMCE(attrs={'cols': 50, 'rows': 10, "class": "form-control",
                                                   "placeholder": "Enter Final phase details"}))

    class Meta:
        model = Project
        fields = ['project_title', 'synopsis', 'phase1', 'phase2', 'fianle']
