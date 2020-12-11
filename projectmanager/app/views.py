from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from .forms import ExtendedFacultyCreationForm
from django.contrib import messages, auth
from django.shortcuts import render, redirect


class Homepage(TemplateView):
    template_name = 'index.html'

class RegisterPage(TemplateView):
    template_name = 'register.html'

class LoginPage(TemplateView):
    template_name = 'login.html'

class Dashboard(TemplateView):
    template_name = 'dashboard.html'
    
class LogoutPage(TemplateView):
    template_name = 'logout.html'



def facultyRegistration(request):
    if request.method == 'POST':
        form = ExtendedFacultyCreationForm(request.POST)
        if form.is_valid():
            form.save()
            ven = form.cleaned_data.get('user')
            print(ven)
            email = form.cleaned_data.get('email')
            messages.success(request, f'Account created for {email}.')
            return redirect('login')
    else:
        form = ExtendedFacultyCreationForm()
    return render(request, 'faculty_register.html', {'form': form})
